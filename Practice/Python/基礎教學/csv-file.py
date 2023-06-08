
#寫入CSV格式檔案
import csv
with open("data.csv",mode="w",newline="") as file: 
    #newline=""是一個小技巧，才不會在寫入時，多出不該多出的東西
    #新增一個csv檔案後，放到file這個變數內
    
    writer=csv.writer(file)
    writer.writerow([1,2,3]) #writerow寫入一個列表，會用逗號隔開，寫入一列(row)的資料
    writer.writerow([4,5,6])
    writer.writerow([7,8,9])
    #writer.writerow(["a","b","c"])

#讀取CSV格式檔案
import csv
with open("data.csv",mode="r",newline="") as file2:
    reader=csv.reader(file2)
    #逐列讀取資料
    for row in reader:
        print(row) #會用列表、字串的形式表示
    print("---------")

with open("data.csv",mode="r",newline="") as file2:
    reader=csv.reader(file2)        
    #把九個數字加總
    total=0
    for row in reader:        
        for data in row:
            total=total+int(data) #字串轉換成整數
    print(total)
