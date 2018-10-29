#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql,sys
sys.path.append("..")
from job_syh.config.config import *



def get_db_conn():
    '''连接数据库'''
    conn = pymysql.connect(host=db_host,
                            port=db_port,
                            user=db_user,
                        password=db_passwd,
                         db=db_api)
    return conn

def query_db(sql):
    '''查询，不需要commint'''
    logging.debug(sql)
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    logging.debug(result)
    return result

def change_db(sql):
    ''''''
    logging.debug(sql)
    conn = get_db_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as a:
        conn.rollback()
        print("数据库操作失败")





