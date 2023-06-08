#定義生成器函式 yield
def test():
    yield 5
#呼叫並回傳生成器(只要定義函式中使用到yield就會變成生成器)
gen=test()
print(gen) #可以觀察不是印出 yield 5，是產生"出生成器物件"(generator object)
#搭配for迴圈中使用
for x in gen: #for 變數 in 生成器
    print(x) #會印出5
print("===========")
def test():
    print("階段一")
    yield 5
    print("階段二")
    yield 10
gen=test()
for x in gen:
    print(x)
print("============")

def Even(): #產生出偶數
    number=0
    yield number
    number+=2
    yield number
    number+=2
    yield number
x=Even()
for data in x:
    print(data)
print("============")
def Even(max): #自動產生出到10的偶數
    number=0
    while number<=max :
        yield number
        number+=2 
x=Even(10)
for data in x:
    print(data)

    
    
    











