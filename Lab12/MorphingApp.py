#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <11/23/2019>
#######################################################

# Import PyQt5 classes
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QGraphicsScene, QGraphicsLineItem, QGraphicsEllipseItem
from MorphingGUI import *
from Morphing import *
import re
import imageio
import os

class MorphingApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MorphingApp, self).__init__(parent)
        self.setupUi(self)

        self.leftPath = None
        self.rightPath = None
        self.leftImage = None
        self.rightImage = None
        self.alpha = 0.0
        self.leftScene = QGraphicsScene()
        self.rightScene = QGraphicsScene()
        self.leftlines = []
        self.rightlines = []
        self.tempLeft = []
        self.leftFlag = 0
        self.tempRight = []
        self.rightFlag = 0
        self.tempPair = [[0, 0], [0, 0]]

        self.btnBlend.setDisabled(True)
        self.chbShow.setDisabled(True)
        self.lineEdit_alpha.setDisabled(True)
        self.Slider.setDisabled(True)
        self.btnStart.clicked.connect(self.loadLeftData)
        self.btnEnding.clicked.connect(self.loadRightData)
        self.btnBlend.clicked.connect(self.blend)
        self.gpvStart.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gpvStart.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gpvEnding.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gpvEnding.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gpvResult.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gpvResult.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Slider.setMinimum(0)
        self.Slider.setMaximum(20)
        self.Slider.setSingleStep(1)
        self.Slider.setPageStep(1)
        self.Slider.setTickPosition(2)
        self.Slider.valueChanged.connect(self.slider_value_change)
        self.chbShow.clicked.connect(self.showTriangles)
        self.gpvStart.mousePressEvent = self.selectLeftPoints
        self.gpvStart.keyPressEvent = self.deleteLeftPoints
        self.gpvEnding.mousePressEvent = self.selectRightPoints
        self.gpvEnding.keyPressEvent = self.deleteRightPoints
        self.mousePressEvent = self.setPersist

    def setPersist(self, event):
        if self.leftFlag == 1 and self.rightFlag == 1:
            x = event.x()
            y = event.y()
            if self.gpvEnding.x() <= x <= self.gpvEnding.x()+self.gpvEnding.width() and self.gpvEnding.y() <= y <= self.gpvEnding.y()+self.gpvEnding.height():
                pass
            else:
                self.leftFlag = 0
                self.rightFlag = 0
                pen = QPen(Qt.blue)
                brush = QBrush(Qt.blue)
                temp_item = self.tempLeft[len(self.tempLeft)-1]
                self.leftScene.removeItem(temp_item)
                temp_item.setPen(pen)
                temp_item.setBrush(brush)
                self.leftScene.addItem(temp_item)
                line_new = '\n%8.1f%8.1f' % (self.tempPair[0][0]*5, self.tempPair[0][1]*5)
                with open(self.leftPath, "a") as f:
                    f.write(line_new)
                temp_item = self.tempRight[len(self.tempRight) - 1]
                self.rightScene.removeItem(temp_item)
                temp_item.setPen(pen)
                temp_item.setBrush(brush)
                self.rightScene.addItem(temp_item)
                line_new = '\n%8.1f%8.1f' % (self.tempPair[1][0] * 5, self.tempPair[1][1] * 5)
                with open(self.rightPath, "a") as f:
                    f.write(line_new)
                if self.chbShow.isChecked():
                    self.removeTriangles()
                    self.addTriangles()

    def getPointList(self, filepath):
        with open(filepath, "r") as f:
            contents = f.readlines()

        point_list = []
        # get left and right point list
        for index in range(len(contents)):
            if contents[index] != "\n":
                xl, yl = contents[index].split()
                point_list.append([xl, yl])
        return point_list

    def addPoints(self, points, scene):
        brush = QBrush()
        pen = QPen()
        pen.setColor(Qt.red)
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(Qt.red)

        for point in points:
            x, y = point
            scene.addEllipse(float(x)/5 - 3, float(y)/5 - 3, 3.0, 3.0, pen, brush)
        return scene

    def addTriangles(self):
        leftTriangle, rightTriangle = loadTriangles(self.leftPath, self.rightPath)
        pen = QPen()
        if len(self.tempLeft) == 0:
            pen.setColor(Qt.red)
        else:
            pen.setColor(Qt.cyan)
        pen.setStyle(Qt.SolidLine)
        for l_tri, r_tri in zip(leftTriangle, rightTriangle):
            l = np.divide(l_tri.vertices, 5)
            r = np.divide(r_tri.vertices, 5)

            self.leftlines.append(QGraphicsLineItem(l[0][0], l[0][1], l[1][0], l[1][1]))
            self.leftlines.append(QGraphicsLineItem(l[0][0], l[0][1], l[2][0], l[2][1]))
            self.leftlines.append(QGraphicsLineItem(l[2][0], l[2][1], l[1][0], l[1][1]))

            self.rightlines.append(QGraphicsLineItem(r[0][0], r[0][1], r[1][0], r[1][1]))
            self.rightlines.append(QGraphicsLineItem(r[0][0], r[0][1], r[2][0], r[2][1]))
            self.rightlines.append(QGraphicsLineItem(r[2][0], r[2][1], r[1][0], r[1][1]))

        for lline,rline in zip(self.leftlines, self.rightlines):
            lline.setPen(pen)
            rline.setPen(pen)
            self.leftScene.addItem(lline)
            self.rightScene.addItem(rline)

    def removeTriangles(self):
        for line in self.leftlines:
            self.leftScene.removeItem(line)
            self.leftlines = []
        for line in self.rightlines:
            self.rightScene.removeItem(line)
            self.rightlines = []
        pass

    def showTriangles(self):
        if os.path.isfile(self.leftPath) and os.path.isfile(self.rightPath):
            if self.chbShow.isChecked():
                self.addTriangles()
            else:
                self.removeTriangles()

    def loadLeftData(self):
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open image file ...',
                                                  filter="Image files (*.png *.jpg)")
        if not filePath:
            return

        self.leftImage = imageio.imread(filePath)
        self.leftPath = filePath + ".txt"
        rect = QtCore.QRect(self.gpvStart.x(), self.gpvStart.y(), self.gpvStart.width(), self.gpvStart.height())
        self.leftScene.setSceneRect(0, 0, rect.width(), rect.height())
        image = QtGui.QPixmap(filePath).scaled(self.gpvStart.size()*0.995, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        self.leftScene.addPixmap(image)

        # get all the points for left image
        if os.path.isfile(self.leftPath):
            self.leftPoionts = self.getPointList(self.leftPath)
            self.leftScene = self.addPoints(self.leftPoionts, self.leftScene)

        self.gpvStart.setScene(self.leftScene)
        self.gpvResult.setScene(None)
        self.chbShow.setChecked(False)
        self.removeTriangles()

        if self.leftPath is not None and self.rightPath is not None:
            self.dataEntry()

    def loadRightData(self):
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open image file ...',
                                                      filter="Image files (*.png *.jpg)")
        if not filePath:
            return

        self.rightImage = imageio.imread(filePath)
        self.rightPath = filePath + ".txt"
        rect = QtCore.QRect(self.gpvEnding.x(), self.gpvEnding.y(), self.gpvEnding.width(), self.gpvEnding.height())
        self.rightScene.setSceneRect(0, 0, rect.width(), rect.height())
        image = QtGui.QPixmap(filePath).scaled(self.gpvEnding.size()*0.995, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        self.rightScene.addPixmap(image)

        # get all the points for right image
        if os.path.isfile(self.rightPath):
            self.rightPoionts = self.getPointList(self.rightPath)
            self.rightScene = self.addPoints(self.rightPoionts, self.rightScene)

        self.gpvEnding.setScene(self.rightScene)
        self.gpvResult.setScene(None)
        self.chbShow.setChecked(False)
        self.removeTriangles()
        if self.leftPath is not None and self.rightPath is not None:
            self.dataEntry()

    def selectLeftPoints(self, event):
        if self.leftFlag == 1 and self.rightFlag == 1:
            self.leftFlag = 0
            self.rightFlag = 0
            pen = QPen(Qt.blue)
            brush = QBrush(Qt.blue)
            temp_item = self.tempLeft[len(self.tempLeft)-1]
            self.leftScene.removeItem(temp_item)
            temp_item.setPen(pen)
            temp_item.setBrush(brush)
            self.leftScene.addItem(temp_item)
            line_new = '\n%8.1f%8.1f' % (self.tempPair[0][0]*5, self.tempPair[0][1]*5)
            with open(self.leftPath, "a") as f:
                f.write(line_new)
            temp_item = self.tempRight[len(self.tempRight) - 1]
            self.rightScene.removeItem(temp_item)
            temp_item.setPen(pen)
            temp_item.setBrush(brush)
            self.rightScene.addItem(temp_item)
            line_new = '\n%8.1f%8.1f' % (self.tempPair[1][0] * 5, self.tempPair[1][1] * 5)
            with open(self.rightPath, "a") as f:
                f.write(line_new)
            if self.chbShow.isChecked():
                self.removeTriangles()
                self.addTriangles()

        if (not os.path.isfile(self.leftPath)) and (not os.path.isfile(self.rightPath)):
            with open(self.leftPath, "w"): pass
            with open(self.rightPath, "w"): pass
        pen = QPen(Qt.green)
        brush = QBrush(Qt.green)

        if self.leftFlag == 0:
            x = event.x()
            y = event.y()
            temp_item = QGraphicsEllipseItem(x - 3, y - 3, 3, 3)
            temp_item.setPen(pen)
            temp_item.setBrush(brush)
            self.tempLeft.append(temp_item)
            self.leftScene.addItem(temp_item)
            self.leftFlag = 1
            self.tempPair[0] = [x, y]

    def deleteLeftPoints(self, event):
        if event.key() == Qt.Key_Backspace and self.leftFlag == 1:
            temp_item = self.tempLeft.pop()
            self.leftScene.removeItem(temp_item)
            self.leftFlag = 0

    def selectRightPoints(self, event):
        if (not os.path.isfile(self.leftPath)) and (not os.path.isfile(self.rightPath)):
            with open(self.leftPath, "w"): pass
            with open(self.rightPath, "w"): pass
        pen = QPen(Qt.green)
        brush = QBrush(Qt.green)

        if self.rightFlag == 0:
            x = event.x()
            y = event.y()
            temp_item = QGraphicsEllipseItem(x - 3, y - 3, 3, 3)
            temp_item.setPen(pen)
            temp_item.setBrush(brush)
            self.tempRight.append(temp_item)
            self.rightScene.addItem(temp_item)
            self.rightFlag = 1
            self.tempPair[1] = [x, y]

    def deleteRightPoints(self, event):
        if event.key() == Qt.Key_Backspace and self.rightFlag == 1:
            temp_item = self.tempRight.pop()
            self.rightScene.removeItem(temp_item)
            self.rightFlag = 0


    def dataEntry(self):
        if self.leftPath and self.rightPath:
            self.btnBlend.setDisabled(False)
            self.chbShow.setDisabled(False)
            self.lineEdit_alpha.setDisabled(False)
            self.Slider.setDisabled(False)
            self.lineEdit_alpha.setText("0.0")
            self.lineEdit_alpha.setReadOnly(True)
            self.Slider.setValue(0)

    def blend(self):
        leftTriangle, rightTriangle = loadTriangles(self.leftPath, self.rightPath)
        new_m = Morpher(self.leftImage, leftTriangle, self.rightImage, rightTriangle)
        result = new_m.getImageAtAlpha(self.alpha)
        path = './result_' + str(round(self.alpha, 2)) + '.png'
        imageio.imwrite(path, result)
        image = QtGui.QPixmap(path).scaled(self.gpvResult.size())
        scene = QGraphicsScene()
        scene.addPixmap(image)

        self.gpvResult.setScene(scene)

    def slider_value_change(self, value):
        self.alpha = value*0.05
        self.lineEdit_alpha.setText(str(round(value * 0.05, 2)))


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MorphingApp()
    currentForm.show()
    sys.exit(currentApp.exec_())
