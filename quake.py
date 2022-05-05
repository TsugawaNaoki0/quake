import requests
import datetime
import numpy as np
import matplotlib.pyplot as plt
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv
import requests
import feedparser
import os



class y_news_class():
    def y_news(self, url):
        self.url = url
        data_bank = []

        feed = feedparser.parse(url)
        for entry in feed.entries:
            data_bank.append(entry.title)
            data_bank.append(entry.link)
            # print('タイトル:', entry.title)
            # print('URL:', entry.link)
        return data_bank

url = "https://headline.5ch.net/bbynamazu/news.rss"

aaa = y_news_class()
bbb = aaa.y_news(url)

# for i in range(len(bbb)):
#     print(bbb[i])

bbb = str(bbb)
data_now = bbb






# path = './data/quake_data.txt'
path = '/home/natsukiogawa/sample/quake_data.txt'


f = open(path, 'r', encoding='UTF-8')
data_before = f.read()
# print(data_before)

if (data_before == data_now):
    print("no change")
else:
    print("There are some changes")

    # path = './data/quake_data.txt'
    # path = './data/quake_data.txt'
    f = open(path, 'w')
    f.write(data_now)  # 何も書き込まなくてファイルは作成されました
    data_now = list(data_now)


    time = datetime.datetime.now()   # 日付を取得する
    time = time.strftime('%Y年%m月%d日 %H:%M:%S')   # 見やすく変換する

    TOKEN = 'ubh9DRuV9zdbxHuY7bRdyigA1nSVTaMj1O8E2oE9QJt'
    api_url = 'https://notify-api.line.me/api/notify'
    #時刻を送る内容の変数に設定
    # send_contents = time
    # send_contents = "プログラムが起動されました。"
    send_contents = "地震が起きました"
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic = {'message': send_contents}

    image_file = './test.png'
    binary = open(image_file, mode='rb')
    image_dic = {'imageFile': binary}

    requests.post(api_url, headers=TOKEN_dic, data=send_dic)



    # print(type(data_now))
    # print(len(data_now))

    # print(data_now)
    # print("<p>" + news + "</p>")



f.close()

 # while true; do python3 quake.py; sleep 20s; done









# path = './data/quake_data.txt'
# f = open(path, 'w')
# f.write(bbb)  # 何も書き込まなくてファイルは作成されました
# f.close()

# print(bbb)
