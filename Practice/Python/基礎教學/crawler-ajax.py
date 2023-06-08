#AJAX技術 Medium 先跑出架構，才會跑出內容 or 右鍵查看原始碼，原始碼會找不到文章標題
#F12 Network→XHR(AJAX技術的另外一個稱呼)
#Preview可以預覽→找到要的標題

#抓取Medium.COM的文章資料
import urllib.request as req #urllib.request 取得資料的python模組
url="https://medium.com/_/api/home-feed"
request=req.Request(url,headers={ 
#建立一個Request物件，附加Request Headers的資訊(要讓伺服器認為是正常使用者)(增加表頭偽裝成瀏覽器)
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response: 
    data=response.read().decode("utf-8") #根據觀察，取得的資料是JSON格式

#解析 JSON格式的資料，取得每篇文章的標題(參考圖一)
import json
data=data.replace("])}while(1);</x>","") #把會影響JSON解析的資料刪除
data=json.loads(data) #把原始的JSON資料解析成字典/列表的表示形式

#取得JSON資料中的文章標題 (參考圖二)
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])