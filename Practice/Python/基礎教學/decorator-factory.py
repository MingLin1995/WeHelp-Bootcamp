#一般裝飾器的運用
def myDeco (cb):
    def run():
        print("裝飾器內的程式")
        cb()
    return run
@myDeco
def test():
    print("普通函式的程式")
test()

print("----------------------------------")
#裝飾器工廠，就是用來生產裝飾器，概念上就是多一層函式
def myFactory(base): #注意層級排列 #可以定義一個參數 #裝飾器工廠
    def myDeco (cb): #裝飾器
        def run():
            print("裝飾器內的程式",base)
            result=base*2
            cb(result) #回呼函式，傳到普通函式中
        return run
    return myDeco #注意層級排列
@myFactory(3) #使用裝飾器工廠就要加上() 
def test(n):
    print("普通函式的程式",n)
test()
print("----------------------------------")
#計算1+2+3+......+max 的裝飾器工廠
def calculaterFactory(max):
    def calculate(callback):
        def run():
            total=0
            for n in range(max+1): #帶入自定義的參數
                total+=n
            callback(total)
        return(run)
    return(calculate)

@calculaterFactory(100)
def show(result):
    print("結果是",result)
@calculaterFactory(50)
def showEnglish(result):
    print("Result is",result)

show()
showEnglish()








