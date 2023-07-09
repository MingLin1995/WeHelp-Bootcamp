""" ----------------#1 網站基礎架構總覽、Flask 快速開始---------------- """

""" 載入Flask模組 """
from flask import Flask
""" 建立 Application 物件 """
app=Flask(__name__)

""" 建立網站首頁的回應方式(建立路徑 / 對應的處理函式) """
@app.route("/") # /代表網站首頁 (用來回應路徑 / 的處理函式)
def index(): #用來回應網站首頁的連線方式
    return "Hello Flask" #回傳網站首頁的內容

""" 啟動網站伺服器 """
#app.run()

""" 啟動伺服器在終端機輸入python flask-base.py """
""" 中斷伺服器在終端機按下ctrl+C """

""" ----------------#2 網址 URL 的組成與運作方式---------------- """
'''
網址 Web Address (URL)
通訊協定(Protocol)://主機名稱(Hostname):埠號(Port)/路徑(Path)?要求字串(Query String)
https://www.google.com.tw/  #埠號:http預設443(預設不用寫出來) 要求字串:無
'''

""" 啟動網站伺服器，可透過port參數指指定埠號(預設5000) """
#app.run(port=3000)

""" ----------------#3 路由基礎 Route---------------- """
'''
Route 決定網址路徑和處理函式的對應關係，前端輸入不同路徑時，後端程式要決定對應的處理函式

@app.route("路徑")
def 處理函式名稱(參數名稱):
    處理函式的程式區塊

#動態路由設定語法
@app.route("/固定字首/<參數名稱>")
def 處理函式名稱(參數名稱):
    處理函式的程式區塊
'''

""" 建立路徑 /data 對應的處理函式 """
@app.route("/data")
def handleDate():
    return "My Data"

""" 動態路由：建立路徑　/user/使用者名稱 對應的處理函式 """
@app.route("/user/<username>")
def handleUser(username):
    if username=="Ming":
        return username+"(伺服器的創造者)，你好" 
        #http://127.0.0.1:3000/user/Ming
    else:
        return "Hello"+username
        #http://127.0.0.1:3000/user/約翰


app.run(port=3000) #通常寫在程式碼最後一行，才能保證上方程式都能執行


