""" Logiciel comptable de facturation, livre de recettes
; by weld, mit license
"""


# allow to use multiple directories
import sys
sys.path.insert(0, "./model/")
sys.path.insert(0, "./view/")
sys.path.insert(0, "./controller/")

import livre_recettes_UI as mainWindow

if __name__ == "__main__":
    mainWindow.init()