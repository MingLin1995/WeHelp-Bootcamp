#載入內建的sys模組並取得系統相關的資訊 (import 模組名稱)
import sys
print(sys.platform) #印出作業系統
print(sys.maxsize) #印出整數型態的最大值

import sys as x #自定模組別名為X
print(x.platform) #印出作業系統
print(x.maxsize) #印出整數型態的最大值

# #建立geometry模組，載入使用(因為路徑有更動，所以跑出來會錯誤，可以先將geometry.py移到python的資料夾)
# import geometry 
# result=geometry.distance(1,1,5,5,)  #模組名稱.模組內的函式名稱
# print(result)
# result=geometry.slope(1,2,5,6)
# print(result)

#調整搜尋模組的路徑
import sys
print(sys.path) #印出搜尋模組的路徑(會將python的模組，依這些路徑的順序搜尋出來)
print("----------")
#若geometry.py放在python的資料夾內可以正常執行
#但如果放到額外新增的modules資料夾，會發生錯誤
#因此要新增搜尋模組的路徑
import sys
sys.path.append("基礎教學\modules")
#sys.path.append("modules")  #在模組的搜尋路徑列表中，新增路徑
print(sys.path) #會跑出 基礎教學\\modules 的路徑
import geometry
print(geometry.distance(1,1,5,5,))

