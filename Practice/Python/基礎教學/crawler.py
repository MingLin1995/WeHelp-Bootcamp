#抓取PTT電影版的網頁原始碼(HTML)
import urllib.request as req #urllib.request 取得資料的python模組
url="https://www.ptt.cc/bbs/movie/index.html"
request=req.Request(url,headers={ 
#建立一個Request物件，附加Request Headers的資訊(要讓伺服器認為是正常使用者)(增加表頭偽裝成瀏覽器)
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response: 
    data=response.read().decode("utf-8") #decode解碼方式
print(data) #可以抓到HTML的網頁原始碼

print("---------------------------------------------------")

#解析原始碼，取得每篇文章的標題，利用bs4套件做解析
import bs4
root=bs4.BeautifulSoup(data,"html.parser") #用html.parser(固定用法)讓BeautifulSoup協助我們解析HTML格式文件
print(root.title) #抓標題
print("---------------------------------------------------")
print(root.title.string,"\n\n\n") #抓標題內的文字，後面用換行看起來比較舒服
print("---------------------------------------------------")

titles=root.find("div",class_="title") #尋找class="title"的div標籤
#用find找到標籤名稱(div)篩選的條件為title
print(titles,"\n\n\n") #會出現div包起來的標籤

print(titles.a,"\n\n\n")  #代表只取到a標籤 

print(titles.a.string,"\n\n\n") #代表只取到a標籤內的文字

print("---------------------------------------------------")

titles=root.find_all("div",class_="title") #抓到所有標題
print(titles,"\n\n\n") 
for title in titles:
    if title.a !=None: #如果標題不等於無效，及有a標籤(沒有被刪除的文章)，則印出
        print(title.a.string)







