# While 迴圈 如果為True會一直執行，直到False
n=1
while n<=3:
    print(n)
    n+=1
#從1+2+3+.....+10=55
n=1
sum=0 #紀錄累加的結果
while n<=10:
    sum=sum+n
    n+=1
print(sum)
print("-----")

# For 迴圈    For 變數名稱 in 列表、字串→會將列表資料一一撈出來
for x in [3,5,1]:
    print(x)
print("-----")
for x in "Hello":
    print(x)
print("-----")

# range相當於列表，從零開始，不包含結尾
for x in range(5): #會出現0 1 2 3 4
    print(x)
print("-----")
for x in range(5,10): #包含開頭不包含結尾
    print(x)
print("-----")
#從1+2+3+.....+10=55
sum=0
for x in range(11): #或是 range(1,11)
    sum=sum+x
print(sum)



















