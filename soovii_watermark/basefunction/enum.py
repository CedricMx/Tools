# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com

# 水印位置
class watermark_position:
    position = [
        {'key':'LeftUp', 'value':'x=0:y=0'},
        {'key':'LeftBottom', 'value':'x=0:y=(h-th)'},
        {'key':'RightBottom', 'value':'x=(w-tw):y=(h-th)'},
        {'key':'RightUp', 'value':'x=(w-tw):y=0'},
        {'key':'Center', 'value':'x=(w-tw)/2:y=(h-th)/2'},
    ]

    @classmethod
    def text_position(self, key):
        for i in watermark_position.position:
            if (i['key']==key):
                return i['value']


# 水印透明度
class watermark_opacity:
    opacity = [
        {'key':'light', 'value':0.2},
        {'key':'mid', 'value':0.4},
        {'key':'heavy', 'value':0.6}
    ]

    @classmethod
    def text_opacity(self, key):
        for i in watermark_opacity.opacity:
            if (i['key']==key):
                return i['value']
