from download import *

def quitAria(a):
	# 关闭aria
	print("Shutdown aria")
	a.shutdownAria()

def startDownload(a, url, split, out, path = "D:/test"):
	# 新建一个任务
	t = task()
	t.link = url
	t.downloadPath = path
	t.limit = "512K"
	t.split = split
	t.out = out
	t.connections = "5"

	gid = a.addNewTask(t)

	# 开始下载任务，前端实现时需要新建一个线程执行downloadStart
	print("Start download")
	flag = a.downloadStart(gid)
	return t, gid, flag

def pauseDownload(a, gid):
	# 暂停任务
	print("Pause download")
	a.downloadPause(gid)
	status = a.tellStatus(gid)  # 更新后端status为aria的新status
	print(status['status'])
	return status['status'], gid

def unpauseDownload(a, gid):
	print("Unpause download")
	a.downloadUnpause(gid)
	status = a.tellStatus(gid)  # 更新后端status为aria的新status
	print(status['status'])
	return status['status'], gid

def deleteDownload(a, gid):
	# 删除任务
	# 如果下载完成时没有调用tellStatus，这里任务gid的状态仍为downloading，不会删除
	print("Delete download")
	print(a.taskStatus[gid])
	a.downloadDelete(gid)

def stopDownload(a, gid):
	# 终止任务（这个指令速度可能比较慢，建议单开一个线程）
	print("Stop download")
	a.downloadStop(gid)
	status = a.taskStatus[gid]  # 更新后端status为aria的新status
	print(status)
	return status, gid