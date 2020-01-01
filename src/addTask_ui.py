# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addTask_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from downloadWrapper import *
class Ui_Form(QtWidgets.QWidget):
    def __init__(self,mainwindow):
        super(QtWidgets.QWidget,self).__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.createNewTask.released.connect(self.addTask)
        self.calcel.released.connect(self.cancel)
    def addTask(self):
        url = self.link.text()
        path = self.downloadPath.text()
        limit = self.limit.text()
        split = self.split.text()
        out = self.out.text()
        threads = self.connections.text()
        if self.link.text() == '':
            reply = QMessageBox.information(self.createNewTask, 'Error', '请输入正确的下载链接', QMessageBox.Yes, QMessageBox.Yes)
            return
        ##以上，传参
        ##以下，尝试创建新的任务
        t, gid, success = startDownload(self.mainwindow.aria, url, split, out) #没传path和limit！
        if  success == 2 :
            reply = QMessageBox.information(self.createNewTask, 'Error', '已有同名文件！', QMessageBox.Yes, QMessageBox.Yes)
            return
        if success == 0:
            reply = QMessageBox.information(self.createNewTask, 'Error', '开始任务失败，请检查下载设置并重新尝试！',
                                                QMessageBox.Yes, QMessageBox.Yes)
            return
        if success == 1 :
            self.mainwindow.addBar(gid,out,t)
            self.close()
    def cancel(self):
        self.close()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(829, 202)
        Form.setStyleSheet("QMenu::item:selected\n"
"{ \n"
"    background-color : #008098;\n"
"    color : white\n"
"}\n"
"\n"
"QToolTip\n"
"{ \n"
"    color: white; \n"
"    background-color: #383838;\n"
"    border: 1px solid white;\n"
"} \n"
"\n"
"QTabWidget::pane\n"
"{\n"
"    background: #383838;\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-style: none;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-bottom: 2px solid #008098;\n"
"    padding-bottom: 5px;\n"
"    font-weight: bold;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    font-weight: normal;\n"
"    margin-bottom: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    border-bottom: 1px solid #008098;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow\n"
"{\n"
"    image: url(:/dark fusion/right_arrow.svg);\n"
"    background: #383838;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow\n"
"{\n"
"    image: url(:/dark fusion/left_arrow.svg);\n"
"    background: #383838;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled\n"
"{\n"
"    image: url(:/dark fusion/right_arrow_disabled.svg);\n"
"    background: #383838;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled\n"
"{\n"
"    image: url(:/dark fusion/left_arrow_disabled.svg);\n"
"    background: #383838;\n"
"}\n"
"\n"
"QPushButton, QComboBox\n"
"{\n"
"    background: #383838;\n"
"    border-radius: 2px;\n"
"    padding: 4px 6px;\n"
"} \n"
"\n"
"QPushButton:enabled, QComboBox:enabled\n"
"{\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:hover, QComboBox:hover\n"
"{\n"
"    border: 1px solid #008098;\n"
"}\n"
"QComboBox\n"
"{\n"
"    background: #2b2b2b;\n"
"    selection-background-color: #008098;\n"
"}\n"
"QComboBox:focus {\n"
"    border: 1px solid #008098;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: gray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow\n"
"{\n"
"\n"
"    border-image: url(:/dark fusion/down_arrow_disabled.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"\n"
"QSpinBox:enabled,\n"
"QDoubleSpinBox:enabled,\n"
"QLineEdit:enabled,\n"
"QDateTimeEdit:enabled\n"
"{\n"
"    border: 1px solid gray;\n"
"    padding-right: 1.5ex;\n"
"    background: #2b2b2b;\n"
"}\n"
"\n"
"QSpinBox::hover,\n"
"QDoubleSpinBox::hover,\n"
"QDateTimeEdit::hover\n"
"{\n"
"    border: 1px solid #008098;\n"
"\n"
"}\n"
"\n"
"QDateTimeEdit::up-button,\n"
"QSpinBox::up-button,\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: right top;\n"
"\n"
"    width: 1.6ex;\n"
"    border-width: 0.1ex;\n"
"}\n"
"\n"
"QDateTimeEdit::up-arrow,\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow\n"
"{\n"
"    border-image: url(:/dark fusion/up_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QDateTimeEdit::up-arrow::hover,\n"
"QDateTimeEdit::up-arrow:pressed,\n"
"QSpinBox::up-arrow:hover,\n"
"QSpinBox::up-arrow:pressed,\n"
"QDoubleSpinBox::up-arrow:hover,\n"
"QDoubleSpinBox::up-arrow:pressed\n"
"{\n"
"    border-image: url(:/dark fusion/up_arrow_hover.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QDateTimeEdit::up-arrow:disabled,\n"
"QDateTimeEdit::up-arrow:off,\n"
"QSpinBox::up-arrow:disabled,\n"
"QSpinBox::up-arrow:off,\n"
"QDoubleSpinBox::up-arrow:disabled,\n"
"QDoubleSpinBox::up-arrow:off\n"
"{\n"
"   border-image: url(:/dark fusion/up_arrow_disabled.svg);\n"
"}\n"
"\n"
"QDateTimeEdit::down-button,\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: right bottom;\n"
"\n"
"    width: 1.6ex;\n"
"    border-width: 0.1ex;\n"
"}\n"
"\n"
"QDateTimeEdit::down-arrow,\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"    border-image: url(:/dark fusion/down_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QDateTimeEdit::down-arrow:hover,\n"
"QDateTimeEdit::down-arrow:pressed,\n"
"QSpinBox::down-arrow:hover,\n"
"QSpinBox::down-arrow:pressed,\n"
"QDoubleSpinBox::down-arrow:hover,\n"
"QDoubleSpinBox::down-arrow:pressed\n"
"{\n"
"    border-image: url(:/dark fusion/down_arrow_hover.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QDateTimeEdit::down-arrow:disabled,\n"
"QSpinBox::down-arrow:disabled,\n"
"QSpinBox::down-arrow:off,\n"
"QDoubleSpinBox::down-arrow:disabled,\n"
"QDoubleSpinBox::down-arrow:off\n"
"{\n"
"   border-image: url(:/dark fusion/down_arrow_disabled.svg);\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    margin: 0.3ex;\n"
"    padding: 0.5ex;\n"
"}\n"
"\n"
"QToolButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 0.1ex solid #008098;\n"
"    border-radius: 0.2ex;\n"
"    margin: 0.3ex;\n"
"    padding: 0.5ex;\n"
"}\n"
"\n"
"QToolBar\n"
"{\n"
"    border: 0.1ex transparent #393838;\n"
"    background: 0.1ex solid #383838;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QToolBar::separator:horizontal\n"
"{\n"
"    background: gray; \n"
"    width: 1px;\n"
"    height: 5ex;\n"
"}\n"
"\n"
"QTableView, QTreeView\n"
"{\n"
"    border: 0.1ex solid gray;\n"
"    gridline-color: #31363b;\n"
"    background-color: #2b2b2b;\n"
"}\n"
"\n"
"QTableView:hover,\n"
"QTreeView:hover,\n"
"QLineEdit:hover\n"
"{\n"
"    border: 1px solid #008098;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    background-color: #383838;\n"
"    border: 0.1ex transparent;\n"
"    border-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #383838;\n"
"    color: #eff0f1;\n"
"    border: 0.1ex solid gray;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 0.5ex;\n"
"    outline: none;\n"
"    color: #eff0f1;\n"
"    margin-bottom: 0.2ex;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #76797c;\n"
"}\n"
"\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 0.2ex;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:focus\n"
"{\n"
"    border-image: url(:/dark fusion/checkbox_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"    border: none;\n"
"    border-image: url(:/dark fusion/checkbox_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    border-image: url(:/dark fusion/checkbox_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover,\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"    border: none;\n"
"    border-image: url(:/dark fusion/checkbox_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate\n"
"{\n"
"    border-image: url(:/dark fusion/checkbox_indeterminate.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"{\n"
"    border-image: url(:/dark fusion/checkbox_indeterminate.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled\n"
"{\n"
"    border-image: url(:/dark fusion/checkbox_indeterminate_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    border-image: url(:/dark fusion/checkbox_checked_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    border-image: url(:/dark fusion/checkbox_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    background-color: #2b2b2b;\n"
"    border: 1px solid gray;\n"
"    border-radius: 0.3ex;\n"
"    height: 2px;\n"
"    text-align: center;\n"
"    margin-top: 1ex;\n"
"    margin-bottom: 1ex;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #008098;\n"
"    border: 0px transparent;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    background-color: #383838;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"")
        self.must = QtWidgets.QGroupBox(Form)
        self.must.setGeometry(QtCore.QRect(20, 10, 781, 181))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.must.setFont(font)
        self.must.setStyleSheet("color: #FFFFFF")
        self.must.setObjectName("must")
        self.label = QtWidgets.QLabel(self.must)
        self.label.setGeometry(QtCore.QRect(10, 30, 65, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.link = QtWidgets.QLineEdit(self.must)
        self.link.setGeometry(QtCore.QRect(80, 30, 681, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.link.setFont(font)
        self.link.setObjectName("link")
        self.label_3 = QtWidgets.QLabel(self.must)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 65, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.downloadPath = QtWidgets.QLineEdit(self.must)
        self.downloadPath.setGeometry(QtCore.QRect(80, 70, 541, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.downloadPath.setFont(font)
        self.downloadPath.setObjectName("downloadPath")
        self.chooseDir = QtWidgets.QPushButton(self.must)
        self.chooseDir.setGeometry(QtCore.QRect(640, 70, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.chooseDir.setFont(font)
        self.chooseDir.setObjectName("chooseDir")
        self.label_12 = QtWidgets.QLabel(self.must)
        self.label_12.setGeometry(QtCore.QRect(10, 110, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.out = QtWidgets.QLineEdit(self.must)
        self.out.setGeometry(QtCore.QRect(80, 110, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.out.setFont(font)
        self.out.setText("")
        self.out.setObjectName("out")
        self.label_9 = QtWidgets.QLabel(self.must)
        self.label_9.setGeometry(QtCore.QRect(260, 110, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.split = QtWidgets.QLineEdit(self.must)
        self.split.setGeometry(QtCore.QRect(370, 110, 251, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.split.setFont(font)
        self.split.setText("")
        self.split.setObjectName("split")
        self.label_10 = QtWidgets.QLabel(self.must)
        self.label_10.setGeometry(QtCore.QRect(10, 150, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.connections = QtWidgets.QLineEdit(self.must)
        self.connections.setGeometry(QtCore.QRect(80, 150, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.connections.setFont(font)
        self.connections.setText("")
        self.connections.setObjectName("connections")
        self.label_11 = QtWidgets.QLabel(self.must)
        self.label_11.setGeometry(QtCore.QRect(260, 150, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.limit = QtWidgets.QLineEdit(self.must)
        self.limit.setGeometry(QtCore.QRect(370, 150, 251, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.limit.setFont(font)
        self.limit.setText("")
        self.limit.setObjectName("limit")
        self.createNewTask = QtWidgets.QPushButton(self.must)
        self.createNewTask.setGeometry(QtCore.QRect(650, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.createNewTask.setFont(font)
        self.createNewTask.setStyleSheet("color: #FFFFFF;")
        self.createNewTask.setObjectName("createNewTask")
        self.calcel = QtWidgets.QPushButton(self.must)
        self.calcel.setGeometry(QtCore.QRect(650, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calcel.setFont(font)
        self.calcel.setStyleSheet("color: #FFFFFF;")
        self.calcel.setObjectName("calcel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "新建下载任务"))
        self.must.setTitle(_translate("Form", "下载选项"))
        self.label.setText(_translate("Form", "下载链接"))
        self.label_3.setText(_translate("Form", "下载目录"))
        self.chooseDir.setText(_translate("Form", "选择文件夹"))
        self.label_12.setText(_translate("Form", "文件名称"))
        self.label_9.setText(_translate("Form", "拆分数量"))
        self.label_10.setText(_translate("Form", "线程数量"))
        self.label_11.setText(_translate("Form", "最大限速"))
        self.createNewTask.setText(_translate("Form", "开始下载"))
        self.calcel.setText(_translate("Form", "取消"))

import resources_rc
