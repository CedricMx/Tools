# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com

import os
import json
from PyPDF2 import PdfFileWriter, PdfFileReader
import reportlab.pdfbase.ttfonts
ttc_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'simsun.ttc')
reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('song', ttc_path))
from reportlab.pdfgen import canvas

# Local import
from basefunction.enum import *
from basefunction.logger import *
