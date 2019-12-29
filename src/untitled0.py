# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 22:30:17 2019

@author: 15112
"""

import inspect

import ctypes

from threading import Thread

def _async_raise(tid, exctype):
	"""raises the exception, performs cleanup if needed"""

	tid = ctypes.c_long(tid)

	if not inspect.isclass(exctype):
		exctype = type(exctype)

	res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))

	if res == 0:

		raise ValueError("invalid thread id")

	elif res != 1:

		# """if it returns a number greater than one, you're in trouble,

		# and you should call it again with exc=NULL to revert the effect"""

		ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)

		raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
	_async_raise(thread.ident, SystemExit)

def Receive():
	while 1:
		print(1)

		time.sleep(0.1)

def Send():
	while 1:
		print(2)

		time.sleep(0.1)

if __name__ == "__main__":
	t1 = Thread(target = Receive)

	t2 = Thread(target = Send)

	t1.start()

	t2.start()

	stop_thread(t1)

	stop_thread(t2)
