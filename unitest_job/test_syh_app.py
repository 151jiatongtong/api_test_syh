#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json,sys,unittest
from ddt import ddt,data,unpack
from lib import Model
from lib import Modeltime
import requests
sys.path.append("..")
from config.config import *
from lib.request import *
# from job_syh.lib.db_mysq import *

@ddt
class TestSYH_APP(unittest.TestCase):
    @data(*Modeltime.DataHelper().readExcels())
    @unpack
    def testapi_app_minute(self,switch,testcase,method,uri,header,body,exception):
        print(testcase)
        # res = requests.post(url=url,data=json.loads(body),headers=json.loads(header))
        res = request(method,uri,header,body)
        print(res.status_code)
        self.assertEqual(200,res.status_code,msg=None)
        # print(res.text)






if __name__ == "__main__":
    unittest.main()













'''
class TestTestSYH_APP(unittest.TestCase):
    # data = getdata(data_file)
    def test_requests(self):
        case_data = getdata(data_file)
        for i in range(len(case_data)):
            # data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]
            print(case_data[i][1])
            url = case_data[i][3]
            data = case_data[i][4]  # json格式的字符串转成字典
            headers = case_data[i][6]
            expect_res = case_data[i][5]
            res = requests.post(url=url, params=json.loads(data), headers=json.loads(headers))
            # print(json.loads(res.text))
            response = json.loads(res.text)
            # print(response['data'])
            self.assertEqual('200',str(res.status_code),msg = None)
            # self.assertIsNotNone(response['data'])

if __name__ == '__main__':
'''


