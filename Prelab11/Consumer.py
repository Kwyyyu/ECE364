
#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <11/9/2019>
#######################################################

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from BasicUI import *
import re


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
        self.btnLoad.clicked.connect(self.loadData)

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
        with open(filePath, "r") as f:
            contents = f.read().replace("\n", "")

        p_name = r'<StudentName graduate="(?P<graduate>[\w]+)">(?P<name>[\w\W]+)</StudentName>'
        match = re.search(p_name, contents)
        self.txtStudentName.setText(match["name"])
        if match["graduate"] == "true":
            self.chkGraduate.setChecked(True)
        else:
            self.chkGraduate.setChecked(False)
        p_ID = r'<StudentID>(?P<ID>[\w\W]+)</StudentID>'
        match = re.search(p_ID, contents)
        self.txtStudentID.setText(match["ID"])
        p_college = r'<College>(?P<college>[\w ]+)</College>'
        match = re.search(p_college, contents)
        self.cboCollege.setCurrentText(match["college"])
        p_comp = r'<Component name="(?P<comp_name>[^"]+)" count="(?P<comp_count>[\d]+)" />'
        match = re.findall(p_comp, contents)
        length = 20
        if len(match) < 20:
            length = len(match)
        for index in range(length):
            c_name = "txtComponentName_" + str(index+1)
            c_count = "txtComponentCount_" + str(index+1)
            for widget in QApplication.allWidgets():
                if widget.objectName() == c_name:
                    widget.setText(match[index][0])
                elif widget.objectName() == c_count:
                    widget.setText(match[index][1])
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
        if self.chkGraduate.isChecked() is True:
            grad = "true"
        name_dic = {}
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
        with open("target.xml", "w") as f:
            f.write(template % data)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
