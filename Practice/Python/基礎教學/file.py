#儲存檔案 檔案物件(自訂名稱)=open(檔案路徑(自訂名稱),mode=開啟模式(r=讀取、w=寫入、r+=讀寫))
file=open("data.txt",mode="w") #開啟(會自動新增到該程式儲存的資料夾)
file.write("Hello File\nSecond Lin") #操作(寫入資料+換行)
file.close() #關閉檔案的資源

#若使用中文，要設定utf-8編碼開啟，否則會出現亂碼
file=open("data.txt",mode="w",encoding="utf-8") 
file.write("測試中文\n好棒棒") 
file.close() #上一段程式碼會被覆蓋

#最佳實務上的寫法 with open(檔案路徑,=開始模式) as 檔案物件:   #該區塊會自動、安全的關閉檔案，就不用寫close
with open("data.txt",mode="w",encoding="utf-8") as file:
          file.write("測試中文\n測試換行")
#讀取檔案
with open("data.txt",mode="r",encoding="utf-8") as file:
    data=file.read() #全部讀取，放到變數data中
print(data)

#讀取檔案，並且把每一行的數字做加法(一行一行的讀取) 
with open("data.txt",mode="w") as file:
          file.write("5\n3")
sum=0 
with open("data.txt",mode="r") as file: #會把上面程式都覆蓋 
     for line in file:#for 變數 in 檔案物件: 若用read會全部讀取不好計算
        sum+=int(line) #字串轉換成整數型態
print(sum)
  
#使用JSON格式讀取、複寫檔案 *先回VC新增config.json 建議先看json的基本介紹才有感覺

#從檔案中讀取json資料，放入變數data裡面
import json #import json
with open("config.json",mode="r") as file:
    data=json.load(file) #讀取到的資料=json.load(檔案物件)
    
print(data) #data是一個字典資料
print("name: ",data["name"]) 
print("version: ",data["version"])

#把最新的資料修改複寫回檔案中
data["name"]="Ming" #修改變數中的資料
with open("config.json",mode="w") as file:
    data=json.dump(data,file) #json.dump(要寫入的資料,檔案物件)

















