# Iterable 資料型態(可疊代資料型態，即可以取出的資料)
#for 迴圈
for x in "abc": #自串
    print(x)
print("-----")
for x in [3,5,2]: #列表
    print(x)
print("-----")
for x in {"a","test",3,10} : #集合，沒有順序姓
    print(x)
print("-----")
for x in {"a":3,"x":5} : #字典，針對key的部分
    print(x)
print("-----")
#for 變數名稱in 可疊代的資料:
dic={"a":3,"x":5}
for x in dic:
    print(x) #取得key
    print(dic[x]) #取得對應的值
print("=====")
#內建函式
#max(可疊代資料)
result=max([10,2,30,1]) #列表
print(result)
print("-----")
result=max("sjdiofz") #字串，字母越後面越大
print(result)
print("-----")
result=max({10,200,69,46}) #集合
print(result)
print("-----")
result=max({"x":50,"q":100}) #字典，取KEY，而非值的大小
print(result)
print("=====")
#sorted(可疊代資料，會有由小到大自動排序的功能，用列表回傳)
result=sorted("cab")
print(result)
print("-----")
result=sorted({10,2,100,-5})
print(result)









