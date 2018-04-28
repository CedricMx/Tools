# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com
'''
传输多个大文件
利用:
    多线程
    队列
    断点续传
'''

import time
import os
import shutil


def check_path(input_file, output_path):
    '''
    Make sure input path exists
    and output path exsits, if not creat one
    '''
    try:
        # If input file exists
        if os.path.isfile(input_file):
            # If output path exists
            if not os.path.exists(output_path):
                os.makedirs(output_path)
                return True, ''
            else:
                # If file exists in output check_path
                filename = os.path.basename(inputfile)
                output_file = os.path.join(output_path, filename)
                if os.path.exists(output_file):
                    return  False, 'ERROR:output file already exists !'

                else:
                    return True, ''
        else:
            return False, 'ERROR:input file not exists !'

    except Exception as e:
        return False, e


def file_copy(input_file, output_path, size):
    '''
    1kB = 1024B
    1B = 8b
    '''
    start_time = time.time()
    with open(input_file, 'rb') as f:
        # Get size of file
        final_pos = f.seek(0, 2)

        pos = 0
        while pos < f.seek(0, 2):
            f.seek(pos,0)
            data = f.read(size)

            with open(output_path, 'ab') as fw:
                fw.write(data)
            # print(pos, data)
            pos += size

    end_time = time.time()
    run_time = end_time - start_time
    data = float('%.2f' % run_time)

    return True, data


def file_transfer(input_file, output_path):

    # Copy file
    filename = os.path.basename(input_file)
    output_file = os.path.join(output_path,filename)
    if not os.path.exists(output_file):
        shutil.copyfile(input_file, output_file)
        print('finish')


if __name__ == '__main__':
    inputfile = r'D:\Cedric\TD\Tools\file_transfer\Test\test.mp4'
    outputpath = r'D:\Cedric\TD\Tools\file_transfer\Test'
    size = 46593

    print(check_path(inputfile, outputpath))
    # file_transfer(inputfile,outputpath)

    # print (file_copy(inputfile, outputpath, size))
    print ()
