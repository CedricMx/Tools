# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com

import requests

# url = 'http://cedric.soovii.com:8082/imagevideowatermarkbytext'
url = 'https://www.baidu.com'
r = requests.get(url)
print (r.status_code)
