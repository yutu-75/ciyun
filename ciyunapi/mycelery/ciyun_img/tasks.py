from mycelery.main import app
# from ciyunapi.utils.participle import makeImage
# from luffyapi.settings import constants
import logging
import multidict as multidict
import numpy as np
import os
import re
from PIL import Image
from os import path
from wordcloud import WordCloud
# import matplotlib.pyplot as plt

log = logging.getLogger("django")



# def ciyun(photo_name,text,data_dict):
@app.task(name="ciyun")
def ciyun(
            photo_name,
            text,
            b_color,
            prefer_horizontal,

            mode="RGBA"
        ):
    contour_width = 0,
    contour_color = 'steelblue',
    margin = 2,
    font = 'simkai.ttf',
    img_name = '11.png',
    print(font)

    alice_mask = np.array(Image.open(r"./ciyunapi/static/img_template/{}".format(img_name)))

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
    print(prefer_horizontal)
    if b_color is not None:
        mode = 'RGB'

    print("***************")

    print(text)
    print(b_color)
    print(mode)
    print("***************")
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
    wc.generate_from_frequencies(text)
    wc.to_file(r"./ciyunapi/static/img_ciyun/{}.png".format(photo_name))

    # show
    # plt.imshow(wc, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()
    return 'ok!!!!'



#
# parameter_list = ['b_color', 'prefer_horizontal', 'contour_width', 'contour_color', 'margin', 'img_name',
#                   'font_str']


# [              b_color=None, prefer_horizontal=0.9, contour_width=0, contour_color='steelblue', margin=2, mode="RGBA"]
# print("获取当前文件路径——" + os.path.realpath(__file__))
# print(Path.cwd())      # 当前目录的路径对象
import sys
# os.chdir(sys.path[0])
"""
c_color = ''
prefer_horizontal = 0.8  # 小于等于 垂直水平都有  大于0.9 水平显示
contour_width = 0.8
contour_color = 'steelblue'
margin = 2
"""
"""
text,
c_color=None,                   # 背景颜色
prefer_horizontal=0.9,          # 小于等于 词汇横竖显示都有  越小竖着显示的词越多   大于0.9 水平显示
contour_width=0,                # 轮廓大小
contour_color='steelblue',      # 轮廓颜色
margin=2,                       # 词汇边距距离
font_str='msyh.ttc              # 词汇字体显示
'
"""


