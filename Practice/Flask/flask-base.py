""" ----------------#1 網站基礎架構總覽、Flask 快速開始---------------- """

""" 載入Flask模組 """
from flask import Flask
""" #5 載入請求物件 """
from flask import request

""" 建立 Application 物件(預設__name__)，也可以設定靜態檔案的處理路徑(參考#4) """
app=Flask(
    __name__,
    #4 所有在static資料夾底下的檔案，都會應到網址路徑/abc/檔案名稱
    static_folder="static", #folder指定資料夾名稱 預設為static
    static_url_path="/" #url_path指定對應的網址路徑 預設為/static
)

""" 建立網站首頁的回應方式(建立路徑 / 對應的處理函式) """
@app.route("/") # /代表網站首頁 (用來回應路徑 / 的處理函式)
def index(): #用來回應網站首頁的連線方式
    #return "Hello Flask" #回傳到網站首頁的內容

    """ #5 請求物件"""
    print("請求的方法：",request.method) #之後會特別介紹
    print("通訊協定：",request.scheme)
    print("主機名稱：",request.host)
    print("路徑：",request.path)
    print("完整的網址：",request.url)
    print("瀏覽器和作業系統：",request.headers.get("user-agent"))#請求物件.headers屬性.get方法(要取得的標頭名稱)
    print("語言偏好：",request.headers.get("accept-language"))
    print("引薦網址：",request.headers.get("referrer"))#例如別人從google點進來到我的網址，那google就是引薦網址

    """ #5 前後端互動 """
    lang=request.headers.get("accept-language")
    if lang.startswith("en"): #startswith 檢查字串是否用指定的字開頭
        return "Hello Flask"
    else:
        return "您好，歡迎光臨"

    

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




""" ----------------#4 靜態檔案處理 Static Files---------------- """
""" 靜態檔案→完全不執行程式直接將檔案送到前端(圖片、影片、HTML、CSS、JS) """

""" Flask預設處理：建立static資料夾→放入檔案→啟動伺服器，就能使用/static/檔案名稱連線 """
#http://127.0.0.1:3000/static/head.png
#http://127.0.0.1:3000/static/test.txt

""" folder指定資料夾名稱、url_path指定對應的網址路徑，請看程式碼8、11~13 """
#static_url_path="/abc"
#http://127.0.0.1:3000/abc/head.png

#也可以設定根目錄 static_url_path="/"
#http://127.0.0.1:3000/head.png


app.run(port=3000) #通常寫在程式碼最後一行，才能保證上方程式都能執行


""" ----------------#5 請求物件基礎 HTTP Request---------------- """
""" 載入請求物件 from flask import request """
""" 參考程式碼5、程式碼19 """

""" ----------------#6 要求字串處理 Query String---------------- """