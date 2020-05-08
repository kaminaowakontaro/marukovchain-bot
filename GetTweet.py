# -*- coding: utf-8 -*-
import os
import re
import requests
import tweepy

# APIのトークン
CK="ここにAPI key"
CS="ここにAPI secret key"
AT="ここにAcsess token"
AS="ここにAccess token sercret"

def gettweet(CK, CS, AT, AS):

    # APIに接続
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    # RTを除いた最新100ツイートを取得するよ
    results=api.home_timeline(count=100,include_rts=False)

    #ここのmodeをaにするとdata.txtに上書きしてくれるよ
    f=open(r"data.txt",mode="w",encoding="utf-8")

    for result in results:

        #リンクの削除
        result.text=re.sub(r"https?://[\w/:%\$&\?\(\)~\.=\+\-…_]+", "" ,result.text)

        #@ツイートの削除
        result.text=re.sub("@[\w]+","",result.text)

        #ほかにも消したい文字があるならここにresult.text=re.sub("消したい文字","",result.text)と追記(ツイッターの設定でワードミュート設定するほうが手軽）
        result.text=re.sub("#質問箱","",result.text)
        result.text=re.sub("#peing","",result.text)

        #data.txtへ書き込み
        f.write(result.text+"\n")

    f.close()

if __name__=="__main__":
    gettweet(CK,CS,AT,AS)