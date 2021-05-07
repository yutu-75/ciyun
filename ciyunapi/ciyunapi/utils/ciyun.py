from wordcloud import WordCloud
# from scipy.misc import imread
from imageio import imread
import matplotlib.pyplot as plt
import jieba


def read_deal_text():
    with open("ciyun.txt", "r", encoding='utf-8') as f:
        txt = f.read()
    re_move = ["，", "。", " ", '\n', '\xa0']
    # 去除无效数据
    for i in re_move:
        txt = txt.replace(i, ' ')
    word = jieba.lcut(txt)  # 使用精确分词模式
    word = [i for i in word if i != ' ']

    print(word)
    with open("txt_save.txt", 'w', encoding='utf-8') as file:
        for i in word:
            file.write(str(i) + ' ')
    print("文本处理完成")


def img_grearte():
    mask = imread("11.png")
    with open("txt_save.txt", "r",encoding='utf-8') as file:
        txt = file.read()
    word = WordCloud(
                    background_color="white",   # 定义背景颜色
                     width=800,
                     height=800,
                     font_path='simhei.ttf',
                     collocations=False,        # 取消关键字重复多次，需要设置collocations=False
                     mask=mask,
                    # max_words=1

                     ).generate(txt)
    word.to_file('test1.png')
    word.to_file('')

    print("词云图片已保存")

    plt.imshow(word,interpolation='bilinear')  # 使用plt库显示图片
    plt.axis("off")
    plt.show()



# read_deal_text()
# img_grearte()
