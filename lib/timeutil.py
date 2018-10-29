# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 19:09
# @Author  : pangyu
# @Email   : 2315307446@qq.com
# @File    : getTime.py
# @Software: PyCharm
#获取当前时间
import datetime as dt
import time
# now=dt.datetime.now()
# print(now)


def getlocalTime():
    localtime = time.localtime()#获取本地时间
    tm = time.strftime("%Y-%m-%d %H:%M:%S",localtime)#将获取的本地时间格式化:2016-03-20 11:45:39  "%Y-%m-%d 00:00:00"
    print(tm)
    return tm

def getTimeperiod():
#定义时间区间
   #timeperiod = [30, 60, 360, 720, 1440, 4320, 10080, 20160, 43200, 86400, 129600]
   timeperiod = [60,1440,20160,129600]
   return timeperiod
def getTimegranularitysql():
    timegranularitysql = [1,2,5,30,60,180,360,720,1440,2880,4320]
    return timegranularitysql
def getTimegranularity():
    #timegranularity = ['1m','2m','5m','30m','1h','3h','6h','12h','1d','2d','3d']
    timegranularity = ['2m','1h','12h','3d']
    return timegranularity
# if __name__ == '__main__':
#     b=getlocalTime()


# def getminTime():
#     pass
# def gethourTime():
#     pass
#
# def getTick():
#     # 是不是要考虑一下，传入参数，如果是自己定义的时间，也能得出时间戳
#    a=getlocalTime()
#    g = time.strptime(a, "%Y-%m-%d %H:%M:%S")
#    ticks = time.mktime(g)
#    # ticks = time.time()
#    # print(ticks)
#    return (ticks)