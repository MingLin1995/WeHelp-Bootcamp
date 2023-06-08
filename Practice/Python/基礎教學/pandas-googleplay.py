#csv就是用逗號把資料隔開，每一行就是一個列，每個逗號代表一個欄

import pandas as pd
#讀取資料
data=pd.read_csv("googleplaystore.csv") #把csv格式的檔案讀取成一個DataFrame
# #觀察資料
# print(data) #檔案會跑出10841列、13欄 但數據太多不會全部顯示出來，就會變成.....
# print("資料數量",data.shape)
# print("資料欄位(名稱)",data.columns)
# print("=====================================")
# #分析資料：評分的各種統計數據
# #假設對"評分"有興趣
# print(data["Rating"]) 
# print("平均數",data["Rating"].mean())
# print("中位數",data["Rating"].median())

# print("取得前100個應用程式的平均",data["Rating"].nlargest(100).mean()) #nlargest從數據中獲取N個最大值
# #跑出來的資料平均不應該大於5分
# #所以要找出問題點
# condition=data["Rating"]>5
# data=data[condition]
# print(data) #跑出資料評分19分，所以有問題，應該要排除

# condition=data["Rating"]<=5 #要先將上一段程式碼#才能跑出正確數字
# data=data[condition]
# print("平均數",data["Rating"].mean())
# print("中位數",data["Rating"].median())
# print("取得前100個應用程式的平均",data["Rating"].nlargest(100).mean())

#分析資料：安裝數量的各種統計數據
#print(data["Installs"]) #觀察安裝數量後發現不是數字格式，是字串(object)
#data["Installs"]=pd.to_numeric(data["Installs"]) #to_numeric是pandas提供的把字串轉數字的工具 #, + 這種符號電腦看不懂，沒辦法轉換
#data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","",regex=True)) #會出現，ValueError: Unable to parse string "Free" at position 10472
#regex解釋看這 https://blog.csdn.net/qq_46343832/article/details/123791759
#我們發現第10472筆資料顯示Free，所以要看一下問題
# print(data["Installs"][10472])
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","",regex=True).replace("Free",""))
# print("平均數",data["Installs"].mean())
# condition=data["Installs"]>100000
# print("安裝數量大於100000的應用程式有幾個",data[condition].shape[0]) #[0]代表顯示數量就好，不要欄


#基於資料的應用：關鍵字搜尋應用程式名稱
keyword=input("請輸入關鍵字：")
condition=data["App"].str.contains(keyword) #contains(是否包含，使用者輸入的關鍵字)
print(data[condition]["App"])
print("包含關鍵字的應用程式數量",data[condition].shape[0])
#若想要忽略大小寫
keyword=input("請輸入關鍵字：")
condition=data["App"].str.contains(keyword,case=False) 
print(data[condition]["App"])
print("包含關鍵字的應用程式數量",data[condition].shape[0])








