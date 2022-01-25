import cv2
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from time import sleep
import re

#--↓ 去除曲線自訂函式 ↓--#
def rm_regression(img, border):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 影像轉灰階
    denoise=cv2.fastNlMeansDenoising(gray, h=30)    # 去除 Noise
    ret, thres = cv2.threshold(denoise, 127, 255,   # 門檻值轉黑白影像
                                cv2.THRESH_BINARY_INV)
    ori = thres.copy()          # 複製一份
    width = thres.shape[1]      # 黑白影像寬度
    height = thres.shape[0]     # 黑白影像高度
    thres[:, border:width-border] = 0       # 只留左右 border 寬度邊界的像素
    thres[height*3//5:height, 0: width//2] = 0   #遮掉左下區域
    thres[height*1//4:height, width//2: width] = 0  #遮掉右下區域
    #----↓ 機器學習 ↓----#
    border_data = np.where(thres == 255)    # 取得白點的 x, y 座標
    Y_label = border_data[0]                # 1 維, 原始資料的資料標籤(答案)
    samples = Y_label.shape[0]              # 共有 samples 個資料
    X = border_data[1].reshape(samples, 1)  # 共有 samples 份的特徵 [[x1], [x2], [x3]…]
    regs = LinearRegression()               # 建立線性迴歸物件
    feature = PolynomialFeatures(degree=2)  # 建立 2 次多項式的特徵物件
    X_input = feature.fit_transform(X)      # 產生二次多項式特徵
    regs.fit(X_input, Y_label)              # 建立線性迴歸模型
#    print('二項式係數：', regs.coef_)        # 即 x2、x1
#    print('二項式截距：', regs.intercept_)   # 即 x0
    #----↓ 產生迴歸線預測值 ↓----#
    newX = np.array([i for i in range(width)])  # 製作新的 x 座標特徵
    newX = newX.reshape(newX.shape[0], 1)              # 做成一份一份
    newX_input = feature.fit_transform(newX)    # 新的二次項特徵
    newY = regs.predict(newX_input)             # 輸入新的輸入資料, 產生預測資料
    #----↓ 繪製資料點 ↓----#
#    plt.ylim(bottom=0, top=height)    # 限制 y 軸的範圍 (0～height)
#    plt.scatter(X, height - Y_label, color='blue', s=1)     # 繪製原始訓練資料點
#    plt.scatter(newX, height - newY, color='red', s=1)      # 繪製預測資料點
#    plt.show()
    #----↓ 製造曲線影像 ↓----#
    img_cuv = np.zeros_like(ori)    # 產生與原始黑白影像同尺寸的全黑影像
    newY = newY.round(0)            # 迴歸線的 y 座標, 去除小數位
    for point in np.column_stack([newY, newX]):
        py = int(point[0])   # y 座標位置
        px = int(point[1])   # x 座標位置
        w = 3               # 設定曲線寬度
        img_cuv[py-w:py+w, px] = 255   # slice
    #----↓ 去除曲線 ↓----#
    diff = cv2.absdiff(ori, img_cuv)   # 原始影像 - 迴歸線
    #----↓ 強力降噪 ↓----#
    denoise = cv2.fastNlMeansDenoising(diff, h = 80)  # 降躁
#    cv2.imshow('aa', denoise)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    return denoise

# 自動輸入車票資訊
def input_ticket_info(driver):
    driver.find_element_by_id('btn-confirm').click() #關閉個人資料使用訊息框
    driver.find_element_by_xpath('//select[@name="selectStartStation"]' +
                                 '//option[@value="2"]').click() # 起站：台北
    driver.find_element_by_xpath('//select[@name="selectDestinationStation"]' +
                                 '//option[@value="11"]').click() # 到站：台南
    driver.find_element_by_id('trainCon:trainRadioGroup_1').click()  #商務車廂
#    e = driver.find_element_by_id('toTimeInputField')   # 日期欄
#    e.clear()                  # 先清除內容
#    e.send_keys("2018/12/05")  # 輸入日期
    driver.find_element_by_xpath('//option[@value="430P"]').click() # 下午4點30
    driver.find_element_by_xpath('//option[@value="2F"]').click()   # 買 2 張票

# 自動輸入訂票人資訊
def input_train_and_person(driver):
    driver.find_element_by_name('SubmitButton').click()  #按【確認車次】鈕
    sleep(1)   # 等待換到下一頁
    driver.find_element_by_id('idNumber').send_keys('K122365XXX')    #輸入身分證字號
    driver.find_element_by_id('mobileInputRadio').click()  #選行動電話單選鈕
    driver.find_element_by_id('mobilePhone').send_keys('090854XXXX') #輸入行動電話
    driver.find_element_by_name('agree').click()  # 按下我已明確了解..高鐵約定事項
#    driver.find_element_by_id("isSubmit").click()  # 按下完成訂位按鈕