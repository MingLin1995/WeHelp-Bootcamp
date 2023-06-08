#載入pandas模組
import pandas as pd
#建立Series
data=pd.Series([20,10,15]) #建立"攔"(單維度的資料)
#基本Series操作
print(data)
print("Max",data.max())
print("Median",data.median())
print("----------------------------")
data=data*2
print(data)
data=data==20 #把資料拿去跟20做比較，如果有相等就是T，反之F(顯示布林值)
print(data)
print("----------------------------")

#建立DataFrame (雙維度的資料)
data=pd.DataFrame({
    "name":["amy","ming","nikki"],
    "salary":[30000,50000,40000]
})
#基本DataFrame操作
print(data)
print("----------------------------")
#取得特定的欄位
print(data["name"])
print(data["salary"])
#取得特定的列
print("============")
print(data.iloc[0]) #印出第一列 (iloc固定用法)




