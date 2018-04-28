# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com

import tornado

# Local import
from methods.watermark import *

class ImageVideoWatermarkByTextHandler(tornado.web.RequestHandler):
    def get(self):
        print ('image get pro')

    def post(self):
        input_path = self.get_argument('inputpath')
        output_path = self.get_argument('outputpath')
        watermark_text = self.get_argument('text')
        position = self.get_argument('position', 'Center')
        opacity = self.get_argument('opacity', 'light')

        result = image_video_watermark_by_text(input_path, watermark_text, output_path, position, opacity)
        print (result)
        self.write(json.dumps(result))
        self.finish()

class PdfWatermarkByTextHandler(tornado.web.RequestHandler):
    def get(self):
        print ('pdf get pro')

    def post(self):
        input_path = self.get_argument('inputpath')
        output_path = self.get_argument('outputpath')
        watermark_text = self.get_argument('text')
        # position = self.get_argument('position', 'Center')
        # opacity = self.get_argument('opacity', 'light')

        result = pdf_watermark_by_text(input_path, watermark_text, output_path)
        print (result)
        self.write(json.dumps(result))
        self.finish()
