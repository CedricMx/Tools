# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com

from .handler import *

urlpatterns = [
    # 给图片或视频打文字水印
    (r'/imagevideowatermarkbytext', ImageVideoWatermarkByTextHandler),
    (r'/pdfwatermarkbytext', PdfWatermarkByTextHandler)
]
