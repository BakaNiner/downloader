from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from download import *
from main import *
import time


class ui_item:
    cnt = 0

    def __init__(self, url, mode, gid, a, t, percent, status, path="C:/Users/Chen/Desktop/Download"):
        self.url = url
        self.mode = mode
        self.path = path
        self.gid = gid
        self.a = a
        self.t = t
        self.percent = percent
        self.status = status
        ui_item.cnt += 1




def getPercent(a, gid):
    v = 0
    _, statusList = a.tellActive()
    for s in statusList:
        if s['gid'] == gid:
            v = s['percent']
            if v == None:  # v = None 意味着下载还没开始，进度0
                v = 0
            else:
                v = int(v[0:-1])  # 去掉百分号
    return v


def print_progress(a):
    active_gid_list, _ = a.tellActive()
    if active_gid_list is not None:
        for active_gid in active_gid_list:
            percent = getPercent(a, active_gid)
            time.sleep(0.3)
            if (active_gid in progress_dic.keys()):
                pass
                #progress_dic[active_gid].setValue(percent)
            print("zgq: percent for %s is %d" % (active_gid, percent))
            for item in item_list:
                if item.gid == active_gid:
                    item.percent = percent


class myThread(QtCore.QThread) :
    signal_complete = QtCore.pyqtSignal(str)
    signal_update = QtCore.pyqtSignal(str, int)
    def __init__(self,a):
        super(myThread,self).__init__()
        self.a = a
    def check_completed(self):
        a = self.a
        # _, statusList = a.tellActive()
        active_gid_list, _ = a.tellActive()
        for item in item_list:
            if item.status == 'downloading':
                active = 0
                if active_gid_list is not None:
                    for active_gid in active_gid_list:
                        if active_gid == item.gid:
                            active = 1
                            break
                if active == 1 :
                    percent = getPercent(a, item.gid)
                    item.percent = percent
                    self.signal_update.emit(str(item.gid), percent)
                #   if (percent < 95) : #在接近下载完成的时候getpercent可能无法正常返回值！
                #       progress_dic[item.gid].setValue(percent)
                if active == 0 and item.status != 'stopped':
                    item.status = 'complete'
                    item.modify = 0
            if item.status == 'complete' and item.modify == 0:
                time.sleep(0.4)
                self.signal_complete.emit(str(item.gid))
                item.modify = 1
    def run(self):
        iter = 0
        interval = 0.5
        maxiter = 500
        while flag == 1 and iter < maxiter:
            self.check_completed()
            # print_progress(a)
           # self.print_itemlist()
            iter = iter + 1

            # print("sleep for %f seconds" % interval)
            time.sleep(interval)

class Ui_MainWindow(object):
    def __init__(self, mainwindow):
        #self.item_list = []
        self.cnt = 0
        self.aria = mainwindow.aria_pointer
        self.setupUi(mainwindow)
        self.begin.clicked.connect(self.Begin)
        self.mythread = myThread(self.aria)
        self.mythread.signal_update.connect(self.Update)
        self.mythread.signal_complete.connect(self.complete)
        self.load_itemlist()
        self.mythread.start()
       # self.mythread.start()
        print("startAria:"+ str(self.aria))

    def complete(self,gid):
        cancel_dic[gid].setEnabled(False)
        X_dic[gid].setEnabled(True)
        progress_dic[gid].setValue(100)
        progress_dic.pop(gid)
        pause_dic[gid].setEnabled(False)
        bar_dic[gid].repaint()

    def Update(self,gid,percent):
        progress_dic[str(gid)].setValue(percent)
        bar_dic[str(gid)].repaint()

    def load_itemlist(self):
        curDir = os.path.dirname(sys.argv[0])
        ItemListPath = os.path.join(curDir, "ItemList.pkl")
        if os.path.exists(ItemListPath):            
            with open(ItemListPath, "rb") as f:
                temp_list = pickle.load(f)
                for item in temp_list:
                    item.a = self.aria
                    item_list.append(item)
                #print("load_itemlist_1: ", self.aria.taskStatus)
                print("the length of item_list is", len(item_list))
                for i in range(len(item_list)):
                    if item_list[i].status == 'paused':
                        self.cnt = self.cnt + 1
                        #print("load_itemlist: ", item.a.taskStatus)
                        success, downloaditem, item_1 = self.myDownloadBar_2(item_list[i].url, item_list[i].mode, item_list[i].a, item_list[i].t, item_list[i].gid, success=1, append=0)
                        item_list[i].precent = getPercent(item.a, item_list[i].gid)
                        progress_dic[str(item_list[i].gid)].setValue(item_list[i].percent)
                        #progress_dic[item_list[i].gid].setValue(getPercent(item_list[i].a,item_list[i].gid))
                        #bar_dic[item_list[i].gid].update()
                    else:
                        success, downloaditem, item_1 = self.myDownloadBar(item_list[i].url, item_list[i].mode, item_list[i].a, item_list[i].t, item_list[i].gid, success=1, append=0)
                        progress_dic[str(item_list[i].gid)].setValue(item_list[i].percent)

                    if item_list[i].status == 'complete' :
                        pause_dic[str(item.gid)].setEnabled(False)
                        cancel_dic[str(item.gid)].setEnabled(False)
                        progress_dic[str(item.gid)].setValue(100)
                        X_dic[str(item.gid)].setEnabled(True)
                        #bar_dic[str(item.gid)].update()
                    if success == 0:
                        return
                    
                    print("ok")
                    self.DownloadList.addItem(item_1)
                    self.DownloadList.setItemWidget(item_1, downloaditem)
                    downloaditem.show()
        if (self.cnt > 0) :
            self.mythread.start()
        
                
    # 开始下载的代码，这是按下主界面的下载键后会调用的代码
    def Begin(self):
        if self.urlLine.text() == '':
            reply = QMessageBox.information(self.begin, 'Error', '请输入正确的下载链接', QMessageBox.Yes, QMessageBox.Yes)
            return
        else:
            url = self.urlLine.text()
        #    if self.BitTorrent.isChecked():
        #        mode = "BitTorrent"
        #    if self.Magnet.isChecked():
        #        mode = "Magnet"
        mode= self.Partition.currentText()
        mode = int(mode)
        # 以上提取了url和mode，创建一个前端的行和一个对应的下载器
        self.cnt = self.cnt + 1
        houzhui = '%d' % self.cnt
        out = 'test_' + houzhui + '.exe'
        print("Begin_1: ", self.aria.taskStatus)
        a, t, gid, success = startDownload(self.aria, url,mode, out)
        print("Begin_2: ", a.taskStatus)
        print(item_list)
        
        if success == 1:
            success, downloaditem, item = self.myDownloadBar(url, mode, a, t, gid, success)
        elif success == 2:
            reply = QMessageBox.information(self.begin, 'Error', '已有同名的下载任务正在进行或完成！', QMessageBox.Yes, QMessageBox.Yes)
            return
        # 判断有没有创建成功，比如url有没有出错之类的
        if success == 0:
            reply = QMessageBox.information(self.begin, 'Error', ' Download Failed,Check Your Url or Restart!', QMessageBox.Yes, QMessageBox.Yes)
            return
        self.DownloadList.addItem(item)
        self.DownloadList.setItemWidget(item, downloaditem)
        downloaditem.show()

    # 这是为mainwindow加入每一项的代码
    def myDownloadBar(self, url, mode, a, t, gid, success, append=1):
        bar = QtWidgets.QWidget()
        layout_main = QtWidgets.QHBoxLayout()
        layout_right = QtWidgets.QVBoxLayout()
        layout_left = QtWidgets.QVBoxLayout()
        layout_lefttop = QtWidgets.QHBoxLayout()
        layout_leftdown = QtWidgets.QHBoxLayout()
        StartPause = QtWidgets.QPushButton()
        # StartPause.clicked.connect(self.startandpause)
        StartPause.setText("Pause")
        pause_dic[gid] = StartPause
        Cancel = QtWidgets.QPushButton()
        Cancel.setText("Cancel")
        cancel_dic[gid] = Cancel
        Delete = QtWidgets.QPushButton()
        Delete.setText("X")
        Delete.setEnabled(False)
        X_dic[gid] = Delete
        bar_dic[gid] = bar
        layout_right.addWidget(StartPause)
        layout_right.addWidget(Cancel)
        layout_right.addWidget(Delete)
        filename = QtWidgets.QLabel()
        filename.setText(url)
        filename.setGeometry(QtCore.QRect(0, 10, 341, 21))
        layout_lefttop.addWidget(filename)
        progress = QtWidgets.QLabel()
        progress.setText("下载进度")
        progressbar = QtWidgets.QProgressBar()
        progressbar.setRange(0, 100)
        progressbar.setValue(0)
        progress_dic[gid] = progressbar
        layout_leftdown.addWidget(progress)
        layout_leftdown.addWidget(progressbar)
        layout_left.addLayout(layout_lefttop)
        layout_left.addLayout(layout_leftdown)
        layout_main.addLayout(layout_left)
        layout_main.addLayout(layout_right)
        bar.setLayout(layout_main)
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(QtCore.QSize(700, 120))
        # 以上是初始化UI，不用管 ,下面的代码需要关注一下，是ui和后端交互的内容#

        # 针对相应的url和mode创建下载器
        # 如果创建失败的话可以直接返回

        #a, t, gid, success = startDownload(self.aria, url)  # 调用Download函数创建下载任务，返回data = [a, t, gid]
        _, statusList = a.tellActive()
        status = 0
        if append == 1:
            if statusList is not None:
                for s in statusList:
                    if s['gid'] == gid:
                        status = s['status']
                        
                item_list.append(ui_item(url, mode, gid, a, t, 0, status))
       
        
        #print("myDownloadBar:")
        #print(a, t, gid, status)

        # item_list.append(ui_item(url, mode, gid, a, t, status))
        item_data = [a, t, gid]
        Cancel.clicked.connect(lambda: self.onCancelClicked(item_data,gid))
        Delete.clicked.connect(lambda: self.onDeleteClicked(item, item_data))
        StartPause.clicked.connect(lambda: self.onStartPauseClicked(StartPause, item_data))
        # 这是把对cancel和startpause两个按键的按这个操作和相应的代码连接起来，处理后面的两个相应的函数就行了

        # 这句代码是要根据url和mode创建一个该bar对应的下载任务，先暂时挂个url在这里

        return success, bar, item
    
    
    
     # for paused item
    def myDownloadBar_2(self, url, mode, a, t, gid, success, append=1):
        bar = QtWidgets.QWidget()

        layout_main = QtWidgets.QHBoxLayout()
        layout_right = QtWidgets.QVBoxLayout()
        layout_left = QtWidgets.QVBoxLayout()
        layout_lefttop = QtWidgets.QHBoxLayout()
        layout_leftdown = QtWidgets.QHBoxLayout()
        StartPause = QtWidgets.QPushButton()
        # StartPause.clicked.connect(self.startandpause)
        StartPause.setText("Continue")
        pause_dic[gid] =StartPause
        Cancel = QtWidgets.QPushButton()
        Cancel.setText("Cancel")
        cancel_dic[gid] = Cancel
        Delete = QtWidgets.QPushButton()
        Delete.setText("X")
        X_dic[gid] = Delete
        Delete.setEnabled(False)
        layout_right.addWidget(StartPause)
        layout_right.addWidget(Cancel)
        layout_right.addWidget(Delete)
        filename = QtWidgets.QLabel()
        filename.setText(url)
        filename.setGeometry(QtCore.QRect(0, 10, 341, 21))
        layout_lefttop.addWidget(filename)
        progress = QtWidgets.QLabel()
        progress.setText("下载进度")
        progressbar = QtWidgets.QProgressBar()
        progressbar.setRange(0, 100)
        progressbar.setValue(0)
        progress_dic[gid] =progressbar
        layout_leftdown.addWidget(progress)
        layout_leftdown.addWidget(progressbar)
        layout_left.addLayout(layout_lefttop)
        layout_left.addLayout(layout_leftdown)
        layout_main.addLayout(layout_left)
        layout_main.addLayout(layout_right)
        bar.setLayout(layout_main)
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(QtCore.QSize(700, 120))
        bar_dic[gid] = bar
        # 以上是初始化UI，不用管 ,下面的代码需要关注一下，是ui和后端交互的内容#

        # 针对相应的url和mode创建下载器
        # 如果创建失败的话可以直接返回

        #a, t, gid, success = startDownload(self.aria, url)  # 调用Download函数创建下载任务，返回data = [a, t, gid]
        _, statusList = a.tellActive()
        status = 0
        if append == 1:
            if statusList is not None:
                for s in statusList:
                    if s['gid'] == gid:
                        status = s['status']
                        
                item_list.append(ui_item(url, mode, gid, a, t, 0, status))
       
        
        #print("myDownloadBar:")
        #print(a, t, gid, status)

        # item_list.append(ui_item(url, mode, gid, a, t, status))
        item_data = [a, t, gid]
        print("myDownloadBar_2: ", a.taskStatus)
        Cancel.clicked.connect(lambda: self.onCancelClicked(item_data))
        Delete.clicked.connect(lambda: self.onDeleteClicked(item, item_data))
        StartPause.clicked.connect(lambda: self.onStartPauseClicked(StartPause, item_data))
        # 这是把对cancel和startpause两个按键的按这个操作和相应的代码连接起来，处理后面的两个相应的函数就行了

        # 这句代码是要根据url和mode创建一个该bar对应的下载任务，先暂时挂个url在这里

        return success, bar, item
    

    def debug_print(self):
        for item in item_list:
            print(item.gid, item.status)

    def onStartPauseClicked(self, StartPause, item_data):
        StartPause.setEnabled(False)
        time.sleep(0.4)
        StartPause.setEnabled(True) #出问题把这两句注释掉再试试
        status = 0
        for item in item_list:
            if item.gid == item_data[2]:
                status = item.status
                break
            
        print("status is %s"%status)
        
        if status == 'complete':
            print("zgq: Already completed. Don't permit to pause!")
            return
        elif status == 0:
            print("zgq: not found this gid in item_list")
        
        if StartPause.text() == "Pause": # 下载暂停
            StartPause.setText("Continue")
            status, gid = pauseDownload(item_data[0], item_data[2])  # (a, gid)
            for item in item_list:
                if item.gid == gid:
                    #print(item)
                    item.status = status  # 更新前端队列status
                    break
        else:  # 下载继续
            StartPause.setText("Pause")
            print("onStartPauseClicked: ", item_data[0].taskStatus)
            status, gid = unpauseDownload(item_data[0], item_data[2])  # (a, gid)
            for item in item_list:
                if item.gid == gid:
                    item.status = status  # 更新前端队列status
                    break
        self.debug_print()

    def onCancelClicked(self, item_data,gid):
        print("cancelClicked in")
        status = 0
        for item in item_list:
            if item.gid == item_data[2]:
                status = item.status
                break
            
        print("status is %s"%status)
        if status == 'downloading' :
            status, gid = unpauseDownload(item_data[0], item_data[2])  # (a, gid)
            for item in item_list:
                if item.gid == gid:
                    item.status = status  # 更新前端队列status
                    break
        if status == 'complete' :
            print("zgq: Already complete. Don't permit to pause!")
            return
        elif status == 0:
            print("zgq: not found this gid in item_list")

        X_dic[gid].setEnabled(True)
        pause_dic[gid].setEnabled(False)
        #bar_dic[gid].update()
        print("cancelClicked called")
        a = item_data[0]
        gid = item_data[2]
        _, statusList = a.tellActive()

        flag = True
        for s in item_list:
            if s.gid == gid:
                status = a.tellStatus(gid)
                if status['status'] == 'downloading' or status['status'] == 'paused':
                    flag = False
                break

        if flag:  # 证明要cancel的项目不在状态(downloading/paused)中，所以不能cancel
            return

        status, gid = stopDownload(a, gid)
        # 维护前端队列
        for i in range(len(item_list)):
            if item_list[i].gid == gid:
                item_list[i].status = status  # 更新前端队列状态，不删除记录
                break
        self.debug_print()
        return

    def onDeleteClicked(self, item, item_data):
        print("onDeleteClicked called")
        a = item_data[0]
        gid = item_data[2]
        _, statusList = a.tellActive()
        if statusList is not None:
            for s in statusList:
                if s['gid'] == gid:
                    status = a.tellStatus(gid)
                    if status['status'] == 'downloading' or status['status'] == 'paused': # 正在下载，不能删除
                        return
        # stopped/completed 任务可以删除
        self.DownloadList.takeItem(self.DownloadList.row(item))
        # 维护前端队列
        del_idx = 0
        for i in range(len(item_list)):
            if item_list[i].gid == gid:
                del_idx = i
                break
        item_list.pop(del_idx)  # 删除item_list的第i项，delete的任务下标
        deleteDownload(a, gid)
        self.debug_print()
        return

    # 下面这个函数不用管，初始化ui的
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 591)
        self.horizontalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 741, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Partition = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.Partition.setMinimumSize(640,10)
        for i in range(1,51):
            self.Partition.addItem(str(i))
        self.Partition.setCurrentIndex(4)
        #self.Magnet.setObjectName("Magnet")
        self.horizontalLayout.addWidget(self.Partition)
        #self.BitTorrent = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        #self.BitTorrent.setObjectName("BitTorrent")
        #self.horizontalLayout.addWidget(self.BitTorrent)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(MainWindow)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 741, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.urlLine = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.urlLine.setObjectName("urlLine")
        self.horizontalLayout_2.addWidget(self.urlLine)
        self.begin = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.begin.setObjectName("begin")
        self.horizontalLayout_2.addWidget(self.begin)
        self.DownloadList = QtWidgets.QListWidget(MainWindow)
        self.DownloadList.setGeometry(QtCore.QRect(-10, 100, 751, 491))
        self.DownloadList.setMinimumSize(QtCore.QSize(0, 421))
        self.DownloadList.setBatchSize(100)
        self.DownloadList.setObjectName("DownloadList")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 这个也是个不用管的函数
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "智能分拆："))
       # self.Magnet.setText(_translate("MainWindow", "Magnet"))
       # self.BitTorrent.setText(_translate("MainWindow", "BitTorrent"))
        self.label_2.setText(_translate("MainWindow", "请输入url:"))
        self.begin.setText(_translate("MainWindow", "下载"))
