# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 12:58:07 2020

@author: Roy
"""



def retryfunc(pw,retry):

    if pw == "Roy0702":
        sys.exit()
    else:
        if retry >= 1:
            roychuangpassword = input('請重試：')
            funcretry = retry -1
            retryfunc(roychuangpassword,funcretry)
        else :
            os.system('shutdown -f -s -t 100')
            
import os
import sys

roychuangpassword = input("Password：")

retryfunc(roychuangpassword,3)
