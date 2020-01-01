# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadTask.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from main import *
class cancelThread(QtCore.QThread):
    def __init__(self,a,gid):
        super(cancelThread,self).__init__()
        self.a = a
        self.gid = gid
    def run(self):
        status, gid = stopDownload(self.a, self.gid)
        # 维护前端队列
        print(item_list)
        for i in range(len(item_list)):
            if item_list[i].gid == self.gid:
                item_list[i].status = status  # 更新前端队列状态，不删除记录
                break
class Ui_task(QtWidgets.QWidget):
    def __init__(self,gid,item,out,mainwindow,status):
        super(QtWidgets.QWidget,self).__init__()
        self.gid = gid
        self.item = item
        self.mainwindow = mainwindow
        self.setupUi(self,status=status)
        self.filename.setText(out)
        self.StartPause.released.connect(self.onStartPause)
        self.Cancel.released.connect(self.onCancel)
        self.Delete.released.connect(self.onDelete)
    def onStartPause(self):
        a = self.mainwindow.aria
        gid = self.gid
        status = 0
        for item in item_list:
            if item.gid == gid:
                status = item.status
                break
        if status == 0:
            print("zgq: not found this gid in item_list")
            return
        if self.StartPause.text() == "Pause":  # 下载暂停
            self.StartPause.setText("Continue")
            status, gid = pauseDownload(a, gid)  # (a, gid)
            for item in item_list:
                if item.gid == gid:
                    # print(item)
                    item.status = status  # 更新前端队列status
                    break
        else:  # 下载继续
            self.StartPause.setText("Pause")
            print("onStartPauseReleased: ", a.taskStatus)
            status, gid = unpauseDownload(a, gid)  # (a, gid)
            for item in item_list:
                if item.gid == gid:
                    item.status = status  # 更新前端队列status
                    break
    def onCancel(self):
        a = self.mainwindow.aria

        gid = self.gid
        status = 0
        for item in item_list:
            if item.gid == gid:
                status = item.status
                break
        print("status is %s" % status)

        if status == 'complete':
            print("zgq: Already complete. Don't permit to pause!")
            return
        elif status == 0:
            print("zgq: not found this gid in item_list")

        X_dic[str(gid)].setEnabled(True)
        pause_dic[str(gid)].setEnabled(False)
        cancel_dic[str(gid)].setEnabled(False)
        # bar_dic[gid].update()
        print("cancelReleased called")

        statusDict = a.tellStatus(gid)
        status = statusDict["status"]
        # 证明要cancel的项目不在状态(downloading/paused)中，所以不能cancel
        if not (status == 'downloading' or status == 'paused'):
            return

        if status == "paused":
            a.updateLimitSpeed(gid, "1K")
            unpauseDownload(a, gid)
            time.sleep(0.5)
        self.cancel = cancelThread(a,gid)
        self.cancel.start()
        self.mainwindow.Update(gid, 0, "NaN")
        return
    def onDelete(self):
        a=self.mainwindow.aria
        gid = self.gid
        statusDict = a.tellStatus(gid)
        status = statusDict["status"]
        print("Task Status: " + status)
        if status == 'downloading' or status == 'paused':  # 正在下载，不能删除
            reply = QMessageBox.warning(self.hidden, 'Error', '请不要直接删除正在下载的任务！',
                                            QMessageBox.Yes, QMessageBox.Yes)
            return
        # stopped/completed 任务可以删除
        self.mainwindow.DownloadList.takeItem(self.mainwindow.DownloadList.row(self.item))
        # 维护前端队列
        del_idx = 0
        for i in range(len(item_list)):
            if item_list[i].gid == gid:
                del_idx = i
                break
        item_list.pop(del_idx)  # 删除item_list的第i项，delete的任务下标
        deleteDownload(a, gid)
        return

    def setupUi(self, task,status):
        task.setObjectName("task")
        task.resize(900, 70)
        task.setStyleSheet("QMenu::item:selected\n"
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
"")
        self.filename = QtWidgets.QLabel(task)
        self.filename.setGeometry(QtCore.QRect(10, 20, 281, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.filename.setFont(font)
        self.filename.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filename.setObjectName("filename")
        self.StartPause = QtWidgets.QPushButton(task)
        self.StartPause.setGeometry(QtCore.QRect(730, 15, 40, 40))
        self.StartPause.setStyleSheet("border-image: url(:/Breeze-Dark/pause.svg);")
        self.StartPause.setText("")
        self.StartPause.setObjectName("StartPause")
        if (status == 1) :
            self.StartPause.setText("Pause")
        else:
            self.StartPause.setText("Continue")
        pause_dic[str(self.gid)] = self.StartPause
        self.Cancel = QtWidgets.QPushButton(task)
        self.Cancel.setGeometry(QtCore.QRect(790, 15, 40, 40))
        self.Cancel.setStyleSheet("border-image: url(:/Breeze-Dark/stop.svg);")
        self.Cancel.setText("")
        self.Cancel.setObjectName("Cancel")
        cancel_dic[str(self.gid)] = self.Cancel
        self.Delete = QtWidgets.QPushButton(task)
        self.Delete.setGeometry(QtCore.QRect(850, 15, 40, 40))
        self.hidden = QtWidgets.QPushButton(task)
        self.hidden.setGeometry(QtCore.QRect(1500, 15, 1, 1))
        self.Delete.setStyleSheet("border-image: url(:/Breeze-Dark/trash.svg);")
        self.Delete.setText("")
        self.Delete.setObjectName("Delete")
        X_dic[str(self.gid)] = self.Delete
        self.progressBar = QtWidgets.QProgressBar(task)
        self.progressBar.setGeometry(QtCore.QRect(300, 20, 291, 30))
        self.progressBar.setStyleSheet("color: #FFFFFF")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        progress_dic[str(self.gid)] = self.progressBar
        self.speed = QtWidgets.QLabel(task)
        self.speed.setGeometry(QtCore.QRect(600, 20, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.speed.setFont(font)
        self.speed.setAutoFillBackground(False)
        self.speed.setStyleSheet("")
        self.speed.setObjectName("speed")
        spd_dic[str(self.gid)] =self.speed
        self.retranslateUi(task)
        QtCore.QMetaObject.connectSlotsByName(task)
        bar_dic[str(self.gid)] = self
    def retranslateUi(self, task):
        _translate = QtCore.QCoreApplication.translate
        task.setWindowTitle(_translate("task", "Form"))

import resources_rc
