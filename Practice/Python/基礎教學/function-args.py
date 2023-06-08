#參數的預設資料(若沒指定資料就會跑預設值)
def power(base,exp):
    print(base**exp)
power(3,2)
#power(4) →會發生錯誤，因為沒有給參數的預設值
def power(base,exp=0): #預設如果沒有給參數就是0次方
    print(base**exp)
power(4)
print("---------------------------------------------")
#使用參數名稱對應(可以任意改變資料順序)
def divide(n1,n2):
    print(n1/n2)
divide(2,4)
divide(n2=2,n1=4)
print("---------------------------------------------")
#無限/不定 參數資料(在資料前面加*，就能放無限或不定數量個資料)
def avg(*ns): 
    print(ns) #會印出各個，有順序、不可動的列表 Tuple
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8) 
print("---------------------------------------------")
def avg(*ns):
    for n in ns: #迴圈會把列表資料一個一個取出來
        print(n)
avg(3,4)
print("---------------------------------------------")
#計算平均數，不管有幾個資料都能平均
def avg(*ns):
    sum=0
    for n in ns:
        sum+=n
    print(sum/len(ns)) #除以列表長度，等於除上幾個數
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8) 









