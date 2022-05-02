import pyautogui
# from PIL import Image
import cv2
import os
import sys

TEMP_PATH = os.environ['temp'] # get temp directory path
myScreenshot = pyautogui.screenshot() #screenshot
myScreenshot.save(TEMP_PATH + r'\temp.png') # save file to %temp%

img1 = cv2.imread(TEMP_PATH + r'\temp.png') # read screenshot
cv2.imshow("Screenshot" , img1) # show image
cv2.waitKey(0) # wait key press
cv2.destroyAllWindows() # close imageshow window
os.remove(TEMP_PATH + r'\temp.png')
