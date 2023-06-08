#集合的運算
s1={3,4,5} #集合使用{} 沒有順序的概念
print(3 in s1) #判斷3是否在集合內
print(10 in s1)
print(10 not in s1) #判斷10沒有在集合內

s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 #交集 取兩集合中相同的資料
print(s3)
s3=s1^s2 #反交集 取兩集合中不相同的資料
print(s3)

s3=s1|s2 #聯集 取兩集合中所有的資料，但不重複選取
print(s3)

s3=s1-s2 #差集 從s1中減去與s2重疊的部分，順序會有差異
print(s3)
s3=s2-s1
print(s3)

# set(字串) 會自動拆解成集合
s=set("hello") #沒有順序性、不會重複
print(s) 
print("h" in s) #判斷字串是否在集合內
print("A" in s)

#字典的運算 key:value 配對    
dic={"apple":"蘋果","bug":"蟲蟲"} #:要用半形不能用全形
print(dic["apple"])
dic["apple"]="小蘋果" #更新資料用[]
print(dic["apple"])

#判斷 key是否存在，不能判斷value
print("apple" in dic)
print("小蘋果" in dic)
print("小蘋果" not in dic)

print(dic) #刪除前
del dic["apple"] #刪除字典中的鍵值對
print(dic) #刪除後

# 從[列表]的資料，自動產生字典 dic={x:x*2 for x in [列表] }
dic={x:x*2 for x in [3,4,5] }
print(dic)







