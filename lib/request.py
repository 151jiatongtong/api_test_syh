import requests,json
import ast
from configparser import ConfigParser
from config.config import *
# conf = ConfigParser()
# conf.read("../config/config.ini")
# env = conf.get("env","env")
# if env == "pre":
#     host = conf.get("pre","url")
# if env == "test":
#     host = conf.get("test","url")
#     #print(host)
host =url
def request(method,uri,header,body):
    if header:
        # header = json.loads(header)
        header = ast.literal_eval(header)
    else:
        header = None
    #body = json.loads(body)#将json形式的字符串转化成字典
    # body = eval(body)#将字符串转化成字典，但存在安全性问题
    body = ast.literal_eval(body)#将字符串转化成字典
    if method == "get":
        r = requests.get("http://%s%s"%(host,uri),params=body,headers=header)
    if method == "post":
        # r = requests.post("http://%s%s"%(host,uri),json=body,headers=header)
        r = requests.post("http://%s%s" % (host, uri), data=body, headers=header)
    return r