import sys
import os
import time
import subprocess
import xmlrpc.client
import random
import pickle
import urllib.parse
import ast

class task:
	def __init__(self):
		# 下载链接，必须给出
		self.link = ""
		# 下载目录，必须给出
		self.downloadPath = ""
		# 代理ip
		self.ip = ""
		# 代理端口
		self.port = ""
		# 代理用户名
		self.proxyUser = ""
		# 代理密码
		self.proxyPasswd = ""
		# 下载所需用户名
		self.downloadUser = ""
		# 下载所需密码
		self.downloadPasswd = ""
		# 下载线程数量，默认1
		self.connections = ""
		# 将文件分成多少段，默认5
		self.split = ""
		# 速度上限，默认0（无上限），如果给出，需要以K结尾或以M结尾，可以是浮点数（会转化成整数）
		self.limit = ""
		# 下载开始时间，格式：2016 3 28 22:24:24
		self.startTime = ""
		# 下载结束时间，格式：2016 3 28 22:24:24
		self.endTime = ""
		# 文件名，默认会自动取link最后一部分为名字
		self.out = ""
		# header，每个header用;隔开，每个header用:赋值
		self.header = ""
		# user agent
		self.userAgent = ""
		# cookies
		self.cookies = ""
		# referer
		self.referer = ""

class aria:
	def __init__(self):
		self.server = None
		self.port = -1
		self.taskDict = {}
		self.taskStatus = {}
		self.ariaProcess = None

	# self.startAria()

	@staticmethod
	def convertTimeToFloat(t: str):
		"""
		:param t: 字符串，时间格式：2016 3 28 22:24:24
		:return: 浮点数，返回从1970 1 1 0:0:0开始的计时
		将时间转化为浮点数
		"""
		if t == "":
			return 0
		else:
			return time.mktime(time.strptime(t, "%Y %m %d %H:%M:%S "))

	@staticmethod
	def convertLimit(limit: str):
		"""
		:param limit: 字符串，限速
		:return: 字符串，转化后的限速
		将浮点数转化为整数
		"""
		if limit != "0":
			limitNumber = float(limit[:-1])
			limitUnit = limit[-1]
			limitNumber = round(limitNumber)
			limit = str(limitNumber) + limitUnit
		return limit

	@staticmethod
	def humanReadbleSize(size, inputType = "file_size"):
		labels = ["KiB", "MiB", "GiB", "TiB"]
		i = -1
		if size < 1024:
			return str(size) + " B"
		while size >= 1024:
			i += 1
			size = size / 1024

		if inputType == "speed":
			j = 0
		else:
			j = 1

		if i > j:
			return str(round(size, 2)) + " " + labels[i]
		else:
			return str(round(size, None)) + " " + labels[i]

	def startAria(self, ariaPath = "", port = 6800, maxConcurrentDownloads = 5, loadSession = True):
		"""
		:param ariaPath: aria2c.exe所在的目录，默认当前目录
		:param port: aria的daemon监听端口
		:param maxConcurrentDownloads: 最多几个任务同时下载
		:param loadSession: 是否加载之前的session数据
		:return: bool，aria是否启动成功
		启动aria。这个函数需要一开始被调用。
		"""
		print("zgq: start Aria called")
		curDir = os.path.dirname(sys.argv[0])
		# 如果aria2c.exe目录没给出，默认当前目录
		if ariaPath == "":
			ariaPath = os.path.join(curDir, "aria2c.exe")

		# 如果没找到aria2c.exe，报错返回
		if not os.path.exists(ariaPath):
			print("ERROR: aria2c.exe doesn't exist in the current path.")
			return False

		# 如果aria已经启动，需要杀掉
		if self.server is not None:
			self.ariaProcess.kill()

		# 启动server
		self.port = port
		serverURI = "http://{}:{:d}/rpc".format("localhost", self.port)
		self.server = xmlrpc.client.ServerProxy(serverURI, allow_none = True, verbose = False)

		# 加载参数
		params = [ariaPath, "--no-conf", "--enable-rpc", "--rpc-listen-port=" + str(self.port),
				  "--rpc-allow-origin-all=true", "--continue=true",
				  "--rpc-max-request-size=1024M", "--rpc-listen-all", "--quiet=true",
				  "--max-concurrent-downloads=" + str(maxConcurrentDownloads),
				  "--save-session=sess"]

		# 加载之前存储的数据
		if loadSession:
			sessPath = os.path.join(curDir, "sess")
			taskDictPath = os.path.join(curDir, "taskDict.pkl")
			taskStatusPath = os.path.join(curDir, "taskStatus.pkl")
			if os.path.exists(sessPath) and os.path.exists(taskDictPath) and os.path.exists(taskStatusPath):
				params.append("--input-file=sess")
				with open(taskDictPath, "rb") as f:
					self.taskDict = pickle.load(f)
				with open(taskStatusPath, "rb") as f:
					self.taskStatus = pickle.load(f)
			else:
				print("Loading session failed. Sess: " + str(os.path.exists(sessPath))
					  + " taskDict: " + str(os.path.exists(taskDictPath))
					  + " taskStatus: " + str(os.path.exists(taskStatusPath)))
		# 不显示窗口
		flags = 0x08000000
		# 调用命令行，启动aria
		self.ariaProcess = subprocess.Popen(params, stderr = subprocess.PIPE, stdout = subprocess.PIPE,
											stdin = subprocess.PIPE, shell = False, creationflags = flags)

		time.sleep(5)
		# 利用getVersion函数来判断是否启动成功
		try:
			self.server.aria2.getVersion()
			return True
		except:
			return False

	def allocGID(self):
		"""
		:return: gid
		随机生成一个不重复的十六位十六进制字符串
		"""
		while True:
			# 生成一个十六位随机十六进制串
			gid = hex(random.randint(0x1000000000000000, 0x1999999999999999))
			# 去掉开头的0x
			gid = gid[2:]
			# 判断gid是否和已有的重复
			if not gid in self.taskDict:
				break
		return gid

	def addNewTask(self, t: task):
		"""
		:param t: 要添加的新task
		:return: gid
		给新task生成一个gid，并返回gid
		"""
		# 如果必填项为空，那么返回None
		if t.link == "" or t.downloadPath == "":
			return None

		# 生成一个gid给该task
		gid = self.allocGID()
		# 并加入taskDict
		self.taskDict[gid] = t
		return gid

	def downloadStart(self, gid, mode):
		"""
		:param gid: task的gid
		:return: bool，操作是否成功
		开始一个下载任务
		"""
		# 如果aria daemon未启动，返回错误
		if self.server is None:
			print("ERROR: Please call startAria() first")
			return False

		if os.path.isfile(os.path.join(self.taskDict[gid].downloadPath, self.taskDict[gid].out)):
			print("File with the same name already exists.")
			return 2

		# 判断任务是否有设置开始时间
		if self.taskDict[gid].startTime != "":
			self.taskStatus[gid] = "scheduled"
			# 进行等待
			self.waitToStart(gid)
		else:
			self.taskStatus[gid] = "waiting"

		# 生成header列表
		headerList = ["Cookie:" + str(self.taskDict[gid].cookies)]
		# 如果有header
		header = self.taskDict[gid].header
		if header != "":
			# header之间用;隔开
			semicolonSplitHeader = header.split(";")
			for i in semicolonSplitHeader:
				if i != "":
					# 去除前导空格
					i = i.lstrip()
					headerList.append(i)

		# 将浮点数速度转化为整数
		limit = self.convertLimit(self.taskDict[gid].limit)

		# 将ip和port连起来
		ip = self.taskDict[gid].ip
		port = self.taskDict[gid].port
		if ip != "" and port != "":
			ipPort = ip + ":" + port
		else:
			ipPort = ""

		# 判断下载目录是否存在
		downloadPath = self.taskDict[gid].downloadPath
		if not os.path.isdir(downloadPath):
			os.mkdir(downloadPath)

		# 判断下载是否被终止
		if self.taskStatus[gid] != "stopped":
			# 建立传参表
			ariaDict = {
				"gid": gid,
				"max-tries": "2",
				"retry-wait": "3",
				"timeout": "60",
				"header": headerList,
				"out": self.taskDict[gid].out,
				"user-agent": self.taskDict[gid].userAgent,
				"referer": self.taskDict[gid].referer,
				"all-proxy": ipPort,
				"max-download-limit": limit,
				"all-proxy-user": self.taskDict[gid].proxyUser,
				"all-proxy-passwd": self.taskDict[gid].proxyPasswd,
				"http-user": self.taskDict[gid].downloadUser,
				"http-passwd": self.taskDict[gid].downloadPasswd,
				"split": mode,
				"max-connection-per-server": self.taskDict[gid].connections,
				"min-split-size": "1M",
				"continue": "true",
				"dir": downloadPath
			}

			# 清除空的参数
			ariaDictCopy = ariaDict.copy()
			for key in ariaDictCopy.keys():
				if ariaDictCopy[key] == "":
					del ariaDict[key]

			try:
				result = self.server.aria2.addUri([self.taskDict[gid].link], ariaDict)
				# print(result + " starts.")

				# 如果有终止时间，进入循环等待
				if self.taskDict[gid].endTime != "":
					self.waitToEnd(gid)
				return True  # zbc added
			except:
				self.taskStatus[gid] = "error"
				print("ERROR: Download didn't start.")
				return False
		else:
			# 如果任务被终止，也算执行成功（？）
			# print("Download is stopped.")
			return True

	def downloadStop(self, gid):
		"""
		:param gid: 要结束的任务gid
		:return: 是否成功
		结束掉编号为gid的任务，如果正在下载，会删除已下载的文件
		"""
		# 先调用tellStatus更新taskStatus
		self.tellStatus(gid)
		status = self.taskStatus[gid]
		# 如果状态是scheduled，该任务还未发送给aria
		if status == "scheduled":
			self.taskStatus[gid] = "stopped"
		else:
			# 对于其他状态，给aria发送终止指令
			try:
				self.server.aria2.remove(gid)
				# 如果正在下载，需要删除掉已经下载的文件
				if status == "downloading":
					fileStatus = self.tellStatus(gid)
					self.server.aria2.removeDownloadResult(gid)
					# 多文件这里可能会遇到问题
					if os.path.isfile(fileStatus["path"]):
						os.remove(fileStatus["path"])
					if os.path.isfile(fileStatus["path"] + ".aria2"):
						os.remove(fileStatus["path"] + ".aria2")
			except:
				print("ERROR: Aria remove error.")
				return False
			# 如果下载未完成，需要把状态改成终止
			if status != "complete":
				self.taskStatus[gid] = "stopped"
		return True

	def downloadPause(self, gid):
		"""
		:param gid: 要暂停的任务gid
		:return: 是否成功
		暂停任务的下载
		"""
		try:
			self.server.aria2.pause(gid)
			return True
		except:
			print("ERROR: Pause error.")
			return False

	def downloadUnpause(self, gid):
		"""
		:param gid: 要继续的任务gid
		:return: 是否成功
		继续被暂停的任务
		"""
		try:
			print("gid for downloadUnpause is", gid)
			self.server.aria2.unpause(gid)
			return True
		except:
			print("ERROR: Unpause error.")
			return False

	def updateLimitSpeed(self, gid, limit):
		"""
		:param gid: 任务gid
		:param limit: 任务限速
		:return: 是否成功
		更新任务的限速
		"""
		# 将浮点数速度转化为整数
		limit = self.convertLimit(limit)
		try:
			self.server.aria2.changeOption(gid, {"max-download-limit": limit})
			return True
		except:
			print("ERROR: Update limit speed error.")
			return False

	def downloadDelete(self, gid):
		"""
		:param gid: 任务gid
		:return: 是否删除成功
		删除该任务的历史记录，传入的任务状态必须是stopped或complete
		"""
		# 先调用tellStatus更新taskStatus
		self.tellStatus(gid)
		if self.taskStatus[gid] != "stopped" and self.taskStatus[gid] != "complete":
			print("Task's status is " + self.taskStatus[gid] + ", can not be deleted.")
			return False
		self.taskStatus.pop(gid)
		self.taskDict.pop(gid)
		return True

	def shutdownAria(self):
		"""
		:return: 是否成功
		关闭aria并保存记录
		"""
		# 如果aria还没启动
		if self.server is None:
			print("Aria has not started.")
			return False

		try:
			self.server.aria2.shutdown()
			time.sleep(5)
			self.ariaProcess.kill()
			# self.ariaProcess.communicate()

			# 保存字典
			curDir = os.path.dirname(sys.argv[0])
			taskDictPath = os.path.join(curDir, "taskDict.pkl")
			taskStatusPath = os.path.join(curDir, "taskStatus.pkl")
			with open(taskDictPath, "wb") as f:
				pickle.dump(self.taskDict, f)
			with open(taskStatusPath, "wb") as f:
				pickle.dump(self.taskStatus, f)
		except:
			print("ERROR: Aria2 shutdown error.")
			return False

		# 初始化参数
		self.server = None
		self.port = -1
		self.taskDict = {}
		self.taskStatus = {}
		self.ariaProcess = None
		return True

	def tellActive(self):
		"""
		:return: 两个列表，分别为gid（字符串）列表和状态（dict）列表
		返回所有正在下载的任务gid和状态
		"""
		try:
			downloadsStatus = self.server.aria2.tellActive(
				["gid", "status", "connections", "errorCode", "errorMessage", "downloadSpeed", "connections", "dir",
				 "totalLength", "completedLength", "files"])
		except:
			return None, None

		downloadStatusList = []
		gidList = []
		# 转化信息格式
		for dict in downloadsStatus:
			convertedInfoDict = self.convertDownloadInformation(dict)
			gidList.append(dict["gid"])
			downloadStatusList.append(convertedInfoDict)
		return gidList, downloadStatusList

	def tellStatus(self, gid):
		"""
		:param gid: 任务gid
		:return: 一个dict
		返回该任务的下载状态
		"""
		try:
			downloadStatus = self.server.aria2.tellStatus(
				gid, ["status", "connections", "errorCode", "errorMessage", "downloadSpeed", "connections", "dir",
					  "totalLength", "completedLength", "files"])
			downloadStatus["gid"] = gid
		except:
			# print("kill!!!!!!!!   ", gid)
			# print(self.taskStatus)
			return {"status": self.taskStatus[str(gid)]}

		# 转化信息格式
		convertedInfoDict = self.convertDownloadInformation(downloadStatus)
		self.taskStatus[gid] = convertedInfoDict["status"]

		# 如果出错，给出错误信息，并删除下载缓存
		if convertedInfoDict["status"] == "error":
			convertedInfoDict["error"] = str(downloadStatus["errorMessage"])
			self.server.aria2.remove(gid)
			self.server.aria2.removeDownloadResult(gid)
			# 多文件这里可能会遇到问题
			if os.path.isfile(convertedInfoDict["path"]):
				os.remove(convertedInfoDict["path"])
			if os.path.isfile(convertedInfoDict["path"] + ".aria2"):
				os.remove(convertedInfoDict["path"] + ".aria2")
		return convertedInfoDict

	def convertDownloadInformation(self, downloadStatus):
		"""
		:param downloadStatus: dict，从aria获得的下载状态
		:return: dict，转化后的下载状态
		将aria获得的状态转化为前端要用的状态
		"""
		# 获取文件名和路径
		try:
			fileStatus = str(downloadStatus["files"])
			fileStatus = fileStatus[1:-1]
			fileStatus = ast.literal_eval(fileStatus)
			path = str(fileStatus["path"])
			fileName = urllib.parse.unquote(os.path.basename(path))
			if not fileName:
				fileName = None
			# 只取第一个下载链接，多文件就会有问题
			uris = fileStatus["uris"]
			uri = uris[0]
			link = uri["uri"]
		except:
			fileName = None
			link = None
			path = None

		# 删掉空的状态
		for i in downloadStatus.keys():
			if not downloadStatus[i]:
				downloadStatus[i] = None

		# 获取文件大小
		try:
			fileSize = float(downloadStatus["totalLength"])
		except:
			fileSize = None

		# 获取已下载的文件大小
		try:
			downloaded = float(downloadStatus["completedLength"])
		except:
			downloaded = None

		# 转化文件大小
		if downloaded is not None and fileSize is not None and fileSize != 0:
			fileSizeCopy = fileSize
			downloadedCopy = downloaded

			# 转化为KiB/MiB/GiB
			sizeStr = self.humanReadbleSize(fileSize)
			downloadedStr = self.humanReadbleSize(downloaded)

			# 计算下载百分比
			fileSize = fileSizeCopy
			downloaded = downloadedCopy
			percent = int(downloaded * 100 / fileSize)
			percentStr = str(percent) + "%"
		else:
			percentStr = None
			sizeStr = None
			downloadedStr = None

		# 获取下载速度
		try:
			downloadSpeed = int(downloadStatus["downloadSpeed"])
		except:
			downloadSpeed = 0

		# 转化下载速度并获取下载估计时间
		if downloaded is not None and downloadSpeed != 0:
			# 转化为KiB/MiB/GiB
			downloadSpeedStr = self.humanReadbleSize(downloadSpeed, "speed") + "/s"

			estimateTimeLeft = int((fileSize - downloaded) / downloadSpeed)
			eta = ""
			if estimateTimeLeft >= 3600:
				eta = eta + str(int(estimateTimeLeft / 3600)) + "h"
				estimateTimeLeft = estimateTimeLeft % 3600
				eta = eta + str(int(estimateTimeLeft / 60)) + "m"
				estimateTimeLeft = estimateTimeLeft % 60
				eta = eta + str(estimateTimeLeft) + "s"
			elif estimateTimeLeft >= 60:
				eta = eta + str(int(estimateTimeLeft / 60)) + "m"
				estimateTimeLeft = estimateTimeLeft % 60
				eta = eta + str(estimateTimeLeft) + "s"
			else:
				eta = eta + str(estimateTimeLeft) + "s"
			estimateTimeLeftStr = eta
		else:
			downloadSpeedStr = "0"
			estimateTimeLeftStr = None

		# 获取下载线程数
		try:
			connectionsStr = str(downloadStatus["connections"])
		except:
			connectionsStr = None

		# 获取下载状态
		try:
			statusStr = str(downloadStatus["status"])
		except:
			statusStr = None

		# 将下载状态改名为前端需要的名称
		if statusStr == "active":
			statusStr = "downloading"
		if statusStr == "removed":
			statusStr = "stopped"
		if statusStr == "None":
			statusStr = None

		# 如果任务完成，剩余时间设置为0
		if statusStr == "complete":
			estimateTimeLeftStr = "0s"

		download_info = {
			"gid": downloadStatus["gid"],
			"file_name": fileName,
			"status": statusStr,
			"size": sizeStr,
			"downloaded_size": downloadedStr,
			"percent": percentStr,
			"connections": connectionsStr,
			"rate": downloadSpeedStr,
			"estimate_time_left": estimateTimeLeftStr,
			"link": link,
			"path": path
		}
		return download_info

	def waitToStart(self, gid):
		# 将日期格式转化为浮点数
		startTime = self.convertTimeToFloat(self.taskDict[gid].startTime)
		nowTime = time.time()
		# 一直循环判断时间
		while startTime > nowTime:
			time.sleep(3)
			# 如果该任务被终止了，那么直接返回
			if self.taskStatus[gid] == "stopped":
				return
			# 更新时间，因为有可能修改
			startTime = self.convertTimeToFloat(self.taskDict[gid].startTime)
			nowTime = time.time()
		# 到达时间，返回
		return

	def waitToEnd(self, gid):
		# 将日期格式转化为浮点数
		endTime = self.convertTimeToFloat(self.taskDict[gid].endTime)
		nowTime = time.time()
		# 一直循环判断时间
		while endTime > nowTime:
			time.sleep(3)
			# 如果该任务终止了，或者下载完成了，直接返回
			if self.taskStatus[gid] == "stopped" or self.taskStatus[gid] == "complete":
				return
			# 更新时间，因为有可能修改
			endTime = self.convertTimeToFloat(self.taskDict[gid].endTime)
			nowTime = time.time()

		# 到达时间，并且任务未终止或下载完，暂停任务
		self.downloadPause(gid)

def quitAria(a):
	# 关闭aria
	print("Shutdown aria")
	a.shutdownAria()

def startDownload(a, url, mode, out, path = "C:/Users/15112/Desktop/Download"):
	# 新建一个任务
	# test_id = test_id + 1
	t = task()
	t.link = url
	t.downloadPath = path
	t.limit = "128K"
	# t.out = "test_" + test_id + ".exe"
	out_list = url.split("/")
	out = out_list[len(out_list) - 1]
	t.out = out
	t.connections = "5"

	# res = a.startAri(loadSession=False)
	# print("Aria start result: " + str(res))
	gid = a.addNewTask(t)

	# 开始下载任务，前端实现时需要新建一个线程执行downloadStart
	print("Start download")
	flag = a.downloadStart(gid, mode)
	# print("flag "+str(flag))
	return a, t, gid, flag

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
	print("unpausedownload: ", a.taskStatus)
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
	print("debug1")
	status = a.tellStatus(gid)  # 更新后端status为aria的新status
	print(status['status'])
	print("stop download return")
	return status['status'], gid

if __name__ == "__main__":
	# 新建一个任务
	t = task()
	t.link = "http://down.kuwo.cn/mbox/kwmusic_w1_bds_20191213.exe"
	t.downloadPath = "C:/Users/15112/Desktop/download"
	t.limit = "128K"
	t.out = "test.exe"
	t.connections = "5"

	# 启动aria并加入任务，需要记录gid
	a = aria()
	res = a.startAria(loadSession = False)
	print("Aria start result: " + str(res))
	gid = a.addNewTask(t)

	# 开始下载任务，前端实现时需要新建一个线程执行downloadStart
	print("Start download")
	a.downloadStart(gid)

	# 让任务跑10秒，并同时输出状态
	nowTime = time.time()
	while time.time() - nowTime < 10:
		gidList, statusList = a.tellActive()
		print(gidList)
		print(statusList)
		time.sleep(1)

	# 暂停任务
	print("Pause download")
	a.downloadPause(gid)
	gidList, statusList = a.tellActive()
	print(gidList)
	print(statusList)
	status = a.tellStatus(gid)
	print(status)

	# 关闭aria
	print("Shutdown aria")
	a.shutdownAria()

	time.sleep(5)

	# 重启aria
	res = a.startAria()
	print("debug" + str(a.taskDict))
	print("Aria start result: " + str(res))
	gidList, statusList = a.tellActive()
	print(gidList)
	print(statusList)
	status = a.tellStatus(gid)
	print(status)

	# 继续任务
	print("Unpause download")
	a.downloadUnpause(gid)
	nowTime = time.time()
	while time.time() - nowTime < 10:
		gidList, statusList = a.tellActive()
		print(gidList)
		print(statusList)
		time.sleep(1)

	# 修改限速，再下五秒看看
	print("Change limit speed")
	a.updateLimitSpeed(gid, "1M")
	nowTime = time.time()
	while time.time() - nowTime < 5:
		gidList, statusList = a.tellActive()
		print(gidList)
		print(statusList)
		time.sleep(1)

	# 终止任务（这个指令速度可能比较慢，建议单开一个线程）
	print("Stop download")
	a.downloadStop(gid)

	# 重启终止任务（必须重建一个任务）
	print("Restart download")
	# 改参数可以直接改task
	t.limit = "0"
	gid = a.addNewTask(t)
	a.downloadStart(gid)

	while True:
		gidList, statusList = a.tellActive()
		print(gidList)
		print(statusList)

		if len(gidList) == 0:
			break
		time.sleep(1)

	# 下载完成
	print("Download Completed")

	# !!!只有在调用tellStatus时，才会更新任务gid的状态!!!
	status = a.tellStatus(gid)
	print(status)

	# 删除任务
	# 如果下载完成时没有调用tellStatus，这里任务gid的状态仍为downloading，不会删除
	print(a.taskStatus[gid])
	a.downloadDelete(gid)

	# 结束时一定要调用这个
	a.shutdownAria()
