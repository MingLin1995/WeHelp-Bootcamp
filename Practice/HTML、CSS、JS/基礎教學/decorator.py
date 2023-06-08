#定義裝飾器
def myDeco(cb):
    def run():  #定義內部函式
        print("裝飾器中的程式碼")  #裝飾器中想要執行的程式碼
        cb()  #呼叫回呼函式，這個回呼函式，其實就是被裝飾的普通函式
    return run #回傳內部函式


#基本的函式使用
def test():
    print("基本的函式使用")
test()
print("-----------------------------")

#使用裝飾器→先執行"裝飾器中的程式碼"
#→呼叫回呼函式cb→才執行"普通函式的程式碼"
@myDeco  #@裝飾器名稱
def test():  #定義普通函式
    print("普通函式的程式碼")
test()
print("-----------------------------")


#傳遞參數
#基本的函式使用
def test(n):
    print("基本的函式使用，印出：",n)
test(5)
print("-----------------------------")
#使用裝飾器時
def myDeco2(x):
    def run():  
        print("裝飾器中的程式碼")  
        x(666)  #這裡是最關鍵的部分，跟一般使用方法不一樣 #呼叫回函式，傳到回呼函式內執行
    return run
@myDeco2
def test(n):
    print("使用裝飾器時，印出：",n)
test()


#定義一個裝飾器，計算1+2+....+50的總和
def calculate(callback):
    def run():
        #裝飾器想要執行的程式碼
        result=0
        for n in range(51):
            result+=n  
        #print("1+2+...+50的總和：",result) #寫這段就沒有意義了，因為裝飾器通常我們拿來計算，不拿來顯示
        callback(result)
    return run
#使用裝飾器
@calculate
def show(n):
    print("1+2+...+50的總和：",n)
show()

@calculate
def showEnglish(n):
    print("Result is：",n)
showEnglish()











    