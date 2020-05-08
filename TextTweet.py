# -*- coding: utf-8 -*-
import json
from requests_oauthlib import OAuth1Session
from GenerateText import GenerateText
import random

def puttweet():
    # APIのトークン
    CK="ここにAPI key"
    CS="ここにAPI secret key"
    AT="ここにAcsess token"
    AS="ここにAccess token sercret"

    # APIに接続
    twitter = OAuth1Session(CK,CS,AT,AS)

    generator = GenerateText(random.randint(1,3))

    #ツイート
    markovstring = generator.generate()
    #ツイート内容
    params = {'status': markovstring + '特定の語尾をつけたいならここに書く（ないなら消してね）'}
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)

if __name__=="__main__":
    puttweet()