""" ----------------#1 網站基礎架構總覽、Flask 快速開始---------------- """

""" 載入Flask模組 """
from flask import Flask
""" 建立 Application 物件 """
app=Flask(__name__)

""" 建立網站首頁的回應方式 """
@app.route("/") # /代表網站首頁
def index(): #用來回應網站首頁的連線方式
    return "Hello Flask" #回傳網站首頁的內容

""" 啟動網站伺服器 """
app.run()

""" 啟動伺服器在終端機輸入python flask-base.py """
""" 中斷伺服器在終端機按下ctrl+C """

""" ----------------#2 網址 URL 的組成與運作方式---------------- """

