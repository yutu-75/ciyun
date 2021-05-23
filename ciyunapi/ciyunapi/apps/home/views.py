# coding: utf-8
import os
import json
import uuid
import jieba
import jieba.posseg
import os.path
import random
from django.shortcuts import render, HttpResponse, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from . import models
from ciyunapi.settings import contains
from ciyunapi.utils.config import font1, img_template
from collections import Counter
from imageio import imread
from django.http import StreamingHttpResponse
from .serializers import BannerModelSerializer, NavModelSerializer, BottomModelSerializer

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


# def file_upload(request):
#     """
#     上传文件文件
#     :param request:
#     :param p_name: 图片名称
#     :return:
#     """
#     print(request.FILES.get('file'))
#     return HttpResponse('ok!!!')
#     photo_name = str(uuid.uuid1()).upper().replace('-', '')  # 生成图片名字
#     req = request.FILES.get('file')
#     suffix = req.name  # 获取上传图片的后缀名
#     destination = open(
#         "./ciyunapi/static/img_user_template/{}.{}".format(photo_name, suffix), 'wb+')
#     for chunk in req.chunks():  # 分块写入文件
#         destination.write(chunk)
#     destination.close()
#     img_name = r"./ciyunapi/static/img_user_template/{}.{}".format(photo_name, suffix)
#     return HttpResponse("Sorry but Not Found the File!!!,没有找到此图片！！！")

class UploadView(APIView):

    def get(self, request):
        # data = request.data

        data = request.data

        return HttpResponse(json.dumps('no get!!!', ensure_ascii=False))

    def post(self, request):
        """
        上传文件文件
        :param request:
        :param p_name: 图片名称
        :return:
        """
        print(request.FILES.get('file'))
        # return HttpResponse('ok!!!')
        photo_name = str(uuid.uuid1()).upper().replace('-', '')  # 生成图片名字
        req = request.FILES.get('file')
        if req:
            suffix = str(req.name).split('.')[1]  # 获取上传图片的后缀名
        else:
            data_json = {
                "error_code": 1004,
                "data": {
                    'error': "没有上传图片,或者字段名填写错误！"
                }
            }
            return Response(data_json)

        destination = open(
            "./ciyunapi/static/img_user_template/{}.{}".format(photo_name, suffix), 'wb+')
        for chunk in req.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        # img_name = r"./ciyunapi/static/img_user_template/{}.{}".format(photo_name, suffix)

        data_json = {
            "error_code": 1000,
            "data": {
                'img_name': "{}.{}".format(photo_name, suffix)
            }
        }
        return Response(data_json)

        return Response('ok')


class TemplateView(APIView):
    def get(self, request):
        # data = request.data

        data = request.data

        return HttpResponse(json.dumps('no get!!!', ensure_ascii=False))

    def post(self, request):
        data = request.data  # 获取文本数据


        img_list = os.listdir('./ciyunapi/static/img_template')
        print(img_list)

        data_json = {
            "error_code": 1000,
            "data": {
                'img_list': img_list,
            }
        }
        return HttpResponse(json.dumps(data_json, ensure_ascii=False))


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
            'img_name',
            'byte_color',
            'user_img_name',
        ]

        # 接收的参数名
        receive_list = data.keys()

        # 处理不需要的参数名
        data_dict = {i: data[i] for i in receive_list if i in parameter_list}

        data1 = jieba.posseg.cut(data['data_text'])  # 进行分词

        data_text_list = [list(k) for k in dict(data1).items() if 'x' not in list(k)]  # 生产列表 踢出字符 ['休眠', 'v', 1],
        # print(data_text_list)
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
            print(dict_text)
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
            if data_dict['b_color'] == '0':
                b_color = None
            else:
                b_color = data_dict['b_color']
        else:
            b_color = None
        # print('qwq')
        if 'prefer_horizontal' in d_keys:
            prefer_horizontal = float(data_dict['prefer_horizontal'])
        else:
            prefer_horizontal = 0.9



        if 'contour_width' in d_keys:
            if data_dict['contour_width'] == '0':
                contour_width = 0
            else:
                contour_width = int(data_dict['contour_width'])
        else:
            contour_width = 0
        # if 'contour_width' in d_keys:
        #     contour_width = int(data_dict['contour_width'])
        # else:
        #     contour_width = 0

        if 'contour_color' in d_keys:
            if data_dict['contour_color'] == '0':
                contour_color = 'steelblue'
            else:
                contour_color = data_dict['contour_color']
        else:
            contour_color = 'steelblue'

        # if 'contour_color' in d_keys:
        #     contour_color = data_dict['contour_color']
        # else:
        #     contour_color = 'steelblue'
        if 'margin' in d_keys:
            margin = int(data_dict['margin'])
        else:
            margin = 2
        if 'font_str' in d_keys:
            font = data_dict['font_str']
        else:
            font = 'simkai.ttf'
        if 'img_template' in d_keys:

            img_name = r"./ciyunapi/static/img_template/{}".format(data_dict['img_template'])
        elif request.data.get('user_img_name'):

            img_name = r"./ciyunapi/static/img_user_template/{}".format(request.data['user_img_name'])
        else:
            print(request.data)
            try:
                img_name = r"./ciyunapi/static/img_template/{}".format(request.data['img_name'])
            except:
                img_name = r"./ciyunapi/static/img_template/{}".format('11.png')

        alice_mask = np.array(Image.open(img_name))
        # alice_mask = imread(img_name)

        font_w = r'./ciyunapi/static/font/{}'.format(font)

        if b_color is not None or contour_width != 0:
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
            class SimpleGroupedColorFunc(object):
                """Create a color function object which assigns EXACT colors
                   to certain words based on the color to words mapping

                   Parameters
                   ----------
                   color_to_words : dict(str -> list(str))
                     A dictionary that maps a color to the list of words.

                   default_color : str
                     Color that will be assigned to a word that's not a member
                     of any value from color_to_words.
                """

                def __init__(self, color_to_words, default_color):
                    self.word_to_color = {word: color
                                          for (color, words) in color_to_words.items()
                                          for word in words}

                    self.default_color = default_color

                def __call__(self, word, **kwargs):
                    return self.word_to_color.get(word, self.default_color)

            color_to_words = {
                # words below will be colored with a green single color function
                '#00ff00': ['beautiful', 'explicit', 'simple', 'sparse',
                            'readability', 'rules', 'practicality',
                            'explicitly', 'one', 'now', 'easy', 'obvious', 'better'],
                # will be colored with a red single color function
                'red': ['ugly', 'implicit', 'complex', 'complicated', 'nested',
                        'dense', 'special', 'errors', 'silently', 'ambiguity',
                        'guess', 'hard']
            }
            if data_dict['byte_color'] != '0':
                default_color = data_dict['byte_color']
                grouped_color_func = SimpleGroupedColorFunc(color_to_words, default_color)
                wc.recolor(color_func=grouped_color_func)
                plt.imshow(wc, interpolation="bilinear")

            wc.to_file(r"./ciyunapi/static/img_ciyun/{}.png".format(photo_name))

        except:
            return Response('参数传错！')

        data_json = {
            "error_code": 1000,
            "data": {
                "photo_url": "{}.png".format(photo_name),
                "font": font1,
                "data_text_list": data_text_list,
                "img_template": img_template,
                # "reg_time": "1436864169",
                # "last_login_time": "0",
            }
        }
        return Response(data_json)


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
            'img_name',
            'byte_color',
            'user_img_name',
        ]

        # 接收的参数名
        receive_list = data.keys()

        # 处理不需要的参数名
        data_dict = {i: data[i] for i in receive_list if i in parameter_list}
        # print(data_dict, '************')
        # return Response('ok')

        print(data['data_text'])

        data = jieba.posseg.cut(data['data_text'])  # 进行分词
        # print(data)

        data = dict(Counter(data))  # 分词统计
        c = data

        # for k, v in data.items():
        #     print(k,v)

        data_text_list = [list(k) + [v] for k, v in data.items() if 'x' not in list(k)]  # ['休眠', 'v', 1] 产生列表 踢出字符 ,

        if not data_text_list:
            data_json = {
                "error_code": 1001,
                "data": {
                    'error_text': "文本为空或者没有中文字符！"
                }
            }
            return HttpResponse(json.dumps(data_json, ensure_ascii=False))
        dict_text = {}
        # print('**************')

        for k, v in c.items():
            # print(type(k),type(v),k,v,type(list(k)),list(k))
            k_list = list(k)
            if 'x' not in k_list:
                # print(k,v)
                if k_list[0] in dict_text.keys():
                    dict_text[k_list[0]] += v
                else:
                    dict_text[k_list[0]] = v
                # print(dict_text)
        # print(dict_text)
        # print('**************')

        # dict_text = {list(k)[0]: int(v) for k, v in data.items() if 'x' not in list(k)}  # 生成字典  踢出字符
        # print(dict_text)
        str_a = ''
        for i in dict_text.keys():
            b = i + "," +str(dict_text[i])+'\n'
            str_a += b
        # print(str_a)




        photo_name = str(uuid.uuid1()).upper().replace('-', '')  # 生成图片名字

        from mycelery.ciyun_img.tasks import ciyun

        d_keys = data_dict.keys()

        if 'b_color' in d_keys:
            if data_dict['b_color'] == '0':
                b_color = None
            else:
                b_color = data_dict['b_color']
        else:
            b_color = None
            # print('qwq')
        if 'prefer_horizontal' in d_keys:
            prefer_horizontal = float(data_dict['prefer_horizontal'])
        else:
            prefer_horizontal = 0.9

        if 'contour_width' in d_keys:
            if data_dict['contour_width'] == '0':
                contour_width = 0
            else:
                contour_width = int(data_dict['contour_width'])
        else:
            contour_width = 0
            # if 'contour_width' in d_keys:
            #     contour_width = int(data_dict['contour_width'])
            # else:
            #     contour_width = 0

        if 'contour_color' in d_keys:
            if data_dict['contour_color'] == '0':
                contour_color = 'steelblue'
            else:
                contour_color = data_dict['contour_color']
        else:
            contour_color = 'steelblue'

            # if 'contour_color' in d_keys:
            #     contour_color = data_dict['contour_color']
            # else:
            #     contour_color = 'steelblue'
        if 'margin' in d_keys:
            margin = int(data_dict['margin'])
        else:
            margin = 2
        if 'font_str' in d_keys:
            font = data_dict['font_str']
        else:
            font = 'simkai.ttf'
        if 'img_template' in d_keys:

            img_name = r"./ciyunapi/static/img_template/{}".format(data_dict['img_template'])
        elif request.data.get('user_img_name'):

            img_name = r"./ciyunapi/static/img_user_template/{}".format(request.data['user_img_name'])
        else:
            print(request.data)
            try:
                img_name = r"./ciyunapi/static/img_template/{}".format(request.data['img_name'])
            except:
                img_name = r"./ciyunapi/static/img_template/{}".format('11.png')

        alice_mask = np.array(Image.open(img_name))
        # alice_mask = imread(img_name)

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

        if b_color is not None or contour_width != 0:
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
            relative_scaling=0,
            height=800,
            width=800,
            max_font_size=80,


            # font_step=10,

        )
        # generate word cloud
        wc.generate_from_frequencies(dict_text)


        try:
            class SimpleGroupedColorFunc(object):
                """Create a color function object which assigns EXACT colors
                   to certain words based on the color to words mapping

                   Parameters
                   ----------
                   color_to_words : dict(str -> list(str))
                     A dictionary that maps a color to the list of words.

                   default_color : str
                     Color that will be assigned to a word that's not a member
                     of any value from color_to_words.
                """

                def __init__(self, color_to_words, default_color):
                    self.word_to_color = {word: color
                                          for (color, words) in color_to_words.items()
                                          for word in words}

                    self.default_color = default_color

                def __call__(self, word, **kwargs):
                    return self.word_to_color.get(word, self.default_color)

            color_to_words = {
                # words below will be colored with a green single color function
                '#00ff00': ['beautiful', 'explicit', 'simple', 'sparse',
                            'readability', 'rules', 'practicality',
                            'explicitly', 'one', 'now', 'easy', 'obvious', 'better'],
                # will be colored with a red single color function
                'red': ['ugly', 'implicit', 'complex', 'complicated', 'nested',
                        'dense', 'special', 'errors', 'silently', 'ambiguity',
                        'guess', 'hard']
            }
            if data_dict['byte_color'] != '0':
                default_color = data_dict['byte_color']
                grouped_color_func = SimpleGroupedColorFunc(color_to_words, default_color)
                wc.recolor(color_func=grouped_color_func)
                plt.imshow(wc, interpolation="bilinear")

            wc.to_file(r"./ciyunapi/static/img_ciyun/{}.png".format(photo_name))

        except:
            return Response('参数传错！')


        # wc.to_file(r"./ciyunapi/static/img_ciyun/{}.png".format(photo_name))

        # show
        # plt.imshow(wc, interpolation="bilinear")
        # plt.axis("off")
        # plt.show()

        data_json = {
            "error_code": 1000,
            "data": {
                "photo_url": "{}.png".format(photo_name),
                "font": font1,
                "data_text_list": data_text_list,
                "img_template": img_template,
                'str_a': str_a,
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

        return Response(data_json)


class BannerView(ListAPIView):
    """
    轮播图api
    """
    queryset = models.Banner.objects.filter(is_deleted=False, is_show=True)[0:contains.BANNER_LENGTH]
    serializer_class = BannerModelSerializer


class NavView(ListAPIView):
    """
    导航栏api
    """
    queryset = models.Nav.objects.filter(is_deleted=False, is_show=True, position=1)[0:contains.NAV_TOP_LENGTH]
    serializer_class = NavModelSerializer


class BottomView(ListAPIView):
    """
    导航栏api
    """
    queryset = models.Nav.objects.filter(is_deleted=False, is_show=True, position=1)[0:contains.NAV_TOP_LENGTH]
    serializer_class = BottomModelSerializer
