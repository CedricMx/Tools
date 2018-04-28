# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 soovii
# Cedric, cedric_mx@163.com

import xlrd
import xlrd
from xlutils.copy import copy
import pprint

excel_path = 'D:/Cedric/TD/python_plugins/filter_column_excel/test.xlsx'

# get form
form = xlrd.open_workbook(excel_path)
w_form = copy(form)

# use sheet 3
sheet = form.sheet_by_index(3)
w_sheet = w_form.get_sheet(3)
a =[]
for i in range(0,sheet.nrows):
	if sheet.cell(i,10).value != '':
		a.append(sheet.cell(i,10).value)
b =[]
for i in range(0,sheet.nrows):
	if sheet.cell(i,12).value != '':
		b.append(sheet.cell(i,12).value)
#
have = []
not_have = []
for i in a:
	if i in b:
		have.append(i)
	else:
		not_have.append(i)

for row in range(0,len(have)):
	w_sheet.write(row,14,have[row])
for row in range(0,len(not_have)):
	w_sheet.write(row,15,not_have[row])
w_form.save('D:/test.xls')
