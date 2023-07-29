""" ----------------#9 網站前後端互動 - 超連結與圖片---------------- """
#前端發出request請求，後端回應html程式碼(前端的HTML就是後端回應的字串)

from flask import Flask #載入Flask
from flask import request #載入Request物件
from flask import render_template #載入render_template函式 
#建立Application物件，設定靜態檔案的路徑處理
front_end_interaction=Flask(__name__,static_folder="templates-img", static_url_path="/img") 
#圖片網址 http://127.0.0.1:3000/img/arrow.png
""" 
前端根據網址發出請求到後端→後端把HTML送到前端
前端根據HTML中的圖片網址發送請求到後端→後端根據請求把圖片送到前端
"""

#使用GET方法，處理路徑/的對應函式
@front_end_interaction.route("/")
def index():
    return render_template("index.html")

#處理路徑/page的對應函式
@front_end_interaction.route("/page")
def page():
    return render_template("page.html")


""" ----------------#10 網站前後端互動 - 表單 Form---------------- """
""" 使用者可輸入資料，傳送到後端的介面 """

#處理路徑/show 的對應函式(使用GET方法)
@front_end_interaction.route("/show") #要跟html對應
def show():
    name=request.args.get("n","") #接收要求的字串(要跟html對應)，預設空白
    return "歡迎光臨,"+name

#綜合運用(使用POST方法)
@front_end_interaction.route("/calculate",methods=["POST"])
def calculate():
    #接收GET方法的Query String
    #maxNumber=request.args.get("max","")

    #接收POST方法的Query String
    maxNumber=request.form["max"] #網址不會顯示要求字串

    maxNumber=int(maxNumber)
    result=0
    for i in range(1,maxNumber+1):
        result+=i
    return render_template("result.html",data=result)


""" ----------------#11 網站前後端互動 - 連線方法 GET、POST---------------- """
""" 
method="GET"，沒有特殊處理(額外寫出來)，預設就是用GET方法做前後端互動
data=使用者輸入，會顯示在網址後面
參考 /show
"""
""" 
post 安全性較高，通常用在輸入帳號密碼類型
data=使用者輸入，不會顯示在網址後面，另外存放 
※注意python的部分寫法會跟get不太一樣
參考 /calculate
"""

""" ----------------#12 網站後端開發 - 使用者狀態管理 Session---------------- """
#網站前端每次跟後端連線都是獨立的事件，所以要透過session建立關係
#session[欄位名稱]=使用者輸入的資料

#載入session工具
from flask import session
#載入背後加密機制
front_end_interaction.secret_key="密鑰可以是任何的字串，但是不要告訴別人"

 
@front_end_interaction.route("/hello")
def hello():
    name=request.args.get("name","")
    session["username"]=name #把使用者輸入的字串，儲存下來
    return "您好，"+name
@front_end_interaction.route("/talk")

def talk():
    name=session["username"] #把儲存下來的字串，放到變數中
    return name+"，很高興見到你"



#啟動網站伺服器，可透過port參數指定埠號
front_end_interaction.run(port=3000)



