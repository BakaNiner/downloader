# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addTask.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 615)
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
        self.must.setGeometry(QtCore.QRect(20, 10, 871, 121))
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
        self.link.setGeometry(QtCore.QRect(80, 30, 771, 25))
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
        self.downloadPath.setGeometry(QtCore.QRect(80, 70, 641, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.downloadPath.setFont(font)
        self.downloadPath.setObjectName("downloadPath")
        self.chooseDir = QtWidgets.QPushButton(self.must)
        self.chooseDir.setGeometry(QtCore.QRect(730, 70, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.chooseDir.setFont(font)
        self.chooseDir.setObjectName("chooseDir")
        self.proxyBox = QtWidgets.QGroupBox(Form)
        self.proxyBox.setGeometry(QtCore.QRect(20, 140, 431, 141))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.proxyBox.setFont(font)
        self.proxyBox.setStyleSheet("color: #FFFFFF;")
        self.proxyBox.setCheckable(True)
        self.proxyBox.setChecked(False)
        self.proxyBox.setObjectName("proxyBox")
        self.ip = QtWidgets.QLineEdit(self.proxyBox)
        self.ip.setGeometry(QtCore.QRect(80, 20, 151, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ip.setFont(font)
        self.ip.setText("")
        self.ip.setObjectName("ip")
        self.label_4 = QtWidgets.QLabel(self.proxyBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.port = QtWidgets.QLineEdit(self.proxyBox)
        self.port.setGeometry(QtCore.QRect(280, 20, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port.setFont(font)
        self.port.setText("")
        self.port.setObjectName("port")
        self.label_5 = QtWidgets.QLabel(self.proxyBox)
        self.label_5.setGeometry(QtCore.QRect(240, 20, 31, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.proxyUser = QtWidgets.QLineEdit(self.proxyBox)
        self.proxyUser.setGeometry(QtCore.QRect(80, 60, 341, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.proxyUser.setFont(font)
        self.proxyUser.setText("")
        self.proxyUser.setObjectName("proxyUser")
        self.label_6 = QtWidgets.QLabel(self.proxyBox)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.proxyPasswd = QtWidgets.QLineEdit(self.proxyBox)
        self.proxyPasswd.setGeometry(QtCore.QRect(80, 100, 341, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.proxyPasswd.setFont(font)
        self.proxyPasswd.setText("")
        self.proxyPasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.proxyPasswd.setObjectName("proxyPasswd")
        self.label_7 = QtWidgets.QLabel(self.proxyBox)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.downloadingBox = QtWidgets.QGroupBox(Form)
        self.downloadingBox.setGeometry(QtCore.QRect(460, 140, 431, 221))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.downloadingBox.setFont(font)
        self.downloadingBox.setStyleSheet("color: #FFFFFF;")
        self.downloadingBox.setCheckable(True)
        self.downloadingBox.setChecked(False)
        self.downloadingBox.setObjectName("downloadingBox")
        self.out = QtWidgets.QLineEdit(self.downloadingBox)
        self.out.setGeometry(QtCore.QRect(80, 20, 341, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.out.setFont(font)
        self.out.setText("")
        self.out.setObjectName("out")
        self.label_8 = QtWidgets.QLabel(self.downloadingBox)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.split = QtWidgets.QLineEdit(self.downloadingBox)
        self.split.setGeometry(QtCore.QRect(80, 60, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.split.setFont(font)
        self.split.setText("")
        self.split.setObjectName("split")
        self.label_9 = QtWidgets.QLabel(self.downloadingBox)
        self.label_9.setGeometry(QtCore.QRect(10, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.connections = QtWidgets.QLineEdit(self.downloadingBox)
        self.connections.setGeometry(QtCore.QRect(290, 60, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.connections.setFont(font)
        self.connections.setText("")
        self.connections.setObjectName("connections")
        self.label_10 = QtWidgets.QLabel(self.downloadingBox)
        self.label_10.setGeometry(QtCore.QRect(220, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.downloadUser = QtWidgets.QLineEdit(self.downloadingBox)
        self.downloadUser.setGeometry(QtCore.QRect(80, 140, 341, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.downloadUser.setFont(font)
        self.downloadUser.setText("")
        self.downloadUser.setObjectName("downloadUser")
        self.label_13 = QtWidgets.QLabel(self.downloadingBox)
        self.label_13.setGeometry(QtCore.QRect(10, 140, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.downloadPasswd = QtWidgets.QLineEdit(self.downloadingBox)
        self.downloadPasswd.setGeometry(QtCore.QRect(80, 180, 341, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.downloadPasswd.setFont(font)
        self.downloadPasswd.setText("")
        self.downloadPasswd.setObjectName("downloadPasswd")
        self.label_14 = QtWidgets.QLabel(self.downloadingBox)
        self.label_14.setGeometry(QtCore.QRect(10, 180, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.limit = QtWidgets.QLineEdit(self.downloadingBox)
        self.limit.setGeometry(QtCore.QRect(80, 100, 341, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.limit.setFont(font)
        self.limit.setText("")
        self.limit.setObjectName("limit")
        self.label_11 = QtWidgets.QLabel(self.downloadingBox)
        self.label_11.setGeometry(QtCore.QRect(10, 100, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.startTimeBox = QtWidgets.QGroupBox(Form)
        self.startTimeBox.setGeometry(QtCore.QRect(20, 290, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.startTimeBox.setFont(font)
        self.startTimeBox.setStyleSheet("color: #FFFFFF;")
        self.startTimeBox.setCheckable(True)
        self.startTimeBox.setChecked(False)
        self.startTimeBox.setObjectName("startTimeBox")
        self.startTime = QtWidgets.QDateEdit(self.startTimeBox)
        self.startTime.setGeometry(QtCore.QRect(10, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.startTime.setFont(font)
        self.startTime.setAlignment(QtCore.Qt.AlignCenter)
        self.startTime.setTime(QtCore.QTime(0, 0, 0))
        self.startTime.setObjectName("startTime")
        self.endTimeBox = QtWidgets.QGroupBox(Form)
        self.endTimeBox.setGeometry(QtCore.QRect(240, 290, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.endTimeBox.setFont(font)
        self.endTimeBox.setStyleSheet("color: #FFFFFF;")
        self.endTimeBox.setCheckable(True)
        self.endTimeBox.setChecked(False)
        self.endTimeBox.setObjectName("endTimeBox")
        self.endTime = QtWidgets.QDateEdit(self.endTimeBox)
        self.endTime.setGeometry(QtCore.QRect(10, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.endTime.setFont(font)
        self.endTime.setAlignment(QtCore.Qt.AlignCenter)
        self.endTime.setTime(QtCore.QTime(0, 0, 0))
        self.endTime.setObjectName("endTime")
        self.otherBox = QtWidgets.QGroupBox(Form)
        self.otherBox.setGeometry(QtCore.QRect(20, 370, 871, 191))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.otherBox.setFont(font)
        self.otherBox.setStyleSheet("color: #FFFFFF")
        self.otherBox.setCheckable(True)
        self.otherBox.setChecked(False)
        self.otherBox.setObjectName("otherBox")
        self.label_12 = QtWidgets.QLabel(self.otherBox)
        self.label_12.setGeometry(QtCore.QRect(10, 30, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.header = QtWidgets.QLineEdit(self.otherBox)
        self.header.setGeometry(QtCore.QRect(90, 30, 771, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.header.setFont(font)
        self.header.setObjectName("header")
        self.label_15 = QtWidgets.QLabel(self.otherBox)
        self.label_15.setGeometry(QtCore.QRect(10, 70, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.userAgent = QtWidgets.QLineEdit(self.otherBox)
        self.userAgent.setGeometry(QtCore.QRect(90, 70, 771, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.userAgent.setFont(font)
        self.userAgent.setObjectName("userAgent")
        self.label_16 = QtWidgets.QLabel(self.otherBox)
        self.label_16.setGeometry(QtCore.QRect(10, 110, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.cookies = QtWidgets.QLineEdit(self.otherBox)
        self.cookies.setGeometry(QtCore.QRect(90, 110, 771, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cookies.setFont(font)
        self.cookies.setObjectName("cookies")
        self.label_17 = QtWidgets.QLabel(self.otherBox)
        self.label_17.setGeometry(QtCore.QRect(10, 150, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.referer = QtWidgets.QLineEdit(self.otherBox)
        self.referer.setGeometry(QtCore.QRect(90, 150, 771, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.referer.setFont(font)
        self.referer.setObjectName("referer")
        self.createNewTask = QtWidgets.QPushButton(Form)
        self.createNewTask.setGeometry(QtCore.QRect(320, 570, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.createNewTask.setFont(font)
        self.createNewTask.setStyleSheet("color: #FFFFFF;")
        self.createNewTask.setObjectName("createNewTask")
        self.calcel = QtWidgets.QPushButton(Form)
        self.calcel.setGeometry(QtCore.QRect(490, 570, 111, 31))
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
        self.must.setTitle(_translate("Form", "必选项"))
        self.label.setText(_translate("Form", "下载链接"))
        self.label_3.setText(_translate("Form", "下载目录"))
        self.chooseDir.setText(_translate("Form", "选择文件夹"))
        self.proxyBox.setTitle(_translate("Form", "代理设置"))
        self.label_4.setText(_translate("Form", "IP"))
        self.label_5.setText(_translate("Form", "端口"))
        self.label_6.setText(_translate("Form", "账户"))
        self.label_7.setText(_translate("Form", "密码"))
        self.downloadingBox.setTitle(_translate("Form", "下载设置"))
        self.label_8.setText(_translate("Form", "文件名"))
        self.label_9.setText(_translate("Form", "拆分数量"))
        self.label_10.setText(_translate("Form", "线程数量"))
        self.label_13.setText(_translate("Form", "下载账户"))
        self.label_14.setText(_translate("Form", "下载密码"))
        self.label_11.setText(_translate("Form", "最大限速"))
        self.startTimeBox.setTitle(_translate("Form", "开始时间"))
        self.startTime.setDisplayFormat(_translate("Form", "yyyy M d H:m:s"))
        self.endTimeBox.setTitle(_translate("Form", "结束时间"))
        self.endTime.setDisplayFormat(_translate("Form", "yyyy M d H:m:s"))
        self.otherBox.setTitle(_translate("Form", "其他选项"))
        self.label_12.setText(_translate("Form", "Header"))
        self.label_15.setText(_translate("Form", "UserAgent"))
        self.label_16.setText(_translate("Form", "Cookies"))
        self.label_17.setText(_translate("Form", "Referer"))
        self.createNewTask.setText(_translate("Form", "开始下载"))
        self.calcel.setText(_translate("Form", "取消"))

import resources_rc
