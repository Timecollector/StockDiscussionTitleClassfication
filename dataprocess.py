import numpy as np
import pandas as pd
import re
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

stop_words = pd.read_csv('百度停用词列表.txt',encoding='gb18030',header=None).values

def text_process(data):
    data = data.lower()
    data = re.sub(r"\$.*?\$",'',data)
    data = re.sub(r"//@.*?:", '', data)
    clear_list = '[，,。,.,？,！,【,】,(,),（,）,、,%,@,/,$,-,:,：,《,》,<,>,…]'
    data = re.sub(clear_list, "", data)
    data = re.sub(r"\[.*?\]", '', data)
    data = re.sub(r"【.*?】", '', data)
    data = re.sub("\d+",'',data)
    clear_list1 = '[腾讯, 宁德, 宁德时代, 九安, 九安医疗, 医疗, 港股, 招商, 招商银行, 时代, 三一, 三一重工, 明天, 都]'
    data = re.sub(clear_list1, "", data)
    data = data.strip()
    data = list(jieba.cut(data,cut_all=False))
    data = [word.strip() for word in data if word not in stop_words]
    return data

data_positive = pd.read_csv(r'C:\Users\ZhangYiFan\PycharmProjects\StockNewsTitleClassfication\data\+1\positive.csv',
                   encoding='gb18030',header=None).iloc[:,0]
data_positive = data_positive.apply(text_process)
print(data_positive.head())

data_negative = pd.read_csv(r'C:\Users\ZhangYiFan\PycharmProjects\StockNewsTitleClassfication\data\-1\negative.csv',
                   encoding='gb18030',header=None).iloc[:,0]
data_negative = data_negative.apply(text_process)
print(data_negative.head())

# 画词云
plt.figure(figsize=(16, 10))
plt.subplot(1, 2, 1)
wordc = WordCloud(margin=5, width=1800, height=1000, max_words=500, min_font_size=5, background_color='white',
                  max_font_size=250,font_path='simhei.ttf')
# 把所有词转化为用空格连接
data_positive_c = " ".join(np.concatenate(data_positive.values))
wordc.generate_from_text(data_positive_c)
plt.imshow(wordc)
plt.title('Positive')
plt.subplot(1, 2, 2)
# 要设置字体，不然不显示中文
wordc = WordCloud(margin=5, width=1800, height=1000, max_words=500, min_font_size=5, background_color='white',
                  max_font_size=250,font_path='simhei.ttf')
data_negative_c = " ".join(np.concatenate(data_negative.values))
wordc.generate_from_text(data_negative_c)
plt.imshow(wordc)
plt.title('Negative')
plt.show()