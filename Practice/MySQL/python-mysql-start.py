""" 安裝套件 pip install mysql-connector-python """

""" 載入套件 """
""" 連線到資料庫 """
import mysql.connector
con = mysql.connector.connect(
    user="root",
    password="123456",
    host="localhost",
    database="mydb"
)
print("資料庫連線成功")

""" 建立cursor物件，用來對資料庫下SQL指令 """
cursor = con.cursor()

""" --------------------------新增資料------------------------- """
'''
""" 執行SQL指令，新增資料 """
cursor.execute("insert into product5(name) values ('綠茶')"),

""" 將變數資料帶入到SQL指令裡面 %s代表要把變數的資料(productName)帶入到那個地方 """
productName = "奶綠加倍"
cursor.execute("insert into product5(name) values (%s)",
               (productName,))  # 注意加,的部分(只有一個也要加)
'''


""" --------------------------更新資料------------------------- """
'''
""" 執行SQL指令，更新資料 """
cursor.execute("update product5 set name='綠茶改紅茶' where id=4")
productName = "綠茶加倍改紅茶加倍"
productId = 5
cursor.execute("update product5 set name=%s where id=%s",
               (productName, productId))  # 注意加,的部分
'''


""" --------------------------刪除資料------------------------- """
'''
cursor.execute("delete from product5 where id=6")
productId2 = 7
cursor.execute("delete from product5 where id=%s",
               (productId2,))
'''


""" --------------------------取得資料------------------------- """
""" 透過fetchone取得一筆資料 """
cursor.execute("select * from product5 where id=5")
data = cursor.fetchone()
print(data)
print(data[1])  # 單獨取出資料

print("---------------------------")
""" 透過fetchall取得多筆資料 """
cursor.execute("select * from product5")
data = cursor.fetchall()
print(data)
print(data[1][1])  # 單獨取出資料

""" 逐一取出資料 """
for n in range(len(data)):
    print(data[n][1])

""" 確定執行 """
con.commit()  # 去看MySQL Workbench會發現出現綠茶、奶綠加倍了

""" 關閉資料庫 """
con.close()
