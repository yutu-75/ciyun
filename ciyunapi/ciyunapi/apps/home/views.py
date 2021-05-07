# coding: utf-8
import json
import uuid
import jieba
import jieba.posseg
from django.shortcuts import render, HttpResponse, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from ciyunapi.utils.config import font1, img_template
from collections import Counter
from imageio import imread
from django.http import StreamingHttpResponse
# from rest_framework.viewsets import ModelViewSet
# from jsonrpc import jsonrpc_method
# from ciyunapi.utils.participle import makeImage
# Create your views here.

# 词云依赖
import re
import multidict as multidict
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import numpy as np
from PIL import Image


def file_down(request, p_name):
    """
    下载文件
    :param request:
    :param p_name: 图片名称
    :return:
    """
    print(p_name)
    file_path = r'./ciyunapi/static/img_ciyun/{}'.format(p_name)
    print(file_path)

    def file_iterator(file_path, chunk_size=512):
        """
        文件生成器,防止文件过大，导致内存溢出
        :param file_path: 文件绝对路径
        :param chunk_size: 块大小
        :return: 生成器
        """
        with open(file_path, mode='rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    try:
        # 设置响应头
        # StreamingHttpResponse将文件内容进行流式传输，数据量大可以用这个方法
        response = StreamingHttpResponse(file_iterator('./ciyunapi/static/img_ciyun/{}'.format(p_name)))
        # 以流的形式下载文件,这样可以实现任意格式的文件下载
        response['Content-Type'] = 'application/octet-stream'
        # Content-Disposition就是当用户想把请求所得的内容存为一个文件的时候提供一个默认的文件名
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(p_name)
        return response
    except:
        return HttpResponse("Sorry but Not Found the File!!!,没有找到此图片！！！")


class UpdateView(APIView):

    def get(self, request):
        # data = request.data

        data = request.data

        return HttpResponse(json.dumps('no get!!!', ensure_ascii=False))

    def post(self, request):

        data = request.data  # 获取文本数据

        if "data_text" not in data:
            data_json = {
                "error_code": 1003,
                "data": {
                    'error_text': "没有data_text键名！"
                }
            }
            return HttpResponse(json.dumps(data_json, ensure_ascii=False))
        # 需要的参数名
        parameter_list = [
            'b_color',
            'prefer_horizontal',
            'contour_width',
            'contour_color',
            'margin',
            'font_str',
            'img_name'
        ]

        # 接收的参数名
        receive_list = data.keys()

        # 处理不需要的参数名
        data_dict = {i: data[i] for i in receive_list if i in parameter_list}

        data1 = jieba.posseg.cut(data['data_text'])  # 进行分词

        data_text_list = [list(k) for k in dict(data1).items() if 'x' not in list(k)]  # 生产列表 踢出字符 ['休眠', 'v', 1],
        print(data_text_list)
        if not data_text_list:
            data_json = {
                "error_code": 1001,
                "data": {
                    'error_text': "文本为空或者没有中文字符！"
                }
            }
            return HttpResponse(json.dumps(data_json, ensure_ascii=False))
        # 把用户按照格式输入的文本处理成字典
        d = data['data_text']
        d = d.replace('，', ',')

        d_list = d.split('\n')
        # print(d_list)
        try:
            dict_text = {i.split(',')[0]: int(i.split(',')[1]) for i in d_list if i}
            # print(dict_text)
        except:
            data_json = {
                "error_code": 1002,
                "data": {
                    'error_text': "没有按照指定格式进行输入！！！"
                }
            }
            return HttpResponse(json.dumps(data_json, ensure_ascii=False))


        photo_name = str(uuid.uuid1()).upper().replace('-', '')  # 生成图片名字

        from mycelery.ciyun_img.tasks import ciyun

        d_keys = data_dict.keys()

        if 'b_color' in d_keys:
            b_color = data_dict['b_color']
        else:
            b_color = None
        if 'prefer_horizontal' in d_keys:
            prefer_horizontal = data_dict['prefer_horizontal']
        else:
            prefer_horizontal = 0.9
        if 'contour_width' in d_keys:
            contour_width = int(data_dict['contour_width'])
        else:
            contour_width = 0

        if 'contour_color' in d_keys:
            contour_color = data_dict['contour_color']
        else:
            contour_color = 'steelblue'
        if 'margin' in d_keys:
            margin = data_dict['margin']
        else:
            margin = 2
        if 'font_str' in d_keys:
            font = data_dict['font_str']
        else:
            font = 'simkai.ttf'
        if 'img_template' in d_keys:
            img_name = r"./ciyunapi/static/img_template/{}".format(data_dict['img_name'])
        elif request.FILES.get('file'):

            req = request.FILES.get('file')
            suffix = req.name  # 获取上传图片的后缀名
            destination = open(
                "./ciyunapi/static/img_user_template/{}.{}".format(photo_name, suffix), 'wb+')
            for chunk in req.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            img_name = r"./ciyunapi/static/img_user_template/{}.{}".format(photo_name, suffix)
        else:
            img_name = r"./ciyunapi/static/img_template/11.png"

        # alice_mask = np.array(Image.open(img_name))
        alice_mask = imread(img_name)

        font_w = r'./ciyunapi/static/font/{}'.format(font)

        if b_color is not None or 'contour_width' in d_keys:
            mode = 'RGB'
        else:
            mode = "RGBA"

        wc = WordCloud(
            background_color=b_color,
            prefer_horizontal=prefer_horizontal,
            font_path=font_w,
            max_words=1000,
            mask=alice_mask,
            contour_width=contour_width,
            margin=margin,
            contour_color=contour_color,
            mode=mode,
            # font_step=10,
        )
        # generate word cloud
        wc.generate_from_frequencies(dict_text)
        try:
            wc.to_file(r"./ciyunapi/static/img_ciyun/{}.png".format(photo_name))

        except:
            return Response('参数传错！')

        data_json = {
            "error_code": 1000,
            "data": {
                "photo_url": "statics/img_ciyun/{}.png".format(photo_name),
                "font": font1,
                "data_text_list": data_text_list,
                "img_template": img_template,
                # "reg_time": "1436864169",
                # "last_login_time": "0",
            }
        }
        return Response(json.dumps(data_json, ensure_ascii=False))


class CiyunView(APIView):

    def get(self, request):
        # data = request.data

        return HttpResponse(json.dumps('no get!!!', ensure_ascii=False))

    def post(self, request):

        data = request.data  # 获取文本数据

        if "data_text" not in data:
            data_json = {
                "error_code": 1003,
                "data": {
                    'error_text': "没有data_text键名！"
                }
            }
            return HttpResponse(json.dumps(data_json, ensure_ascii=False))
        # 需要的参数名
        parameter_list = [
            'b_color',
            'prefer_horizontal',
            'contour_width',
            'contour_color',
            'margin',
            'font_str',
            'img_name'
        ]

        # 接收的参数名
        receive_list = data.keys()

        # 处理不需要的参数名
        data_dict = {i: data[i] for i in receive_list if i in parameter_list}
        print(data_dict, '************')
        # return Response('ok')

        print(data['data_text'])

        data = jieba.posseg.cut(data['data_text'])  # 进行分词

        data = dict(Counter(data))  # 分词统计

        data_text_list = [list(k) + [v] for k, v in data.items() if 'x' not in list(k)]  # 生产列表 踢出字符 ['休眠', 'v', 1],

        if not data_text_list:
            data_json = {
                "error_code": 1001,
                "data": {
                    'error_text': "文本为空或者没有中文字符！"
                }
            }
            return HttpResponse(json.dumps(data_json, ensure_ascii=False))
        dict_text = {list(k)[0]: int(v) for k, v in data.items() if 'x' not in list(k)}  # 生成字典  踢出字符
        print(dict_text)
        photo_name = str(uuid.uuid1()).upper().replace('-', '')  # 生成图片名字

        from mycelery.ciyun_img.tasks import ciyun

        d_keys = data_dict.keys()

        if 'b_color' in d_keys:
            b_color = data_dict['b_color']
        else:
            b_color = None
        if 'prefer_horizontal' in d_keys:
            prefer_horizontal = data_dict['prefer_horizontal']
        else:
            prefer_horizontal = 0.9
        if 'contour_width' in d_keys:
            contour_width = data_dict['contour_width']
        else:
            contour_width = 0
        if 'contour_color' in d_keys:
            contour_color = data_dict['contour_color']
        else:
            contour_color = 'steelblue'
        if 'margin' in d_keys:
            margin = data_dict['margin']
        else:
            margin = 2
        if 'font_str' in d_keys:
            font = data_dict['font_str']
        else:
            font = 'simkai.ttf'
        if 'img_template' in d_keys:
            img_name = r"./ciyunapi/static/img_template/{}".format(data_dict['img_name'])
        elif request.FILES.get('file'):

            req = request.FILES.get('file')
            suffix = req.name  # 获取上传图片的后缀名
            destination = open(
                "./ciyunapi/static/img_user_template/{}.{}".format(photo_name, suffix), 'wb+')
            for chunk in req.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            img_name = r"./ciyunapi/static/img_user_template/{}.{}".format(photo_name, suffix)
        else:
            img_name = r"./ciyunapi/static/img_template/11.png"

        # alice_mask = np.array(Image.open(img_name))
        alice_mask = imread(img_name)

        font_w = r'./ciyunapi/static/font/{}'.format(font)
        font1 = [
            'msyh.ttc',  # 微软雅黑 常规
            'msyhbd.ttc',  # 微软雅黑 粗体
            'simfang.ttf',  # 仿宋
            'simkai.ttf',  # 楷体
            'STCAIYUN.TTF',  # 华文彩云
            'msjh.ttc',  # 繁体
            'FZSTK.TTF',  # 方正舒体
            'BRUSHSCI.TTF',  # 英文斜体
            'STXINGKA.TTF',  # 华文行楷
            'STHUPO.TTF',  # 华文琥珀

        ]

        if b_color is not None or 'contour_width' in d_keys:
            mode = 'RGB'
        else:
            mode = "RGBA"

        wc = WordCloud(
            background_color=b_color,
            prefer_horizontal=prefer_horizontal,
            font_path=font_w,
            max_words=1000,
            mask=alice_mask,
            contour_width=contour_width,
            margin=margin,
            contour_color=contour_color,
            mode=mode,
            # font_step=10,

        )
        # generate word cloud
        wc.generate_from_frequencies(dict_text)
        wc.to_file(r"./ciyunapi/static/img_ciyun/{}.png".format(photo_name))

        # show
        # plt.imshow(wc, interpolation="bilinear")
        # plt.axis("off")
        # plt.show()

        data_json = {
            "error_code": 1000,
            "data": {
                "photo_url": "statics/img_ciyun/{}.png".format(photo_name),
                "font": font1,
                "data_text_list": data_text_list,
                "img_template": img_template,
                # "reg_time": "1436864169",
                # "last_login_time": "0",
            }
        }

        # 弃用  原因 ：异步同时调用同一张模板图书时 无法异步处理同一张图片
        # a = ciyun.delay(
        #     photo_name,
        #     dict_text,
        #     b_color,
        #     prefer_horizontal,
        #     # contour_width,
        #     # contour_color,
        #     # margin,
        #     # font,
        #     # img_name,
        # )          # celery异步处理

        # from celery.result import AsyncResult
        # #
        # async_task = AsyncResult(id=a.id, app=ciyun)
        # result = async_task.get()
        # print('xxxxxxxxxx>>>',result)  #xxxxxxxxxx>>> 短信发送成功啦
        # print(a, type(a))
        # res = AsyncResult(str(a))
        #
        # print(a)
        # print(res.result)
        # a = makeImage(data_text, prefer_horizontal=0.9)
        # print(data_text)

        return Response(json.dumps(data_json, ensure_ascii=False))


