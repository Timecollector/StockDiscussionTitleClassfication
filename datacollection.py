import re
import requests
import csv
import time
import random


def download_stock_discussion_title(stock_number, page_start=1,page_end=10):
    page_start = int(page_start)
    page_end = int(page_end)
    f = open(f'{stock_number}discussions_page{page_start}to{page_end}.csv',mode='w',newline='',encoding='gb18030')
    csvwriter =csv.writer(f)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    # proxies = [
    #     '122.192.30.17:8080',
    #     '47.100.255.35:80',
    #     '58.246.58.150:9002',
    #     '112.6.117.135:8085',
    #     '60.161.5.40:8089',
    #     '183.47.237.251:80',
    #     '106.52.172.214:8088',
    #     '106.54.141.54:3128',
    #     '58.220.95.34:10174',
    #     '47.92.113.71:80',
    #     '113.125.152.179:8888',
    #     '39.108.193.201:8888',
    #     '223.100.215.24:8080',
    #     '221.7.197.248:8000',
    #     '218.244.147.59:3128',
    #     '36.134.91.82:8888',
    #     '47.93.239.66:1080',
    #     '58.20.232.245:9091'
    # ]
    str_lt = []
    time_lt = []
    for page in range(page_start, page_end + 1):
        print(f'开始第{page}页')
        time.sleep(random.random())
        url = f'http://guba.eastmoney.com/list,{stock_number}_{page}.html'
        # proxy = random.choice(proxies)
        # proxy = {
        #     'http' : 'http://'+proxy
        # }
        try:
            resp = requests.get(url, headers=headers)#,proxies=proxy)
        except requests.exceptions.ConnectionError as e:
            print(e.args)
        obj = re.compile(r'title="(?P<title>.*?)">.*?</a></span>')
        obj2 = re.compile(r'<span class="l5 a5">(?P<time>.*?)</span>')
        results = obj.finditer(resp.text)
        time_results = obj2.finditer(resp.text)
        for i in results:
            dic = i.groupdict()
            str_lt.append(dic['title'])
        for j in time_results:
            time_dic = j.groupdict()
            if time_dic['time'] != '最后更新':
                time_lt.append(time_dic['time'])
    print(len(str_lt), len(time_lt))
    for j in range(min(len(str_lt), len(time_lt))):
        # 这里之所以要改成列表，是因为writerow读取时按照列表读取，不改成列表就会一个字一个单元格
        m = [str_lt[j], time_lt[j].split(' ')[0]]
        csvwriter.writerow(m)
    print('保存成功')
    f.close()


if __name__ == '__main__':
    stock_number = input('请输入股票代码：')
    page_start = input('请输入开始页码：')
    page_end = input('请输入停止页码：')
    download_stock_discussion_title(stock_number=stock_number, page_start=page_start,page_end=page_end)
