import requests
from lxml import etree
from bs4 import BeautifulSoup
from sqlalchemy import Column, String, create_engine, Integer, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


#
class Book(Base):
    __tablename__  = 'b_data'
    id = Column(Integer, primary_key=True, comment='主键ID')
    img_name = Column(String(50), comment="书封面")
    book_name = Column(String(50), comment='书名')
    author = Column(String(50), comment='作者名')
    book_type = Column(String(50), comment='小说类型')
    book_byte = Column(String(255), comment='小说字数')
    brief_introduction = Column(String(255), comment='小说简介')
    books_text = relationship('Book_text', backref='b_data')
    def __repr__(self):
        return self.book_name

class Book_text(Base):
    __tablename__ = 'b_text'
    id = Column(Integer(), primary_key=True, comment='主键ID')
    book_chapter = Column(String(50), comment='章节名')
    chapter_text = Column(Text(), comment='章节内容')
    book_data_id = Column(Integer,ForeignKey('b_data.id'))


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}


def get_request(url):

    page_text = requests.get(url=url, headers=headers)
    page_text.encoding = 'GBK'
    page_text = page_text.text
    return page_text


# 数据操作
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/books', echo=True)
# 创建一个会话
Session = sessionmaker(bind=engine)
# 创建session对象:
session = Session()

def main():
    url_home = 'https://www.96biquge.com/book/1/1064/1735314.html'
    # url_home = 'https://www.96biquge.com/book/1/1064/'
    while True:
        page = get_request(url_home)
        # print(page.replace('<br>', '\n'))

        # print(page)
        tree = etree.HTML(page)
        soup = BeautifulSoup(page, 'lxml')
        try:

            book_txt = tree.xpath('//*[@id="content"]//text()')
            aaa = ''
            for i in book_txt:
                aaa += i+'<br/><br/>'
            print(aaa)
            # print(soup.select('#content')[0])
            tag = soup.select('#content')[0].text
            # print(tag)
            book_name = soup.select('.bookname h1')[0].string
            print(book_name)
            url_home = 'https://www.96biquge.com' + soup.select('#wrapper > div.content_read > div > div.bottem2 > a:nth-child(4)')[0]['href']
            new_page = Book_text(book_chapter=book_name, chapter_text=str(book_txt),book_data_id=1)
            # 添加到session:
            session.add(new_page)
            # 提交即保存到数据库:
            session.commit()
            # 关闭session:
            session.close()

            with open('qwq.txt','a+',encoding='utf-8') as f:
                f.write(book_name+'\n'+aaa+'\n')

            print(url_home)
        except:
            print('全书已经爬去完毕！')
            break
main()

# print(content_text)
# print(content_text.text)



# 创建一个会话
# Session = sessionmaker(bind=engine)
# 创建session对象:
# session = Session()
# 创建新User对象:
# new_user = User(id='5', name='Bob')
# 添加到session:
# session.add(new_user)
# 提交即保存到数据库:
# session.commit()
# 关闭session:
# session.close()

# book_chapter = Column(String(50), comment='章节名')
# chapter_text = Column(Text(), comment='章节内容')
# book_data_id = Column(Integer, ForeignKey('b_data.id'))

aaa = """
 修仙有八个境界：灵引、仙根、神基、天命、涅槃、羽化、圣灵、仙班。

    前三个境界，都只是“筑基“的境界，分为：

    灵引初期，灵引中期，灵引巅峰。

    仙根初期，仙根中期，仙根巅峰。

    神基初期，神基中期，神基巅峰。

    之所以将这前三个境界来，那是因为它们都只分为三个小境界，而且这也是一个从凡人到修仙者过渡的过程，算是脱去凡胎的三个阶段。

    三个大境界，加起来九个小境界。

    而从“天命”开始，才算是真正的进入了神秘莫测的仙道路，每一个境界的实力相差极大，而且伴随着修为的提高，人的寿命都会跟着提高。

    能够达到天命的境界，寿命一般都能活数百岁，在普通人的眼中就好像神仙一般。

    也正是因为境界跨度太大，所以从第四个境界“天命”开始，每一个境界都分为九重。

    第四个境界，天命九重。

    第五个境界，涅槃九重。

    第六个境界，羽化九重。

    第七个境界，圣灵九重。

    第八个境界，仙班九重。

    ……

    仙班后面的境界暂时不公布！
"""
# new_page = Book_text(book_chapter='境界划分', chapter_text=aaa,book_data_id=1)
# # 添加到session:
# session.add(new_page)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()

# a = session.query(Book_text).get(1)

# print(a.chapter_text)
