from flask import Flask
app=Flask(__name__) #__name__代表目前執行的模組

@app.route("/") #函式的裝飾(Decorator):以函式為基礎，提供附加的功能
def home():
    return "Hello 測試測試測試" #瀏覽器輸入 http://127.0.0.1:5000/ 會顯示出來

@app.route("/test") #代表我們要處理的網站路徑
def test():
    return "Hello Test"

if __name__ == "__main__": #如果以主程式執行
    app.run() #立刻啟動伺服器

#Heroku 雲端主機教學(教學二) ※herouku 目前已經沒辦法用要付費
#1.建立專案描述檔 runtime.txt 告訴人家python版本
#2.建立專案描述檔 requirements.txt告訴人家我們的專案在運作時，需要那些套件
#3.建立專案描述黨 Procfile 告訴gunicorn要怎麼啟動我們的專案 app(代表app.py):app(代表物件名稱app=Flask.........)
#4 問一下毛怎麼放到雲端上，若更新程式要怎麼更新