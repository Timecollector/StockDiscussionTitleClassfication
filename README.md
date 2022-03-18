## 基于股票下帖子标题的涨跌预测

当前更新了标题爬取以及数据预处理的代码，后续代码写完之后再发



### 数据收集

数据来源于东方财富网，数据以csv格式保存，**每次爬取页码不要超过100页，不然会被封ip几分钟，挂了代理当我没说**

demo：

```python
stock_number = input('请输入股票代码：')
page_start = input('请输入开始页码：')
page_end = input('请输入停止页码：')
download_stock_discussion_title(stock_number=stock_number, page_start=page_start,page_end=page_end)
```

### 数据预处理

这部分首先对收集的标题进行了处理：

- 删除了一些奇怪符号
- 删除了股票名，避免对预测产生影响
- 删除了数字以及标点符号
- 删除了空格
- 删除了表情
- 使用jieba进行分词

最后将数据可视化为词云

![image-20220318135520123](C:\Users\ZhangYiFan\AppData\Roaming\Typora\typora-user-images\image-20220318135520123.png)

后续写完神经网络训练好模型再上传剩余代码





**data文件夹中包含我之前爬取的一些股票评论，主要是九安医疗、腾讯、招商银行、三一重工等**

其中+1文件夹中的评论是第二天涨的

-1文件夹中的评论是第二天跌的

所有评论都集中到了`positive.csv`和`negative.csv`中

