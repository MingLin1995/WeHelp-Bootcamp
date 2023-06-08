#Point 實體物件的設計：平面座標上的點
class Point: #先建立類別名稱
    def __init__(self): #定義初始化函式
        self.x=3 #建立實體屬性 self.屬性的名稱=放入的資料
        self.y=4
p=Point() #建立實體物件，放入變數p(此實體物件包含x、y兩個實體屬性)
print(p.x,p.y) #呼叫初始化函式

#參數彈性變化
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
p1=Point(3,4) #建立第一個實體物件
print(p1.x,p1.y)
p2=Point(5,6) #建立第二個實體物件
print(p2.x,p2.y)

#FullName 實體物件的設計：分開紀錄姓、名資料的全名
class FullName:
    def __init__(self):
        self.first="Y.M"
        self.last="Lin"
name=FullName()
print(name.first,name.last)

#參數彈性變化
class FullName:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=FullName("Y.M","Lin")
print(name1.first,name1.last)
name2=FullName("L.L","LAI")
print(name2.first,name2.last)











