#載入pandas模組
import pandas as pd

#資料索引:pd.DataFrame(字典,index=索引列表)
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
},index=["a","b","c"]) #自訂索引
print(data)
print("===========")

#觀察資料
print("資料數量",data.size)
print("資料形狀(列,欄)",data.shape) #注意先顯示列，才會顯示欄
print("資料索引",data.index)
print("===========")

#取得列的Series資料:根據順序(iloc)取得資料、根據索引(loc)取得資料
print("取得第二列",data.iloc[1],sep="\n") #變更連接分隔符號 sep='<你要的分隔符號>’
print("===========")
print("取得第C列",data.loc["c"],sep="\n")
print("===========")

#取得欄的Series資料:根據欄位的名稱
print("取得salary欄位",data["salary"],sep="\n")
print("===========")
names=data["name"] #取得單維度的Series資料放進變數names
print("把name全部轉大寫",names.str.upper(),sep="\n")
print("===========")

#計算薪水的平均值
salaries=data["salary"]
print("薪水的平均值",salaries.mean())
print("===========")

#建立新的欄位 #兩種方法都可以用
data["REV"]=[500000,400000,30000] #data[新欄位的名稱]=列表
data["Rank"]=pd.Series([3,6,1],index=["a","b","c"]) #data[新欄位的名稱]=Series的資料
data["CP值"]=data["REV"]/data["salary"] #用現有欄位資料複製過去，並且計算
print(data)




