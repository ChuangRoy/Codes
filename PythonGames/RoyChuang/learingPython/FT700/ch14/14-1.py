import pytesseract
import cv2

img = cv2.imread('1A2B.png')
ocr_txt = pytesseract.image_to_string(img)
print('OCR 辨識結果:', ocr_txt)
cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()