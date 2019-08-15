""" Accountancy software, leading to manage bills and user, for "auto-entrepreneurs"
; by weld, mit license
"""


# allow to use multiple directories
import sys
sys.path.insert(0, "./model/")
sys.path.insert(0, "./view/")
sys.path.insert(0, "./controller/")

import cashbook_UI as mainWindow

if __name__ == "__main__":
    mainWindow.init()