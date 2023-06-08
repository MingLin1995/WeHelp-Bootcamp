#定義類別、與類別屬性(封裝在類別中的變數和函式)

#定義類別
#class 類別名稱:
    #定義封裝的變數
    #定義封裝的函式

#定義一個類別 IO，有兩個屬性 supportedSrcs 和 read
class IO: #定義XXX類別(IO=input、output)；supportedSrcs跟src就是IO類別的屬性
    supportedSrcs=["console","file"] #定義變數
    def read(src): #定義函式
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("Read from",src) 

#使用類別 基本語法：類別名稱.屬性名稱
print(IO.supportedSrcs)
IO.read("file") #file傳到src，IF 是否不不在列表中，否，所以跳到ELSE
IO.read("internet") #IF 是否不再列表中，對不在列表中，所以印出NOT







