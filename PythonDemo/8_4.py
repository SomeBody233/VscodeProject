import datetime
import time
timeStamp = time.time()-60*60*24*3 #获得3天前的时间
#时间戳转换成标准时间格式
timeArray = datetime.datetime.utcfromtimestamp(timeStamp)
formatTime = timeArray.strftime("%Y-%m-%d %H:%M:%S")
print (formatTime)