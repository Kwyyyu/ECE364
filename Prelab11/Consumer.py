
#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <11/9/2019>
#######################################################

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from BasicUI import *
from pprint import pprint as pp


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.btnSave.setDisabled(True)
        self.btnClear.clicked.connect(self.clearAll)
        for widget in QApplication.allWidgets():
            if widget.__class__ is QtWidgets.QLineEdit:
                widget.textChanged.connect(self.dataEntry)
        self.cboCollege.currentIndexChanged.connect(self.dataEntry)
        self.chkGraduate.stateChanged.connect(self.dataEntry)
        self.btnSave.clicked.connect(self.dataSave)

    def loadData(self):
        """
        *** DO NOT MODIFY THIS METHOD! ***
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        You must modify the method below.
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """
        pass

    def clearAll(self):
        for widget in QApplication.allWidgets():
            if widget.__class__ is QtWidgets.QLineEdit:
                widget.clear()
        self.chkGraduate.setChecked(False)
        self.cboCollege.setCurrentIndex(0)
        self.btnSave.setDisabled(True)
        self.btnLoad.setDisabled(False)

    def dataEntry(self):
        self.btnSave.setDisabled(False)
        self.btnLoad.setDisabled(True)

    def dataSave(self):
        grad = "false"
        if self.chkGraduate.isChecked is True:
            grad = "true"
        name_dic={}
        c_list = []
        for widget in QApplication.allWidgets():
            if widget.__class__ is QtWidgets.QLineEdit:
                name_dic[widget.objectName()] = widget.text()
        #pp(name_dic)
        for index in range(1, 20):
            c_name = "txtComponentName_" + str(index)
            c_count = "txtComponentCount_" + str(index)
            if name_dic[c_name]:
                c_list.append('<Component name="' + name_dic[c_name] + '" count="' + name_dic[c_count] + '" />')
        content = ""
        for record in c_list:
            content += "\t\t" + record + "\n"
        content = content[:len(content)-1]
        #pp(content)
        data = {'name': self.txtStudentName.text(), 'ID': self.txtStudentID.text(), "gradStatus": grad, "college": self.cboCollege.currentText(), "content": content}
        template = """<?xml version="1.0" encoding="UTF-8"?>
<Content>
    <StudentName graduate="%(gradStatus)s">%(name)s</StudentName>
    <StudentID>%(ID)s</StudentID>
    <College>%(college)s</College>
    <Components>
%(content)s
    </Components>
</Content>"""
        #print(template%data)
        with open("target.xml", "w") as f:
            f.write(template % data)












if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
