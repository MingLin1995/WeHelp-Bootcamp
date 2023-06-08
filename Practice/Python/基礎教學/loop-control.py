# break 若判斷為True，就會跳脫出該迴圈
n=0
while n<5:
    if n==3:
        break #若n=3跳出該迴圈
    print(n) #印出迴圈中的n
    n+=1
    
print("最後的n:",n) #印出迴圈結束後的n

# continue 強制繼續下個迴圈
n=0
for x in [0,1,2,3] :
    if x%2==0: #X除以2取餘數(X是偶數)
        continue #True的話會繼續"從頭"執行，不會跑下方程式碼(直接重新執行迴圈，跳過下方)
    print(x) 
    n+=1
print("最後的n:",n) #只有執行兩次，n=0+1(印出1)+1(印出3)=2

#else 迴圈結束前，執行此區塊的語法
sum=0
for x in range(11) :
    sum+=x
else :
    print(sum) #印出1+2+...+10的結果
    
#找整數出平方根 EX.輸入9得3 輸入11得[沒有整數的平方根]
n=int(input("請輸入一個正整數:")) #將n轉換成數字
for i in range(n): #i的值為 0~n-1
    if i*i==n:
        print("該數值整數平方根為:",i)
        break # 小技巧 用break強制結束迴圈時，不會執行else區塊
else:
    print("該數值沒有整數平方根")
