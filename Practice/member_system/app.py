#初始化資料庫連線
import pymongo
""" 
連線網址
登入mongoDB→Databases→Connect→Connect to your application
"""
client=pymongo.MongoClient("mongodb+srv://root:root123@mycluster.wevxghs.mongodb.net/?retryWrites=true&w=majority")
db=client.member_system #資料庫名稱
#print("資料庫連線建立成功")

#初始化Flask伺服器
from flask import *
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key="任何字串都行，但要保密"

#處理路由
@app.route("/")
def index():
    #render_template 用樣板引擎渲染畫面，非透過網址轉跳
    return render_template("index.html") 

@app.route("/member")
def member():
    #判斷nickname_session有沒有在session中記錄
    if "nickname_session" in session:
        return render_template("member.html")
    else:
        return redirect("/")

#錯誤訊息要有彈性，不能寫死，因為可能帳密錯誤，或是輸入了空白訊息
#透過要求字串來顯示錯誤訊息 /error?msg=錯誤訊息
@app.route("/error") 
def error():
    #若有透過"msg"輸入要求字串，則顯示"要求的字串"，否則顯示"預設要求字串"
    message_var=request.args.get("msg","預設要求字串")
    #http://127.0.0.1:3000/error?msg=帳號錯誤 顯示"帳號錯誤"
    #http://127.0.0.1:3000/error 顯示"預設要求字串"

    #要渲染到error.html的變數名稱為message
    return render_template("error.html",message=message_var)

#會員註冊功能
#signup 是功能性路由，不渲染網頁畫面
""" 
1.註冊
2.到資料庫檢查、新增會員資料
3-1.註冊成功導向 / 頁面
3-2.註冊失敗導向 error 頁面
"""
@app.route("/signup",methods=["POST"])
def signup():
    #從前端接收資料
    nickname_var=request.form["nickname"]
    email_var=request.form["email"]
    password_var=request.form["password"]
    print(nickname_var,email_var,password_var)
    #return "ok" #畫面會顯示ok

    #根據接收到的資料，和資料庫互動
    collection=db.user
    result=collection.find_one({
        "email":email_var
    })
    #檢查是否有相同的Email資料
    if result != None: #如果不等於空值，代表被用過了
        #導向錯誤頁面
        return redirect("/error?msg=信箱已經被註冊")
    #把資料放進資料庫，完成註冊
    collection.insert_one({
       "nickname":nickname_var,
       "email":email_var,
       "password":password_var
    })
    #註冊成功，導向到首頁
    return redirect("/")

#會員登入、登出功能
""" 會員登入
1.首頁登入導向到/signin
2.到資料庫檢查帳號密碼
3-1.登入成功導向會員頁，紀錄session資訊
3-2.登入失敗導向錯誤頁面
"""
@app.route("/signin",methods=["POST"])
def signin():
    #從前端取得使用者的輸入
    email_var=request.form["email"]
    password_var=request.form["password"]
    #和資料庫互動
    collection=db.user
    #檢查信箱密碼是否正確
    result=collection.find_one({
        "$and":[
            {"email":email_var},
            {"password":password_var}
        ]
    })
    #找不到對應的資料，所以登入失敗，導向到錯誤頁面
    if result==None:
        return redirect("/error?msg=帳號或密碼輸入錯誤")
    #登入成功，在session紀錄會員資訊，導向到會員頁面
    session["nickname_session"]=result["nickname"]
    return redirect("/member")

 
""" 登出功能
1.登出導向到/signout
2.登出成功，移除session資訊
"""
@app.route("/signout")
def signout():
    #移除Session中的會員資訊
    del session["nickname_session"]
    return redirect("/")

app.run(port=3000)