#載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import time #要使瀏覽器有等待的動作
#設定Chrome Driver的執行檔路徑
options=Options()
options.chrome_executable_path=r"C:\Users\林右銘\Desktop\python\selenium\chromedriver.exe" 
#建立Driver物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options) 
#連線到LinkedIn工作搜尋網頁
driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")

#捲動視窗N次並等待瀏覽器載入更多內容
n=0
while n<3: #捲動三次
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #執行(execute)JacaScript的程式碼
    time.sleep(5) #要給予程式等待時間，不然會開啟網頁後馬上抓標題，才捲動視窗。
    n+=1
    
#取得網頁中工作的標題
titleTags=driver.find_elements(By.CLASS_NAME,"base-search-card__title") #看圖1
for titleTag in titleTags:
    print(titleTag.text)
    
driver.close()