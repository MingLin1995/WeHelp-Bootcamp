# #17 文件編號是一個Objectld物件，所以要先從bson.objectid封包載入
from bson.objectid import ObjectId
# 載入pymongo套件 # pip install pymongo[srv]
import pymongo

# 連線到 MongoDB 雲端資料庫
""" 
1.回去MyCluster網頁 Connect點下去
2.Connect to your application
3.python 版本選第二新的比較不會有問題
"""
# root(帳號):root123(密碼)
client = pymongo.MongoClient(
    "mongodb+srv://root:root123@mycluster.wevxghs.mongodb.net/?retryWrites=true&w=majority")

# 把資料放進資料庫中
db = client.website  # 選擇操作website資料庫 (.資料庫名稱)
collection = db.users  # 選擇操作users集合 (.集合名稱 也就是table)

# 把資料新增到集合中 集合.insert_one(文件資料)
""" collection.insert_one({
    "name": "Ming",
    "gender": "男"
})
print("資料新增成功") """

# 回到MyCluster collections點下去 就可以看到剛剛新增的資料了

""" ---------------#16 MongoDB 新增資料---------------- """
# 新增資料 集合.insert_one(文件資料)
""" collection.insert_one({
    "name": "test",
    "email": "test@gmai.com",
    "passwoed": "test123",
    "level": 1
})
print("單筆資料新增成功") """

# 取得編號 inserted_id
""" result = collection.insert_one({
    "name": "test2",
    "email": "test2@gmai.com",
    "password": "test123",
    "level": 2
})
print(result.inserted_id)
print("編號取得成功") """

# 新增多個資料 集合.insert_many([{文件資料2},{文件資料2}])
""" result2 = collection.insert_many([
    {
        "name": "test3",
        "email": "test3@gmai.com",
        "password": "test123",
        "level": 3
    },
    {
        "name": "test4",
        "email": "test4@gmai.com",
        "password": "test123",
        "level": 4
    }
])
print("多筆資料新增成功")
# 取得多個編號 inserted_ids
print(result2.inserted_ids)
print("編號取得成功") """


""" ---------------#17 MongoDB 取得資料---------------- """
""" # 取得一筆資料 集合.find_one()
data = collection.find_one()
print(data)
print("--------------------------------------------------") """

""" # 根據編號取得資料 集合.find_one(Objectld("文件編號"))
data2 = collection.find_one("64c9146457feb61488d9c4d8")
print(data2)  # 無法取得資料，會顯示None

# 文件編號是一個Objectld物件，所以要先從bson.objectid封包載入
# from bson.objectid import ObjectId
data2 = collection.find_one(ObjectId("64c9146457feb61488d9c4d8"))
print(data2)  # 無法取得資料，會顯示None

# 取得欄位 文件資料["欄位名稱"] 同字典操作
print(data2["_id"])
print(data2["email"])
print("--------------------------------------------------") """

""" # 取得多筆文件資料
# 集合.find()
data3 = collection.find()  # 會取得Cursor物件
# 透過迴圈將Cursor物件逐一取出文件
for x in data3:
    print(x)

# 上一個迴圈已經取出資料，所以data3是空的，所以要再取得新的物件
data3 = collection.find()
# 只取得名子
for y in data3:
    print(y["name"]) """

""" ---------------#18 MongoDB 更新資料---------------- """
# 集合.update_one(篩選條件,更新的資訊)
# 字串型態 $set 覆蓋(若原本存在)/新增欄位(若原本不存在)
""" result = collection.update_one(
    {"email": "test1@gmail.com"},
    # {"$set": {"email": "test1@gmail.com"}} #覆蓋(若原本存在)
    # {"$set": {"description": "Hello"}} #新增欄位(若原本不存在)
    {"$unset": {"description": ""}}  # 清除單一欄位 $unset 後面的值寫多少都不重要，重點是前面的欄位
)
# 取得更新的結果
# matched_count符合篩選條件的數量
print("符合篩選條件的數量", result.matched_count)
# modified_count實際完成更新的數量
print("實際完成更新的數量", result.modified_count) """

""" # 數字型態 $inc 加減數字欄位，數字為要增加或減少的，若要減少就是用負號表示
result = collection.update_one(
    {"email": "test1@gmail.com"},
    {"$inc": {"level": 99}}  # 原本1+99=100
)
print("符合篩選條件的數量", result.matched_count)
print("實際完成更新的數量", result.modified_count) """

""" # 對數字欄位乘除 $mul
result = collection.update_one(
    {"email": "test1@gmail.com"},
    {"$mul": {"level": 0.01}}  # 原本100*0.01=1
)
print("符合篩選條件的數量", result.matched_count)
print("實際完成更新的數量", result.modified_count)
 """

""" # 多筆資料更新 update_man
result = collection.update_many(
    {"level": 2},
    {"$set": {"level": 666}}

)
print("符合篩選條件的數量", result.matched_count)
print("實際完成更新的數量", result.modified_count) """

""" ---------------#19 MongoDB 刪除資料---------------- """
""" # 刪除一筆資料(非單一欄位) 集合.delete_one(篩選條件)
result = collection.delete_one({
    "email": "test4@gmai.com"
})
# 實際完成刪除的數量 deleted_count
print("實際完成刪除的數量", result.deleted_count) """

""" # 刪除多筆資料 集合.delete_many(篩選條件)
result = collection.delete_many({
    "level": 666
})
# 實際完成刪除的數量 deleted_count
print("實際完成刪除的數量", result.deleted_count) """

""" ---------------#20 MongoDB 篩選資料---------------- """
""" # 新增多個資料 集合.insert_many([{文件資料2},{文件資料2}])
result2 = collection.insert_many([
    {
        "name": "test1",
        "email": "test1@gmail.com",
        "password": "test123",
        "level": 1
    },
    {
        "name": "test2",
        "email": "test2@gmail.com",
        "password": "test123",
        "level": 2
    }, {
        "name": "test3",
        "email": "test3@gmail.com",
        "password": "test123",
        "level": 1
    }, {
        "name": "test4",
        "email": "test4@gmail.com",
        "password": "test123",
        "level": 2
    },
]) """

""" # 篩選一筆資料 集合.find_one(篩選條件)
doc = collection.find_one({
    "email": "test1@gmail.com"
})
print("取得的資料", doc)  # 會取出所有字典 """

# 複合篩選條件(多筆資料) 集合.find(篩選條件)
# 同時滿足條件 "$and":[{條件一},{條件二}]
# 滿足任一條件 "$or":[{條件一},{條件二}]
""" doc = collection.find({
    "$and": [
        {"level": 1},
        {"password": "test123"}
    ]
})
# print("取得的資料", doc) # 會取得Cursor物件
# 透過迴圈將Cursor物件逐一取出文件
for x in doc:
    print("取得的資料", x) """

# 篩選結果排序
# 集合.find(篩選條件{}代表不篩選直接排序,sort=[("要排序的欄位名稱",排序方式)])
# 排序方式 小到大 pymongo.ASCENDING ; 大到小 .DESCENDING
doc = collection.find(
    {
        "$or": [
            {"email": "test1@gmail.com"},
            {"level": 2}
        ]
    },
    sort=[("level", pymongo.DESCENDING)]
)
# print("取得的資料", doc) # 會取得Cursor物件
# 透過迴圈將Cursor物件逐一取出文件
for x in doc:
    print(x["name"])
