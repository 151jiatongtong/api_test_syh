#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging,os
#项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#case路径
data_file = os.path.join(prj_path,'data','manageexcel.xls')

#主机+端口
url='192.168.2.135:18080'
#unitest执行文件夹
testcase_path = os.path.join(prj_path,'unitest_job')
#report路径
report_file = os.path.join(prj_path,'report','report.html')
#log路径
log_file = os.path.join(prj_path,'log','log.txt')




#全局log配置
logging.basicConfig(level=logging.DEBUG,#日志级别
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    filemode="a")

#数据库配置
db_host= '192.168.2.242'
db_port = 3306
db_user = 'root'
db_passwd = "Nbs@2010"
db_api = 'lens_mobapp_data'

#邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '985134468@qq.com'
smtp_password = 'ozprfvtrlrltbdcd'

sender = smtp_user
receiver = '17612254995@163.com,2057689257@qq.com'
sunject = '接口测试报告'
email_body = 'HI,all\n测试完成，请查看附件'



if __name__ == "__main__":
    logging.info("hello")