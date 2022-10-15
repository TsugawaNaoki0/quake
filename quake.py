# message = "〇〇〇〇年〇〇月〇〇日〇〇時〇〇分〇〇秒　〇〇地域　M〇〇　深さ〇〇km　最大震度〇〇"

import requests
import re
import datetime
import urllib.request, urllib.error
import csv
import requests
import feedparser
import os
from email.mime.text import MIMEText
import smtplib
import sys





class to_mail_class():
    def to_mail(self):
        # mail_list = ["jinchuanzhishu76@gmail.com"\
        #              ,"qq856533@gmail.com"\
        #              ,"mqiang838@gmail.com"\
        #              ]
        ##########################################


        return mail_list


class quake_mail_class():
    def quake_mail(self, quake_news, to_address_list):

        # SMTP認証情報
        account = "subaodezhen641@gmail.com"
        # password = "19960701jishin"
        password = "ubqrmyfjgxsojiwg"

        # 送受信先
        to_email = to_address_list
        from_email = "subaodezhen641@gmail.com"

        # MIMEの作成
        subject = "地震速報"
        # message = "地震速報"
        message = quake_news
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = from_email

        # メール送信処理
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(account, password)
        server.send_message(msg)
        server.quit()


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




args = sys.argv

mail_list = []

for i in range(1, len(args)):
    mail_list.append(args[i])
    print("<p>" + mail_list[i-1] + "</p>")




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
    # print(ddd[0])
    # print(type(ddd[0]))

    message = ddd[0]


    res_list = re.findall(r'\d+', message)
    # print(res_list)
    res_date_before = res_list[0]

    res_date = res_date_before[:4] + "年" + res_date_before[4:]
    res_date = res_date[:7] + "月" + res_date[7:]
    res_date = res_date[:10] + "日" + res_date[10:]
    res_date = res_date[:13] + "時" + res_date[13:]
    res_date = res_date[:16] + "分" + res_date[16:]
    res_date = res_date[:19] + "秒" + res_date[19:]
    # print(res_date)
    # res[7] = "年"
    # res[10] = "年"
    # massage = res
    message = message.replace(res_date_before, res_date)



    # time = datetime.datetime.now()   # 日付を取得する
    # time = time.strftime('%Y年%m月%d日 %H:%M:%S')   # 見やすく変換する

    # 以下、LINEのメッセージ送信プログラム

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



    qqq = to_mail_class()
    to_mail_list = qqq.to_mail()
    print(to_mail_list)





    # to_mail_address = to_mail_list[0]
    to_mail_address = to_mail_list



    for i in range(len(to_mail_address)):
        quake_news = send_contents
        aaa= quake_mail_class()
        bbb = aaa.quake_mail(quake_news, to_mail_address[i])

f.close()




 # while true; do python3 quake.py; sleep 20s; done
