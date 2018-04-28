# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com

from .importpy import *

def image_video_watermark_by_text(input_path, watermark_text, output_path, position, opacity):
    '''
    给图片或视频打文本水印

    position传入水印位置参数:
        LeftUp : 左上
        LeftBottom : 左下
        Center : 中间
        RightUp : 右上
        RightBottom : 右下

    opacity传入水印透明度参数:
        light : 水印颜色浅
        mid : 水印颜色适中
        heavy :  水印颜色深
    '''
    try:
        # Make sure inputfile exist
        if not os.path.exists(input_path):
            logger.error(input_path + ' ERROR:Input not exists')
            return {"status": 1, "msg": 'ERROR:Input not exists', "data": "", "result": 0}

        # Make sure output path exists
        if not os.path.exists(os.path.dirname(output_path)):
            os.makedirs(os.path.dirname(output_path))

        text_position = watermark_position.text_position(position)
        text_opacity = watermark_opacity.text_opacity(opacity)

        # cmd = 'ffmpeg -y -i {0} -b 2000k -vf drawtext=fontfile="simsun.ttc":text="{1}":fix_bounds=true:fontcolor=white@{2}:fontsize=96:{3} {4}'.format(input_path, watermark_text, text_opacity, text_position, output_path)
        cmd = '''ffmpeg -y -i {0} -b:v 2000k -vf 'drawtext=fontfile="/home/chendezhi/zhaojianwei/soovii_watermark/main_watermark/simsun.ttc":text="{1}":fix_bounds=true:fontcolor=white@{2}:fontsize=96:{3}' {4}'''.format(input_path, watermark_text, text_opacity, text_position, output_path)
        print (cmd)
        print('-'*80)
        status = os.system(cmd)

        if status == 0:
            return {"status": 1, "msg": 'success', "data": "", "result": 1}
        else:
            logger.error(input_path + ' watermark fail')
            return {"status": 1, "msg": 'fail', "data": "", "result": 0}

    except Exception as e:
        logger.error(input_path + ' watermark fail:' + str(e.args))
        return {"status": 1, "msg": e.args, "data": "", "result": 0}

def create_watermark(text):
    """
    创建PDF水印模板
    """
    # 使用reportlab来创建一个PDF文件来作为一个水印文件
    currentpath = os.path.dirname(__file__)
    temppath = os.path.dirname(currentpath)
    tempfilepath = os.path.join(temppath, 'temp', 'watermark.pdf')
    print('tempfilepath:',tempfilepath)

    c = canvas.Canvas(tempfilepath)
    # 设置字体和大小
    c.setFont('song', 60)
    # 水印文字颜色
    c.setFillColorRGB(0,0,0)
    # 水印透明度
    c.setFillAlpha(0.3)
    # 水印文字位置和内容
    c.drawCentredString(300, 450, text)
    # 旋转文字
    # c.rotate(45)
    # c.translate(300, 15)
    # 保存水印文件
    c.save()

    pdf_watermark = PdfFileReader(open(tempfilepath, 'rb'))
    return pdf_watermark



def pdf_watermark_by_text(input_path, watermark_text, output_path):
    '''
    给指定PDF文件文件加上水印
    '''
    try:
        # Make sure inputfile exist
        if not os.path.exists(input_path):
            logger.error(input_path + ' ERROR:Input not exists')
            return {"status": 1, "msg": 'ERROR:Input not exists', "data": "", "result": 0}

        # Make sure output path exists
        if not os.path.exists(os.path.dirname(output_path)):
            os.makedirs(os.path.dirname(output_path))

        pdf_output = PdfFileWriter()
        with open(input_path, 'rb') as input_stream:
        # input_stream = file(input_path, 'rb')
            pdf_input = PdfFileReader(input_stream)

            # PDF文件被加密了
            # if pdf_input.getIsEncrypted():
            # print '该PDF文件被加密了.'
            # # 尝试用空密码解密
            # try:
            #     pdf_input.decrypt('')
            # except Exception, e:
            #     print '尝试用空密码解密失败.'
            #     return False
            # else:
            #     print '用空密码解密成功.'

            # 获取PDF文件的页数
            pageNum = pdf_input.getNumPages()
            pdf_watermark = create_watermark(watermark_text)
            # 给每一页打水印
            for i in range(pageNum):
                page = pdf_input.getPage(i)
                page.mergePage(pdf_watermark.getPage(0))
                pdf_output.addPage(page)

            # 最后输出文件
            output_stream = open(output_path, 'wb')
            pdf_output.write(output_stream)
            output_stream.close()

            return {"status": 1, "msg": 'success', "data": "", "result": 1}

    except Exception as e:
        logger.error(input_path + ' watermark fail:' + str(e.args))
        return {"status": 1, "msg": e.args, "data": "", "result": 0}
