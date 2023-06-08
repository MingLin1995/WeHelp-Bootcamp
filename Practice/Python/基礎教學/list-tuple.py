#有序可變動列表 List []
grades=[30,40,60,55,95]
print(grades)
grades=[30,40,60,55,95]
print(grades[4])

grades[0]=60 #更新列表[]=XX 把60放到序列三的位置 不可以用()
print(grades)

grades=[30,40,60,55,95]
print(grades[1:4]) #取列表1~3的值

grades=[30,40,60,55,95]
grades[1:4]=[] #連續刪除列表
print(grades) 

grades=[30,40,60,55,95]
grades=grades+[20,80] #串接列表
print(grades)
#計算列表長度 =len(列表) (用小括號)
length=len(grades) #上方字串原本5個+串接的2個，所以7個
print(length)

#巢狀列表(列表中的列表)
data=[[3,4,5],[6,7,8,]]
print(data[1][2]) #第一層第三個數值
data[0][0:2]=[5,5,5] #更新數值
print(data[0])

#=========================================================
#有序不可變動列表 Tuple ()
data=(3,4,5)
print(data)

data=(3,4,5)
data[0]=6 #會發生錯誤，Tuple的資料不可以變動
print(data)
















