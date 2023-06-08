#一般函式使用
def test (arg):
    print(arg)
test(3)
test("Hello")

#回呼函式流程 1.呼叫test函式(參數是另一個函式)
def test(arg): #2.函式x會傳到arg內
    print(arg) #arg是一個函式，名稱叫做x，記憶體位置式後面那一串 #3.因為arg變成函式，所以執行時會變成呼叫回呼函式(呼叫傳遞進來的回呼函式)
#定義一個回呼函式
def x():
    print(100) #4.執行回呼函式

test(x)  #1.呼叫test函式(參數是另一個函式x)

#一般用法
def test(arg):
    arg() #呼叫 回呼函式 
def x():
    print(100)
test(x)

#回呼函式定義定義參數用法
def test(arg):
    arg("給個資料吧")  
def x(da): #定義參數da
    print(da)
test(x)
print("=================")

def add(n1,n2):
    print(n1+n2)
add(3,4)

def add(n1,n2,x):
    x(n1+n2) #呼叫 回呼函式
def handle1(result): #用中文表示
    print("結果是",result)
def handle2(result): #用英文表示
    print("Result of Add is",result)
    
add(3,4,handle1)
add(856,6,handle1)
add(999,1,handle2)









