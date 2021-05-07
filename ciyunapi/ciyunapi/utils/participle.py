# coding: utf-8

import jieba

string = """

数据的价值是提升业务而不仅仅是用户画像 
2016年客户开始拥抱大数据，引入外部数据成为热点，市场上出现了各类数据提供商。运营商数据、航旅数据、银联数据、电商数据、物流数据等数据源已经形成数据热点。企业疯狂地追寻外部数据源，引入外部数据成了大数据战略一个重点，外部数据成为企业数据应用的主题，客户画像成为数据应用的主要议题。 
数据的应用场景可分为三类，一个是提升业务，一个是降低运营成本，另外一个是精细化运营。用户画像仅仅是数据应用的一个过程，不是数据应用的目的。企业客户知道了用户的个人属性、兴趣爱好，消费偏好，行为标签等信息，丰富了企业对客户的了解，了解了过去不知道到信息。 




仅仅是数据应用的一个过程，离企业的业务需求还有较大的距离。数据应用需要解决的不仅仅是让企业重新认识客户(用户画像



)，还需要解决从数据到商业决策最后一公里的问题。数据应用的目的是提升业务，帮助企业以较低的成本和较好的客户体验，实现精准营销，提升业务收入。 
金融客户拥有较为丰富的个人属性数据、资产数据、信用数据、交易数据。缺少客户在本金融企业之外的金融数据和个人行为数据。大的银行、券商、保险开始对外引入和购买客户的外部行为数据和金融数据，用于丰富标签和用户画像，但是具体如何应用这些标签数据，如何衡量数据价值，如何寻找数据应用场景，都在探索之中。其实金融企业内部的人也不太清楚，也没有一个系统的方式方法去寻找数据应用场景，大家都在摸索中。 
市场上最好的数据是运营商数据和银联数据，运营商数据利用DPI技术分析出客户网上行为，为客户打上一些行为标签，例如客户喜欢看的手机品牌、3C产品，客户点击浏览的电商产品，客户浏览的出国、留学、旅游、房产、汽车等网站或网页。 
目前电信的DPI标签集中在客户固网访问行为，也就是在PC上的浏览标签，联通的DPI标签集中在移动互联网的访问行为行为和标签，中国移动的DPI标签还在挖掘开发中。移动、电信、联通覆盖的移动互联网用户比例分别为6:2:2，中国移动占了大部分，客户质量较高。另外可以提供移动互联网访问行为表标签的数据厂商是TakingData、极推、个推等第三方数据服务商。 
银联的数据集中在刷卡的消费和支出的分级信息，以卡、POS为单位，可以用于风控和信用评估，具体个人的刷卡信息不能提供。 短信服务商可以利用短信来加工一些客户的收入、转账、消费、分期、贷款等信息。误差比较大，无法全面揭示客户收入、资产、消费信息，仅仅可以作为参考。市场上还有一些公司可以提供航旅信息，例如飞行次数、公里、总金额、头等舱次数、经济舱次数，平均票价等。这些信息具有强相关的金融消费属性，容易应用。 
外部行为标签的确给金融企业带来了新的信息源，但是如何使用这些标签来推动业务，来实现精准营销，帮助金融企业销售产品，大家还在探索中。目前这些标签主要用于用户画像，业务人员对这些数据标签的价值也持观望态度，不愿意主动实践。即使是小范围实践，如果一旦效果出现波动，业务人员会有放大这个结果，怀疑数据的价值。 
数据在金融企业的应用很曲折，数据部门同业务部门在数据应用效果和场景应用需要长时间磨合。有的保险企业数据部门即使将整理好的潜在客户名单发给业务部门，业务部门也不相信，也不会打电话去尝试。有的证券企业，即使外呼效果已经比原来盲呼效果好了十倍，但是没有达到业务部门的期望(追求20%以上的转化率)，业务部门也会以影响客户体验为理由，拒绝进一步的数据尝试。 银行也遇到同样的问题，外部行为数据标签如何应用是一个难题，数据应用方式和数据应效果如何衡量也是一个问题。如果数据应用效果好，业绩是数据部门的还是业务部门的?业务提升是产品原因还是数据原因?外呼的价值高还是短信的价值高



?这些都是数据价值应用的坑，需要花时间去填上。 
一、第一方数据是金矿，先从分析第一方数据开始 
从经验上来讲，金融行业活跃的客户在40%，有的企业可能更低。活跃客户没有明确的定义，一般以月度发生过一次交易/查询以上的客户定义为活跃客户。金融企业的僵尸客户，可以定义为是一年业务之内没有同金融企业发生过任何交易的客户，一般在30%左右，这里面也包含了羊毛党客户。另外的30%客户可以定义为休眠/不活跃客户，这些客户一年之内偶而会同金融企业进行交易，包括产品购买和支付等。


"""
import jieba.posseg
from pathlib import Path
from collections import Counter
a = jieba.posseg.cut(string)


# for k,v in a:
#     print(k,"\t\t",v)


data1 = jieba.posseg.cut(string)
data = dict(Counter(data1))



aaa = {
    "sdsa":1,
    "asd":1,
    '萨达萨达':22,

 }
# data_text = [list(k)+[v] for k, v in data.items() if 'x' not in list(k)]


import multidict as multidict

import numpy as np

import os
import re
from PIL import Image
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def getFrequencyDictForText(sentence):
    fullTermsDict = multidict.MultiDict()
    tmpDict = {}

    # making dict for counting frequencies
    for text in sentence.split(" "):
        if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be", text):
            continue
        val = tmpDict.get(text, 0)
        tmpDict[text.lower()] = val + 1
    for key in tmpDict:
        fullTermsDict.add(key, tmpDict[key])
    return fullTermsDict


def makeImage11(photo_name,text, data_dict=None):
    data_dict = eval(data_dict)
    print(data_dict)

    b_color = None
    prefer_horizontal = 0.9
    contour_width = 0
    contour_color = 'steelblue'
    margin = 2
    mode = "RGBA"
    d_keys = data_dict.keys()

    parameter_list = ['b_color', 'prefer_horizontal', 'contour_width', 'contour_color', 'margin', 'img_name', 'font_str']
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
        img_name = data_dict['img_name']
    else:
        img_name = '11.png'



  # [              b_color=None, prefer_horizontal=0.9, contour_width=0, contour_color='steelblue', margin=2, mode="RGBA"]
    # print("获取当前文件路径——" + os.path.realpath(__file__))
    # print(Path.cwd())      # 当前目录的路径对象
    import sys
    # os.chdir(sys.path[0])
    print(font)

    alice_mask = np.array(Image.open(r"./ciyunapi/static/img_template/{}".format(img_name)))

    font_w = r'./ciyunapi/static/font/{}'.format(font)
    font1 = [
        'msyh.ttc',         # 微软雅黑 常规
        'msyhbd.ttc',       # 微软雅黑 粗体
        'simfang.ttf',      # 仿宋
        'simkai.ttf',       # 楷体
        'STCAIYUN.TTF',     # 华文彩云
        'msjh.ttc',         # 繁体
        'FZSTK.TTF',        # 方正舒体
        'BRUSHSCI.TTF',     # 英文斜体
        'STXINGKA.TTF',     # 华文行楷
        'STHUPO.TTF',       # 华文琥珀

    ]
    print(prefer_horizontal)
    if b_color is not None:
        mode = 'RGB'


    print("***************")
    print(data_dict)
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
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    return 'ok!!!!'






c_color = ''
prefer_horizontal = 0.8         # 小于等于 垂直水平都有  大于0.9 水平显示
contour_width = 0.8
contour_color = 'steelblue'
margin = 2




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
# makeImage(prefer_horizontal=0.9)



