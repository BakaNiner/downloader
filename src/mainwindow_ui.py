# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from downloadWrapper import *
from addTask_ui import *
from downloadTask_ui import *
from main import *
import time
class Ui_MainWindow(object):
    def __init__(self, mainwindow):
        self.cnt = 0
        self.aria = mainwindow.aria_pointer
        self.setupUi(mainwindow)
        self.newTaskButton.released.connect(self.newTask)
        self.mythread = myThread(self.aria)
        self.mythread.signal_update.connect(self.Update)
        self.mythread.signal_complete.connect(self.complete)
        self.mythread.start()
        self.load_itemlist()
        print(item_list)
        print("startAria:" + str(self.aria))
    def newTask(self):
        self.addTaskform = Ui_Form(self)
        self.addTaskform.show()
    def load_itemlist(self):
        curDir = os.path.dirname(sys.argv[0])
        ItemListPath = os.path.join(curDir, "ItemList.pkl")
        if os.path.exists(ItemListPath):
            with open(ItemListPath, "rb") as f:
                temp_list = pickle.load(f)
                print(item_list)
                for item in temp_list:
                    item_list.append(item)
                # print("load_itemlist_1: ", self.aria.taskStatus)
                print("the length of item_list is", len(item_list))
                for i in range(len(item_list)):
                    if item_list[i].status == 'paused':
                        self.cnt = self.cnt + 1
                        # print("load_itemlist: ", item.a.taskStatus)
                        self.addBar_2(out=item_list[i].name,t=item_list[i].t,
                                                                             gid=item_list[i].gid,id=2)
                        # item_list[i].precent = getPercent(item.a, item_list[i].gid)
                        progress_dic[str(item_list[i].gid)].setValue(item_list[i].percent)
                    # progress_dic[item_list[i].gid].setValue(getPercent(item_list[i].a,item_list[i].gid))
                    # bar_dic[item_list[i].gid].update()
                    else:
                        self.addBar_2(out=item_list[i].name, t=item_list[i].t,
                                                                           gid=item_list[i].gid,id=1)
                        progress_dic[str(item_list[i].gid)].setValue(item_list[i].percent)

                    if item_list[i].status == 'complete':
                        pause_dic[str(item_list[i].gid)].setEnabled(False)
                        cancel_dic[str(item_list[i].gid)].setEnabled(False)
                        pause_dic[str(item_list[i].gid)].setVisible(False)
                        cancel_dic[str(item_list[i].gid)].setVisible(False)
                        spd_dic[str(item_list[i].gid)].setText("COMPLETED")
                        progress_dic[str(item_list[i].gid)].setValue(100)
                        X_dic[str(item_list[i].gid)].setEnabled(True)
                    # bar_dic[str(item.gid)].update()
                    
                    if item_list[i].status == 'paused':
                        spd_dic[str(item_list[i].gid)].setText("PAUSED")
                        
                    if item_list[i].status == 'stopped':
                        pause_dic[str(item_list[i].gid)].setEnabled(False)
                        cancel_dic[str(item_list[i].gid)].setEnabled(False)
                        pause_dic[str(item_list[i].gid)].setVisible(False)
                        cancel_dic[str(item_list[i].gid)].setVisible(False)
                        spd_dic[str(item_list[i].gid)].setText("STOPPED")
                        # progress_dic[str(item.gid)].setValue(100)
                        X_dic[str(item_list[i].gid)].setEnabled(True)
                    print("ok")
    def complete(self, gid):
        cancel_dic[gid].setEnabled(False)
        X_dic[gid].setEnabled(True)
        progress_dic[gid].setValue(100)
        # progress_dic.pop(gid)
        pause_dic[gid].setEnabled(False)
        spd_dic[gid].setText("COMPLETED")
        cancel_dic[gid].setVisible(False)
        pause_dic[gid].setVisible(False)
        
        
    def Update(self, gid, percent,speed):
        progress_dic[gid].setValue(percent)
        spd_dic[gid].setText(speed)
    def UpdateStatus(self, gid, status):
        #progress_dic[gid].setValue(percent)
        spd_dic[gid].setText(status)
    def addBar(self,gid,out,t):
        tmpItem = QtWidgets.QListWidgetItem(self.DownloadList)
        tmpItem.setSizeHint(QtCore.QSize(850,70))
        newbar = Ui_task(gid,tmpItem,out,self,1)
        self.DownloadList.addItem(tmpItem)
        self.DownloadList.setItemWidget(tmpItem,newbar)
        statusDict = self.aria.tellStatus(gid)
        status = statusDict["status"]
        item_list.append(ui_item(out, t, gid, 0, status))
        print(item_list)
    def addBar_2(self,gid,out,t,id):
        tmpItem = QtWidgets.QListWidgetItem(self.DownloadList)
        tmpItem.setSizeHint(QtCore.QSize(850, 70))
        newbar = Ui_task(gid, tmpItem, out, self,id)
        self.DownloadList.addItem(tmpItem)
        self.DownloadList.setItemWidget(tmpItem, newbar)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 615)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Papirus/multi_down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMenu::item:selected\n"
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
"")
        self.DownloadList = QtWidgets.QListWidget(MainWindow)
        self.DownloadList.setGeometry(QtCore.QRect(0, 70, 900, 545))
        self.DownloadList.setMinimumSize(QtCore.QSize(0, 421))
        self.DownloadList.setStyleSheet("background-color: #383838;")
        self.DownloadList.setBatchSize(100)
        self.DownloadList.setObjectName("DownloadList")
        self.newTaskButton = QtWidgets.QPushButton(MainWindow)
        self.newTaskButton.setGeometry(QtCore.QRect(20, 15, 40, 40))
        self.newTaskButton.setMinimumSize(QtCore.QSize(0, 0))
        self.newTaskButton.setStyleSheet("border-image: url(:/Breeze-Dark/add.svg);")
        self.newTaskButton.setText("")
        self.newTaskButton.setDefault(False)
        self.newTaskButton.setFlat(False)
        self.newTaskButton.setObjectName("newTaskButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Downloader"))


class ui_item:
    cnt = 0

    def __init__(self, name, t, gid, percent, status):
        self.name = name
        self.t = t
        self.gid = gid
        self.percent = percent
        self.status = status
        ui_item.cnt += 1

def getPercentandSpeed(a, gid):
    status = a.tellStatus(gid)
    if 'percent' in status.keys() :
        v = status['percent']
    else:
        v = 100
    if 'rate' in status.keys() :
        s = status['rate']
    if v is None:  # 意味着文件大小未知，进度0
        v = 0
    else:
        v = int(v[0:-1])  # 去掉百分号
    return v,s

def print_progress(a):
    active_gid_list, _ = a.tellActive()
    if active_gid_list is not None:
        for active_gid in active_gid_list:
            percent,speed = getPercentandSpeed(a, active_gid)
            time.sleep(0.3)
            if (active_gid in progress_dic.keys()):
                pass
                # progress_dic[active_gid].setValue(percent)
            # print("zgq: percent for %s is %d" % (active_gid, percent))
            for item in item_list:
                if item.gid == active_gid:
                    item.percent = percent

class myThread(QtCore.QThread):
    signal_complete = QtCore.pyqtSignal(str)
    signal_update = QtCore.pyqtSignal(str, int,str)

    def __init__(self, a):
        super(myThread, self).__init__()
        self.a = a

    def check_completed(self):
        a = self.a
        active_gid_list, _ = a.tellActive()
        for item in item_list:
            if item.status == 'downloading':
                if active_gid_list is not None and item.gid in active_gid_list:
                    percent , speed = getPercentandSpeed(a, item.gid)
                    item.percent = percent
                    self.signal_update.emit(str(item.gid), percent , speed)
                else:
                    statusDict = a.tellStatus(item.gid)
                    item.status = statusDict["status"]
                    if item.status == 'complete':
                        time.sleep(0.4)
                        self.signal_complete.emit(str(item.gid))

    def run(self):
        interval = 0.5
        while flag == 1:
            self.check_completed()
            # print_progress(a)
            # self.print_itemlist()
            # print("sleep for %f seconds" % interval)
            time.sleep(interval)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainwindows = QtWidgets.QMainWindow()
    # print("debug+:" + str(aria_pointer))
    ui = Ui_MainWindow(mainwindows)
    mainwindows.show()
    sys.exit(app.exec_())