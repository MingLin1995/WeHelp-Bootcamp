#載入pandas模組
import pandas as pd
#篩選練習-Series
data=pd.Series([30,15,20])
condition=[True,False,True] #要與資料數量對應(篩選條件，True就會抓出來)
filteredData=data[condition] #建立篩選條件
print(filteredData)
print("===or==")
data=pd.Series([30,15,20])
condition=data>18 #資料篩選的概念(假設篩選出>18歲)
print(condition) #會找出TorF
filteredData=data[condition] 
print(filteredData)
print("=====")
data=pd.Series(["您好","Python","Pandas"])
condition=data.str.contains("P") #是否包含特P #contains 判斷是否包含特定字元
print(condition)
filteredData=data[condition]
print(filteredData)
print("=====")
#篩選練習-DataFrame
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
})
print(data)
condition=data["salary"]>=40000
filteredData=data[condition]
print(filteredData)
print("=====")
condition=data["name"]=="Amy"
filteredData=data[condition]
print(filteredData)









