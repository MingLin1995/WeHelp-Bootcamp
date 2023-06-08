#Point實體物件的設計:平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self): #定義實體方法(函式)
        print(self.x,self.y)
    def distance(self,targetX,targetY):#找出該線段對於目標先段的距離 ((X1-X2)^2+(Y2-Y1)^2)^0.5
        return ((self.x-targetX)**2+(self.y-targetY)**2)**0.5
p=Point(3,4)
p.show() #呼叫實體方法(函式) 實體物件.實體方法的名稱()
result=p.distance(0,0)
print(result) #結果是利用return回傳到result

#File實體物件的設計:包裝檔案讀取的程式
class File:
    def __init__(self,name):
        self.name=name
        self.file=None #初始設定尚未開啟檔案 所以用None的用法
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
#讀取第一個檔案
f1=File("data1.txt")
f1.open()
data=f1.read()
print(data)
#讀取第二個檔案
f2=File("data2.txt")
f2.open()
data=f2.read()
print(data)













