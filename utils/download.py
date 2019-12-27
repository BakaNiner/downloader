import mainwindow
import os
import pickle
from mainwindow import *
from download import *
from PyQt5 import QtWidgets
import sys
import time
from threading import Thread
import inspect
import ctypes

flag = 1
#http://down.kuwo.cn/mbox/kwmusic_w1_bds_20191213.exe
#http://down.sandai.net/thunderx/XunLeiWebSetup10.1.26.618gw.exe
#https://dldir1.qq.com/weixin/Windows/WeChat_C1018.exe
#http://xmp.down.sandai.net/xmp/XMPSetup6.1.2.650xmpgw.exe

 
item_list = []
progress_dic = {}
pause_dic = {}
cancel_dic = {}
X_dic = {}
bar_dic = {}
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

 

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)



def print_itemlist():
    for item in mainwindow.item_list:
        print(item.gid, item.status)


class myMainwindow(QtWidgets.QMainWindow):
    def __init__(self, aria_pointer):
        QtWidgets.QMainWindow.__init__(self)
        self.aria_pointer = aria_pointer
        #print("before startAria" + str(aria_pointer.taskDict))
        #print("before startAria" + str(aria_pointer.taskStatus))
        res = aria_pointer.startAria()
        #print("after startAria" + str(aria_pointer.taskDict))
        #print("after startAria" + str(aria_pointer.taskStatus))
        #print("Aria start result: " + str(res))

    def closeEvent(self, event):
        print("quit Aria")
        print(aria_pointer)
        #self.aria_pointer.tellActive()
        for item in mainwindow.item_list:
            if item.status == 'downloading':
                status, gid = pauseDownload(item.a, item.gid)  # (a, gid)
                item.status = 'paused'
                
        isSucess = aria_pointer.shutdownAria()
               
        curDir = os.path.dirname(sys.argv[0])
        ItemListPath = os.path.join(curDir, "ItemList.pkl")
        with open(ItemListPath, "wb") as f:
            pickle.dump(mainwindow.item_list, f)
            
        
        global flag 
        flag = 0
        print("quit Aria shutdown returned %d" % isSucess)
        while not isSucess:
            event.ignore()
            isSucess = aria_pointer.shutdownAria()
            print(isSucess)
        #global flag
        #flag = 0
        event.accept()
        
        
        



if __name__ == '__main__':
    item_list = []
    app = QtWidgets.QApplication(sys.argv)
    aria_pointer = aria()
    #res = aria_pointer.startAria()
    mainwindows = myMainwindow(aria_pointer)
    #print("debug+:" + str(aria_pointer))
    ui = Ui_MainWindow(mainwindows)
    mainwindows.show()
   # maxiter = 500
    
   # t = Thread(target=signal.interval_check, args=(0.5, aria_pointer, maxiter ))
   # t.setDaemon(True)
   # t.start()
    
    #stop_thread(t)
    
    #print("thread stopped!")
    
    #flag = 0
    sys.exit(app.exec_())
    t.quit()

   
