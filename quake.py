import requests
import re
import datetime
import urllib.request, urllib.error
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


path = './data/quake_data.txt'
# path = '/home/natsukiogawa/sample/quake_data.txt'


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


    ccc = y_news_class()
    ddd = aaa.y_news(url)
    # print(ddd)
    # print(type(ddd))
    print(ddd[0])
    print(type(ddd[0]))

    message = ddd[0]


    res_list = re.findall(r'\d+', message)
    print(res_list)
    res_date_before = res_list[0]

    res_date = res_date_before[:4] + "年" + res_date_before[4:]
    res_date = res_date[:7] + "月" + res_date[7:]
    res_date = res_date[:10] + "日" + res_date[10:]
    res_date = res_date[:13] + "時" + res_date[13:]
    res_date = res_date[:16] + "分" + res_date[16:]
    res_date = res_date[:19] + "秒" + res_date[19:]
    print(res_date)
    # res[7] = "年"
    # res[10] = "年"
    # massage = res
    message = message.replace(res_date_before, res_date)



    time = datetime.datetime.now()   # 日付を取得する
    time = time.strftime('%Y年%m月%d日 %H:%M:%S')   # 見やすく変換する

    TOKEN = 'ubh9DRuV9zdbxHuY7bRdyigA1nSVTaMj1O8E2oE9QJt'
    api_url = 'https://notify-api.line.me/api/notify'
    #時刻を送る内容の変数に設定
    # send_contents = time
    # send_contents = "プログラムが起動されました。"
    send_contents = "地震が起きました : " + message + " "
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic = {'message': send_contents}

    image_file = './test.png'
    binary = open(image_file, mode='rb')
    image_dic = {'imageFile': binary}

    requests.post(api_url, headers=TOKEN_dic, data=send_dic)


f.close()

 # while true; do python3 quake.py; sleep 20s; done
