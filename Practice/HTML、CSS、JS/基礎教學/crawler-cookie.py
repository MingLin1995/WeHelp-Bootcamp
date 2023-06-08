#抓取PTT八卦版的網頁原始碼(HTML)
import urllib.request as req
#定義函式，下方全部縮排，畫面會比較簡潔
def getData(url): 
    #url="https://www.ptt.cc/bbs/Gossiping/index.html" 定義函示後就不用這一段
    #建立一個Request物件，附加Request Headers的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1", #因為有跳出是否滿18歲，要加入cookie的動作才有辦法進去網頁
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

        #解析原始碼，取得每篇文章的標題
        import bs4
        root=bs4.BeautifulSoup(data,"html.parser") #讓BeautifulSoup協助我們解析HTML格式文件
        titles=root.find_all("div",class_="title") #尋找所有 class="title"的dic標籤
        for title in titles:
            if title.a != None: #如果標題包含a標籤(沒有被刪除),印出來
                print(title.a.string)                
        #抓取上一頁的連結
        print("-----換頁分隔線-----")
        nextLink=root.find("a",string="‹ 上頁") #找到內文是‹ 上頁的a標籤
        return (nextLink["href"]) #要印出的是這個標籤的href屬性
print("------------------------------------------")        

#主程序:抓取一個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
pageURL="https://www.ptt.cc"+getData(pageURL) #呼叫函式，return的結果會回傳回來 
         #因為跑出來資料沒有https所以要自己加上
print(pageURL) #會印出上一頁的網址
print("------------------------------------------")

#抓取多個頁面
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1









