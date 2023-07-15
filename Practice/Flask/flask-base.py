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
    """ 如果主要語言是英文就回應英文，若主要語言是其他語言，就回應中文 """
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


""" ----------------#5 請求物件基礎 HTTP Request---------------- """
""" 載入請求物件 from flask import request """
""" 參考程式碼5、程式碼19 """

""" ----------------#6 要求字串處理 Query String---------------- """
""" 參數名稱=對應的資料&參數名稱=資料&....  """
#https://www.google.com.tw/search?q(參數名稱)=iphone14(對應的資料) 前端送出要求搜尋iphone14

#建立路徑 /getSum對應的處理函式 
#/路徑(Path)?要求字串(Query String)&要求字串(Query String)
#並且利用要求字串(Query String)提供彈性：/getSum?min=最小數字 & max=最大數字
@app.route("/getSum")
def getSum():#1+2+3+...+100 #1+2+3+...+max #min+(min+1)+....+max
    #接收要求字串中的參數資料
    maxNumber=request.args.get("max",100) #(對應的字串max,預設值為100)
    maxNumber=int(maxNumber)
    print("最大數字",maxNumber)

    minNumber=request.args.get("min",1)
    minNumber=int(minNumber)
    print("最小數字",maxNumber)
    
    result=0
    for i in range (minNumber,maxNumber):
        result+=i
    return "結果："+str(result)


""" ----------------#7 回應與導向 Response & Redirect---------------- """
#載入redirect函式
from flask import redirect
#載入json模組，可以幫助我們把字典轉換成json格式的字串
import json

@app.route("/json") 
def indexJson(): 
    """ 透過redirect(網址路徑)，將使用者導向特定網址路徑 """
    #return redirect("/") #導向到路徑/ 也可以導向到完整的網址https://www.google.com.tw/

    """ 透過Json.dumps(字典)，將字典型態的資料轉換成json格式字串，傳送到前端 """
    lang=request.headers.get("accept-language")
    if lang.startswith("en"): 
        return redirect("/en/") #透過路徑導向轉換到其他路由
        return json.dumps({
            "This is the key of dictionary 1": "This is the value of dictionary 1",
            "This is the key of dictionary 2": "This is the value of dictionary 2"
        })
    else:
        return redirect("/zh/")
        return json.dumps({
            "這是字典1的key":"這是字典1的value"
            ,"這是字典2的key":"這是字典2的value"
            },
            #中文轉換成json格式時會被用英文重新編碼，所以要額外處理
            ensure_ascii=False #指示不要用ASCII編碼處理中文
        )

@app.route("/en/") 
def indexEnglish():   
    return json.dumps({
            "This is the key of dictionary 1": "This is the value of dictionary 1",
            "This is the key of dictionary 2": "This is the value of dictionary 2"
        })

@app.route("/zh/") 
def indexChinese():  
    return json.dumps({
            "這是字典1的key":"這是字典1的value"
            ,"這是字典2的key":"這是字典2的value"
            },
            #中文轉換成json格式時會被用英文重新編碼，所以要額外處理
            ensure_ascii=False #指示不要用ASCII編碼處理中文
        ) 

""" ----------------#8 樣板引擎 Template Engine---------------- """
#回應前端的方式1.直接回應字串2.回應JSON格式字串3.重新導向4.使用樣板引擎

""" 
建立樣本檔案，放在在專案的templates資料夾底下
利用 {{資料欄位名稱}} 定義欄位
透過render_template(檔案路徑,資料欄位名稱=資料) 
"""
#載入render_template函式
from flask import render_template
@app.route("/template")
def index_Template():
    return render_template("indexTemplate",name="小明") #index檔案也要改


""" ----------------#8 樣板引擎 Template Engine---------------- """
app.run(port=3000) #通常寫在程式碼最後一行，才能保證上方程式都能執行
