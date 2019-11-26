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
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QGraphicsScene, QGraphicsLineItem
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
        self.leftScene = QGraphicsScene()
        self.rightScene = QGraphicsScene()
        self.lines = []

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
        self.Slider.valueChanged.connect(self.slider_value_change)
        self.chbShow.clicked.connect(self.addTriangles)

    def getPointList(self, filepath):
        with open(filepath, "r") as f:
            contents = f.readlines()

        point_list = []
        # get left and right point list
        for index in range(len(contents)):
            xl, yl = contents[index].split()
            point_list.append([xl, yl])
        return point_list

    def addPoints(self, points, scene):
        brush = QBrush()
        pen = QPen()
        pen.setColor(Qt.red)
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(Qt.red)
        # print(points)

        for point in points:
            x, y = point
            # print(x, y)
            scene.addEllipse(float(x)/5 - 3, float(y)/5 - 3, 3.0, 3.0, pen, brush)
        return scene

    def addTriangles(self):
        leftTriangle, rightTriangle = loadTriangles(self.leftPath, self.rightPath)
        for l_tri, r_tri in zip(leftTriangle, rightTriangle):
            l = np.divide(l_tri.vertices, 5)
            r = np.divide(r_tri.vertices, 5)
            # print(l[0])
            # print(r)
            pen = QPen()
            pen.setColor(Qt.red)
            pen.setStyle(Qt.SolidLine)

            self.lines.append(QGraphicsLineItem(l[0][0], l[0][1], l[1][0], l[1][1], pen))
            
            # self.leftScene.addLine(l[0][0], l[0][1], l[2][0], l[2][1], pen)
            # self.leftScene.addLine(l[2][0], l[2][1], l[1][0], l[1][1], pen)
            #
            # self.rightScene.addLine(r[0][0], r[0][1], r[1][0], r[1][1], pen)
            # self.rightScene.addLine(r[0][0], r[0][1], r[2][0], r[2][1], pen)
            # self.rightScene.addLine(r[2][0], r[2][1], r[1][0], r[1][1], pen)

    def loadLeftData(self):
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open image file ...',
                                                  filter="Image files (*.png *.jpg)")
        if not filePath:
            return

        self.leftImage = imageio.imread(filePath)
        self.leftPath = filePath + ".txt"
        rect = QtCore.QRect(self.gpvStart.x(), self.gpvStart.y(), self.gpvStart.width(), self.gpvStart.height())
        self.leftScene.setSceneRect(0,0, rect.width(), rect.height())
        image = QtGui.QPixmap(filePath).scaled(self.gpvStart.size()*0.995, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        self.leftScene.addPixmap(image)

        # get all the points for left image
        self.leftPoionts = self.getPointList(self.leftPath)
        self.leftScene = self.addPoints(self.leftPoionts, self.leftScene)

        self.gpvStart.setScene(self.leftScene)
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
        self.rightPoionts = self.getPointList(self.rightPath)
        self.rightScene = self.addPoints(self.rightPoionts, self.rightScene)

        self.gpvEnding.setScene(self.rightScene)
        if self.leftPath is not None and self.rightPath is not None:
            self.dataEntry()

    def dataEntry(self):
        if self.leftPath and self.rightPath:
            print("enable everything")
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
        # self.lineEdit_alpha.setText("%.2f" % (value*0.05))
        self.lineEdit_alpha.setText(str(round(value * 0.05, 2)))


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MorphingApp()
    currentForm.show()
    sys.exit(currentApp.exec_())
