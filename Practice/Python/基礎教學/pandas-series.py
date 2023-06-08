#載入pandas模組
import pandas as pd
#資料索引
data=pd.Series([5,4,-2,3,7],index=["a","b","c","d","e"]) #自訂資料索引
print(data)
print("------------------------------------------------------")
#觀察資料
print("資料型態",data.dtype) #整數64位元
print("資料數量",data.size)
print("資料索引",data.index)
print("------------------------------------------------------")
#取得資料:、
print(data[2],data[0]) #根據順序
print(data["e"],data["d"]) #根據索引
print("------------------------------------------------------")
#數字運算:基本、統計、順序
print("乘法的總和",data.prod())
print("平均數",data.mean())
print("取前三大的數字",data.nlargest(3))
print("取最小的兩個數字",data.nsmallest(2))
print("------------------------------------------------------")
#字串運算:基本、串接、搜尋、取代
data=pd.Series(["您好","Python","pandas"])
print(data.str.lower()) #全部變小寫
print(data.str.len()) #算出字串的長度
print(data.str.cat(sep="-")) #把字串串起來，可自訂串接的符號
print(data.str.contains("P")) #判斷是否包含特定字元
print(data.str.replace("您好","Hello")) #取代字串










