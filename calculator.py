#開倉建議計算
TA=float(input("總資金:")) 
Stop_Loss=float(input("停損比率(百分比):"))/100
Stop_Loss_Amount=TA*Stop_Loss 
LS=input("做多輸入L，做空輸入S:")
if LS=="L" :
    Long_in=float(input("做多進場價格:"))
    Long_out=float(input("做多停損價格:"))
    Long_Loss_Point=Long_in-Long_out
    Long_Open_U=Stop_Loss_Amount/Long_Loss_Point*Long_in
    Long_Open_Unit=Long_Open_U/Long_in
    print("建議開倉大小（U）:",Long_Open_U,"\n建議開倉大小（顆數）",Long_Open_Unit)
elif LS=="S" :
    Short_in=float(input("做空進場價格:"))
    Short_out=float(input("做空停損價格:"))
    Short_Loss_Point=Short_out-Short_in
    Short_Open_U=Stop_Loss_Amount/Short_Loss_Point*Short_in
    Short_Open_Unit=Short_Open_U/Short_in
    print("建議倉大小（U）:",Short_Open_U,"\n建議開倉大小（顆數）",Short_Open_Unit)
