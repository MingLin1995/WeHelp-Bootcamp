#定義函式 def XXXXX():
def multiply():
    print(3*4)    #沒有跳出錯誤就是正常執行，會沒有印出來是因為，函式內部的程式碼，如果沒有做函式呼叫就不會執行
#呼叫函式
multiply()

def multiply(n1,n2):
    print(n1*n2)
multiply(5,6)
multiply(11,11)

#return 結束定義函式，結束時會回傳Nono，寫跟不寫都一樣(預設跑完就是return)
def multiply(n1,n2):
    print(n1*n2) #印出12
    return #有寫跟沒有寫都一樣
value=multiply(3,4) 
print(value) #印出函式呼叫的結果，就是回傳值None

#return後面可以隨意放任何資料
def multiply(n1,n2):
    print(n1*n2) 
    return "隨便放任何資料，數字啥都可以" #也可以直接回傳 n1*n2
value=multiply(3,4) 
print(value) 

def multiply(n1,n2):
    return n1*n2
value=multiply(3,4)+multiply(5,10)
print(value) 

#函式可用來做程式的包裝，同樣的邏輯可以重複利用
def calculate(max):
    sum=0
    for n in range(1,max+1): #因為要會去尾數，所以要+1
        sum+=n
    print(sum)
calculate(10)
calculate(20)




















