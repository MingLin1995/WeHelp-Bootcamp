#先建立最外層式專案資料夾(package)，新增封包資料夾(geometry)，在封包資料夾內新增__init__.py(一定要有)
#在開始建立模組(line、point)


# 主程式 
import geometry.point #import 封包名稱.模組名稱 
result=geometry.point.distance(3,4) #使用封包底下的函式
print("點的距離",result)

import geometry.line
result=geometry.line.slope(1,1,3,3)
print("斜率",result)

import geometry.line as line #後面也可以使用as建立模組別名
result=line.len(1,1,5,5)
print("線的距離",result)