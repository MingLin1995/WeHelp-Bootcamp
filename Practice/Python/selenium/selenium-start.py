
#搜尋ChromeDriver 設定→說明→關於Chrome就能看到版本，依照版本去下載
#載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#設定Chrome Driver的執行檔路徑
options=Options()
options.chrome_executable_path=r"C:\Users\林右銘\Desktop\python\selenium\chromedriver.exe" #前面加上r才不會造成\的編碼錯誤
#建立Driver物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options) #打開瀏覽器
driver.maximize_window() #視窗最大化
driver.get("http://www.google.com/") #跑到GOOEL的網址
driver.save_screenshot("screenshot-google.png") #網頁截圖，自訂檔案名稱，會跑到資料夾中
driver.get("http://www.ntu.edu.tw/")
driver.save_screenshot("screenshot-ntu.png") 
driver.close() #結果為，打開chrome，跑到GOOGLE、台大的首頁，截圖，然後關閉
