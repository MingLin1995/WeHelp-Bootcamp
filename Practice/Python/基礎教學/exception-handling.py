#例外處理情境：轉換資料型態失敗，要預先設想可能發生錯誤的情形
data=input("請輸入一個數字：")

#try內的程式碼發生錯誤，就會跳到exception繼續往後執行，如果沒發生錯誤，就會跳過exception繼續執行下面的程式碼
try:
    number=int(data) #這行指令可能會發生錯誤，因為使用者可能會輸入非數字的值
except Exception: #try發生錯誤後，會跳到exception
    number=0 #輸入任何非數值值的值，都會變成0

number=number*2
print(number)
print("------------------------------")

#使用者如果輸入的資料格式不能轉換成數字，請他重新輸入，直到輸入成功為止
while True: #無窮迴圈
    data=input("請輸入一個數字：")
    try:
        number=int(data) 
        break #若沒發生錯誤，就會跳出迴圈
    except Exception:
        print("輸入格式錯誤，請重新再輸入") 
        
number=number*2
print(number)