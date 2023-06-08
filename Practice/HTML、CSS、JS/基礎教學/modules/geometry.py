#在geometry模組中定義幾何運算功能

#計算兩個點(x1,y1與x2,y2)的距離
def distance(x1,y1,x2,y2):
    return((x2-x1)**2+(y2-y1)**2)**0.5 #x2-x1的平方加y2-y1的平方，開根號

#計算線段的斜率
def slope(x1,y1,x2,y2):
    return(y2-y1)/(x2-x1)