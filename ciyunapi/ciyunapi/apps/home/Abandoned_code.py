from datetime import datetime
import asyncio, os, time, json
from django.shortcuts import render, HttpResponse, redirect
from jsonrpc import jsonrpc_method
from rest_framework.viewsets import ModelViewSet
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


async def http_call_async(requests):
    # for i in range(100):
    #     print(i)

    a = datetime.now()
    await asyncio.sleep(3)
    b = datetime.now()

    return HttpResponse('ok   第一次请求视图的时间%s  ----- \n执行完任务后时间%s  ' % (a, b))


def modify(request):
    if request.method != 'POST':
        return HttpResponse(json.dumps({'error': '请求方法错误！'}, ensure_ascii=False))
    else:
        return HttpResponse(json.dumps('ok', ensure_ascii=False))


def ay(requests):
    a = datetime.now()
    time.sleep(10)
    b = datetime.now()

    return HttpResponse('ok   第一次请求视图的时间%s  ----- \n执行完任务后时间%s  ' % (a, b))


@jsonrpc_method('home.qwq')
def home_qwq():
    return {"qwq": '111'}


# class UserInfoView(ModelViewSet):


"""
        下载压缩文件
        :param request:
        :param id: 数据库id
        :return:
"""
data = [{"id": "1", "image": "animation.jpg"}]  # 模拟mysql表数据
file_name = data['name']

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
file_path = os.path.join(base_dir, 'upload', 'images', file_name)  # 下载文件的绝对路径

# if not os.path.isfile(file_path):  # 判断下载文件是否存在
#     return HttpResponse("Sorry but Not Found the File")

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

# try:
    # 设置响应头
    # StreamingHttpResponse将文件内容进行流式传输，数据量大可以用这个方法
    # response = StreamingHttpResponse(file_iterator("statics/img_ciyun/{}".format(file_name)))
    # 以流的形式下载文件,这样可以实现任意格式的文件下载
    # response['Content-Type'] = 'application/octet-stream'
    # # Content-Disposition就是当用户想把请求所得的内容存为一个文件的时候提供一个默认的文件名
    # response['Content-Disposition'] = 'attachment;filename="{}"'.format(file_name)
# except:
#     return HttpResponse("Sorry but Not Found the File")
# return response