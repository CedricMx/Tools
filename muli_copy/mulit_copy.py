# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 soovii
# Cedric, cedric_mx@163.com

import os
from os import listdir
from os.path import exists, join
import xlrd
import shutil



def read_excel(excel_path,sheet_index, col, start_row):
	'''get value of row and col in sheet of excel '''

	# Access excel by path
	workbook = xlrd.open_workbook(excel_path)
	# Access the sheet of excel
	sheet = workbook.sheet_by_index(sheet_index)

	# Collect data
	shot =[]
	for i in range(start_row,sheet.nrows):
		if sheet.cell(i,col).value != '':
			shot.append(sheet.cell(i,col).value)
	print('shot number: ',len(shot))
	print('-'*80)

	return shot

def mulit_copy(path,ex_path, shot):

	# print('shot number: ',len(shot))

	if os.path.exists(path):
		# print(os.listdir(path))

		# make local dir
		if not os.path.exists(ex_path):
			os.mkdir(ex_path)
			print('create :',ex_path)

		num = 1
		for i in shot:

			# get epi number
			epi = i.split('_')[1]
			# print(epi)
			search_path = join(path,epi)

			# check shot in this dir

			for mov in os.listdir(search_path):
				name = os.path.basename(mov)
				# print(name)

				if name.startswith(i):
					oldfile= join(search_path, name)
					newfile= join(ex_path, name)
					# shutil.copyfile(oldfile,newfile)
					print('zhouyou is dog: {}/{},from{} to {}'.format(num,len(shot),oldfile,newfile))
					num = num +1


	else:
		print('Not exist:{}'.format(path))


# Test
excel_path = 'D:/zhouyou.xlsx'
sheet_index = 2
col = 0
start_row = 1
shot = read_excel(excel_path,sheet_index, col, start_row)

path = '//192.168.2.238/byt/Editorial/Demo/SooviiDemo/ShotDemo'
ex_path = 'D:/Cedric'
mulit_copy(path,ex_path, shot)
