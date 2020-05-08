# -*- coding: utf-8 -*-
import tweepy
from GenerateText import GenerateText
import random
import time

def replytweet():
    # APIのトークン
    CK="ここにAPI key"
    CS="ここにAPI secret key"
    AT="ここにAcsess token"
    AS="ここにAccess token sercret"

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth)

    #ここのcount=の数字が一回に取得するツイートの数だよ
    status = api.mentions_timeline(count = 100)

    for mention in status:
        generator = GenerateText(random.randint(1,3))
        markovstring = generator.generate()
        mentionTime = mention.created_at.timestamp()
        nowTime = time.time()
        if nowTime - mentionTime < 32460.0:
                #ツイート内容
                reply_text = "@"+str(mention.user.screen_name)+" "+markovstring+"ここに特定の語尾を書く（なければ消す）"
                api.update_status(status = reply_text, in_reply_to_status_id = mention.id)


if __name__=="__main__":
    replytweet()