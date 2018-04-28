# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com

import os

cwd_path = os.getcwd()
project_path = os.path.dirname(cwd_path)
logfile_path = os.path.join(project_path, 'log','error.log')

print (os.path.exists(logfile_path))
