import cv2

img = cv2.imread('RPHF.png')   # 讀取 RPHF.png (已附於程式碼目錄)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 影像轉灰階
denoise=cv2.fastNlMeansDenoising(gray, h=50)    # 去除 Noise
gaus = cv2.GaussianBlur(gray, (5, 5), 0)        # 高斯模糊
ret, thresh = cv2.threshold(denoise, 127, 255,  #　門檻值轉黑白影像
                            cv2.THRESH_BINARY_INV)   
cv2.imshow('1', img)                            
cv2.imshow('2', gaus)                           
cv2.imshow('3', denoise)
cv2.imshow('4', thresh)                        
cv2.waitKey(0)
cv2.destroyAllWindows()