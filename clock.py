# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import os
import TextTweet
import GetTweet
import ReplyTweet
import PrepareChain

# APIのトークン
CK="ここにAPI key"
CS="ここにAPI secret key"
AT="ここにAcsess token"
AS="ここにAccess token sercret"

twische = BlockingScheduler()

# 10分に一度ツイート（minutesで時間を指定できるよ）
@twische.scheduled_job('interval',minutes=10)
def timed_job():
    TextTweet.puttweet()

# 1分に一度返信するよ（minutesで時間を指定できるよ）
@twische.scheduled_job('interval',minutes=1)
def timed_job():
    ReplyTweet.replytweet()

# 10分に一度ツイートを取得、チェーンを作ってdbに保存するよ
@twische.scheduled_job('interval',minutes=10)
def timed_job():
    #ツイートを取得
    GetTweet.gettweet(CK,CS,AT,AS)

    #data.txtに保存
    f = open("data.txt",encoding="utf-8")
    text = f.read()
    f.close()

    #チェーンを作成、dbに保存
    chain = PrepareChain(text)
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)

if __name__ == "__main__":
    twische.start()
