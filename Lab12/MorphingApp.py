#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <11/23/2019>
#######################################################

# Import PyQt5 classes
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from MorphingGUI import *
from Morphing import *
import re
import imageio


class MorphingApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MorphingApp, self).__init__(parent)
        self.setupUi(self)

        self.leftPath = None
        self.rightPath = None
        self.leftImage = None
        self.rightImage = None
        self.alpha = 0.0

        self.btnBlend.setDisabled(True)
        self.chbShow.setDisabled(True)
        self.lineEdit_alpha.setDisabled(True)
        self.Slider.setDisabled(True)
        self.btnStart.clicked.connect(self.loadLeftData)
        self.btnEnding.clicked.connect(self.loadRightData)
        self.tbsStart.textChanged.connect(self.dataEntry)
        self.tbsEnding.textChanged.connect(self.dataEntry)
        self.btnBlend.clicked.connect(self.blend)

        self.Slider.setMinimum(0)
        self.Slider.setMaximum(20)
        self.Slider.setSingleStep(1)
        self.Slider.valueChanged.connect(self.slider_value_change)

    def loadLeftData(self):
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open image file ...', filter="Image files (*.png *.jpg)")
        if not filePath:
            return

        self.leftImage = imageio.imread(filePath)
        self.leftPath = filePath + ".txt"
        # print(self.leftImage)
        self.tbsStart.setText("test on left")

    def loadRightData(self):
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open image file ...',
                                                      filter="Image files (*.png *.jpg)")
        if not filePath:
            return

        self.rightImage = imageio.imread(filePath)
        self.rightPath = filePath + ".txt"
        # print(self.rightImage)
        self.tbsEnding.setText("test on right")

    def dataEntry(self):
        if self.leftPath and self.rightPath:
            print("enable everything")
            self.btnBlend.setDisabled(False)
            self.chbShow.setDisabled(False)
            self.lineEdit_alpha.setDisabled(False)
            self.Slider.setDisabled(False)
            self.lineEdit_alpha.setText("0.0")
            self.lineEdit_alpha.setReadOnly(True)

    def blend(self):
        leftTriangle, rightTriangle = loadTriangles(self.leftPath, self.rightPath)
        new_m = Morpher(self.leftImage, leftTriangle, self.rightImage, rightTriangle)
        result = new_m.getImageAtAlpha(self.alpha)
        imageio.imwrite('./result_' + str(self.alpha) + '.png', result)
        self.tbsResult.setText("finish morphing")

    def slider_value_change(self, value):
        self.alpha = value*0.05
        # self.lineEdit_alpha.setText("%.2f" % (value*0.05))
        self.lineEdit_alpha.setText(str(round(value * 0.05, 2)))


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MorphingApp()
    currentForm.show()
    sys.exit(currentApp.exec_())
