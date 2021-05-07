# coding: utf-8
import re

import requests
from bs4 import BeautifulSoup
from lxml import etree
import lxml
headers = {

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_40639e2e855ad00c65304ee021f07859=1619532565,1619573478,1619577941; Hm_lpvt_40639e2e855ad00c65304ee021f07859=1619577941',
    'Host': 'www.ddxstxt8.com ',
    'Referer': 'https://www.ddxstxt8.com/5_2082/',
    'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90" ',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
# pagSec-Fetch-Mode: navigatee = requests.get(url='https://www.ddxstxt8.com/5_2082/',headers=headers)
# pagSec-Fetch-Site: same-origine.encoding = 'GBK'
# pagSec-Fetch-User: ?1e_text = page.text
# priUpgrade-Insecure-Requests: 1nt(page_text)

url_z = 'https://www.ddxstxt8.com/5_2082/44219013.html'



headers1 = {
    'Cookie': 'Hm_lvt_40639e2e855ad00c65304ee021f07859=1619532565,1619573478,1619577941; Hm_lpvt_40639e2e855ad00c65304ee021f07859=1619577941',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
# print('/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“行！”麻子脸是能拿到点儿钱是点儿，于是直接同意了下来：“你给我三万吧，然后你去领奖！”<br /><br /><script>chaptererror();')
page = requests.get(url=url_z, headers=headers1)
page.encoding = 'GBK'
page_text = page.text
# print(page_text)


# BeautifulSoup  未知 bug 文本显示不完整  可能是pycharm的问题
soup = BeautifulSoup(page_text,'lxml')
print(soup.text)


# 解决

with open('qwq.html','w',encoding='utf-8') as f:
    f.write(page_text)
with open('qwq.html','r',encoding='utf-8') as f1:
    page_text = f1.read()
soup = BeautifulSoup(page_text,'lxml')
print(soup.text)



print('**********************')
tree = etree.HTML(page_text)
print(tree.xpath('//div[@id="content"]//text()'))





