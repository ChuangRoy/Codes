import ticket_module as m
import cv2
from selenium import webdriver
from time import sleep
import pytesseract
import re
#----↓ 開啟高鐵購票網站 ↓----#
url = 'https://irs.thsrc.com.tw/IMINT/?locale=tw'
option = webdriver.ChromeOptions()   # ←↓加入選項來指定不要有自動控制的訊息
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options = option)  #以指定的選項啟動 Chrome
driver.get(url)
m.input_ticket_info(driver) # 輸入購票資訊
is_success = False          # 用來判斷是否輸入驗證碼成功
#----↓ 嘗試破解驗證碼 20 次 ↓----#
for t in range(20):
    if is_success: # 判斷是否輸入驗證碼成功
        m.input_train_and_person(driver) # 輸入購票人資訊
        break     # 如果輸入驗證碼成功, 離開 t 迴圈
    print(f'----第{t+1}次----')
    #----↓ 操作網頁元素 ↓----#
    imgurl = driver.find_element_by_id(
             'BookingS1Form_homeCaptcha_passCode').get_attribute('src')
    renew_btn = driver.find_element_by_id \
        ('BookingS1Form_homeCaptcha_reCodeLink').click()    # 按下重新產生驗證碼按鈕
    imgurl2 = imgurl
    while(imgurl == imgurl2):   #等待驗證圖更換完成
        try:
            imgurl2 = driver.find_element_by_id(
                      'BookingS1Form_homeCaptcha_passCode').get_attribute('src')
        except:
            pass     # pass 表示不做事
        sleep(0.5)  # 暫停一下
    input_text = driver.find_element_by_name \
        ("homeCaptcha:securityCode")                # 驗證碼輸入欄位元素
    sub_btn = driver.find_element_by_id \
        ("SubmitButton")                            # 開始查詢按鈕元素
    captcha_tag = driver.find_element_by_id \
        ('BookingS1Form_homeCaptcha_passCode')      # 驗證碼圖片元素
    while(captcha_tag.size['width'] < 50 or         #等待圖檔載入完成
          captcha_tag.size['width'] > 180 ):
        pass    # pass 表示不做事
    captcha_tag.screenshot('captcha.png')           # 儲存驗證碼圖片
    #----↓ 驗證碼圖片的影像處理 ↓----#
    wrong = []    # 存放 ocr 辨識結果的 list (錯誤的驗證碼)
    img = cv2.imread('captcha.png')     # 讀取驗證碼圖片
    for b in range(2, 15):              # 使用範圍 2~15 的 border 寬度進行線性迴歸測試
        result_img = m.rm_regression(img, border=b)         # 取得去除迴歸線後的影像
        ocr_txt = pytesseract.image_to_string(result_img)   # 對影像進行 OCR 文字辨識
#        print('ocr結果', ocr_txt)
        key = re.sub(r'[^0-9^A-Z]*', '', ocr_txt.upper())   # 英文字轉大寫並將數字與英文取代成空字串
        if len(key) != 4:
            continue
        #----↓ OCR 有辨識結果 ↓----#
        key = re.sub(r'[0O]', 'Q', key)   #將 0 或 O 替換為 Q (因驗證碼中不會有0或O)
        if key not in wrong:  # 不要重複輸入錯的驗證碼
            print('輸入驗證碼：',key)
            driver.find_element_by_name \
                ('homeCaptcha:securityCode').send_keys(key)  # 輸入驗證碼
            driver.find_element_by_id \
                ('SubmitButton').click() # 按下查詢按鈕
            sleep(0.5)
            try:
                if driver.find_element_by_class_name \
                ('section_title').text != '':  # 如果有訂位明細元素
                    is_success = True
                    print('驗證成功')
                    break       # 驗證成功, 離開 b 迴圈
            except:
                print('驗證失敗')
                wrong.append(key) # 將錯的驗證碼存入清單
                input_text = driver.find_element_by_name \
                ('homeCaptcha:securityCode').clear() # 清空驗證碼欄位