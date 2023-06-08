#載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By #要使用By就要先載入模組
#設定Chrome Driver的執行檔路徑
options=Options()
options.chrome_executable_path=r"C:\Users\林右銘\Desktop\python\selenium\chromedriver.exe" 
#建立Driver物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options) 
#連線到PTT股票版

#取得股票版中的文章標題
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
#print(driver.page_source) #取得網頁原始碼
tags=driver.find_elements(By.CLASS_NAME,"title") #要抓很多個，所以element+s ;搜尋class屬性中所有title的標籤
#print(tage) #標題的標籤會以列表的狀態顯示出來
for tag in tags:
    print(tag.text) #把列表中的標籤一個一個取出來，取得標籤內部的文字
print("-------------------------------------")
#取得上五頁的文章標題
for click in range(5):
    link=driver.find_element(By.LINK_TEXT,"‹ 上頁") #只取一個所以element不加s
    link.click() #模擬使用者點擊連結標籤
    tags=driver.find_elements(By.CLASS_NAME,"title")
    for tag in tags:
        print(tag.text)
    print("--換頁--")
print("-------------------------------------")
#取得上三頁的文章標題
count=0
while count <3 :
    link=driver.find_element(By.LINK_TEXT,"‹ 上頁") #只取一個所以element不加s
    link.click() #模擬使用者點擊連結標籤
    tags=driver.find_elements(By.CLASS_NAME,"title")
    for tag in tags:
        print(tag.text)
    print("--換頁--")
    count+=1
print("-------------------------------------")    
    
driver.close() 


