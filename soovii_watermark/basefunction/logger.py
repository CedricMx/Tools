# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com

import os
import logging

def logging_function():

    currentpath = os.path.dirname(__file__)
    logpath = os.path.dirname(currentpath)
    logfilepath = os.path.join(logpath, 'log', 'error.log')

    logger = logging.getLogger("error_log")
    logger.setLevel(logging.DEBUG)

    # 建立一个filehandler来把日志记录在文件里，级别为debug以上
    fh = logging.FileHandler(logfilepath)
    fh.setLevel(logging.DEBUG)

    # 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # 设置日志格式
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", '%Y-%m-%d %H:%M:%S')

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    #将相应的handler添加在logger对象中
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

logger = logging_function()

if __name__ == '__main__':

    logger.debug('test-debug')
    logger.info('test-info')
    logger.warning('test-warn')
    logger.error('test-error')
