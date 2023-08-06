#載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import time 
from selenium.webdriver.common.keys import Keys #額外載入keys的模組，幫助送出enter的按鍵
#設定Chrome Driver的執行檔路徑
options=Options()
options.chrome_executable_path=r"C:\Users\林右銘\Desktop\python\selenium\chromedriver.exe" 
#建立Driver物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options) 

#連線到LeetCode登入頁面
driver.get("https://leetcode.com/accounts/login/")
# 保留瀏覽器窗口5秒，不然還沒跑好網頁就關閉了
time.sleep(5)

#輸入帳號密碼，按下登入按鈕 (觀察網頁，發現有個標籤，帳號的部分，id=id_login；密碼的部分，id=id_password；送出按鈕 id=signin_btn)
usernameInput=driver.find_element(By.ID,"id_login")
passwordInput=driver.find_element(By.ID,"id_password")
usernameInput.send_keys("1234596@gmail.com")
passwordInput.send_keys("123456")
signinBtn=driver.find_element(By.ID,"signin_btn") #按下輸入的按鈕
signinBtn.send_keys(Keys.ENTER) #按下的功能
#等待登入完成
time.sleep(10)

#連線到登入後才能取得資料的頁面，並取得想要的資料 #登入後選擇problems
driver.get("https://leetcode.com/problemset/all/") #登入後典點擊problems的選項
time.sleep(10)
statElement=driver.find_element(By.CSS_SELECTOR,"[data-difficulty=TOTAL]")#抓取class選擇器的標籤
print(statElement.text) #會發現有 ALL、以刷題數、總題數
print("-----")
columns=statElement.text.split("\n") #根據換行符號切割成列表
print(columns)
print("-----")
print("已完成刷提數量",columns[1])#取得第二個項目
driver.close()