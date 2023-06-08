#隨機模組
import random

#隨機選取 choice、sample
data=random.choice([1,5,6,10,20]) # 隨機選取數字
print(data)
data=random.sample([1,5,6,10,20],3) #可以一次選出N個隨機數字
print(data)

#隨機調換順序 shuffle （就是洗牌的概念）
data=[1,5,8,20]
random.shuffle(data) #會直接對date修改
print(data)

#隨機取得亂數 random、uniform
data=random.random() #0~1之間的隨機亂數
print(data)
data=random.uniform(60,100) #X~Y之間的隨機亂數（可以指定開頭跟結束的數字）
print(data)

#取得常態分配亂數 normalvariate(平均數,標準差)
data=random.normalvariate(100,10) #資料通常都在90~110之間
print(data)

#統計模組
import statistics as stat #簡化函式名稱用別名
data=stat.mean([1,4,5,8]) #mean 取得平均數
print(data)
data=stat.median([1,2,3,4,5,8,100]) #median 取得中位數
print(data)
data=stat.stdev([1,2,3,4,5,8,100]) #stdec 取得標準差(資料散佈的狀況)
print(data)









