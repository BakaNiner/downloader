# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 21:16:29 2019

@author: 15112
"""

from threading import Thread
import time
 
 
def sayhi(name):
    time.sleep(2)
    print("%s say hello" % name)
 
 
if __name__ == '__main__':
    t = Thread(target=sayhi, args=('mike', ))
    t.start()
    print("主线程")