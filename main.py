import sys
import PyQt4.Qt
import math
from PyQt4 import uic, QtGui

app = QtGui.QApplication(sys.argv)
win = uic.loadUi("main.ui")
win.show()
sys.exit(app.exec_())
