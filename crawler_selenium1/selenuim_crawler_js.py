from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def ScrollToBottom(t=1):
    x = 0
    while x < t:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 捲動視窗到底部
        time.sleep(2)
        x += 1

# 建立chromedriver的執行黨路徑
options = Options()
options.chrome_executable_path = "D:\Python 3.10\crawler_selenium\crawler_selenium1\chromedriver.exe"

# 建立driver實體物件 用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)

# 連線到聯合新聞網站
driver.get("https://udn.com/news/breaknews/1")

# 等待網頁跑出 (By.ID, "breaknews"), "h2" 最多10秒
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "breaknews"))  # 這裡一定要兩個括號
)

# 捲動視窗並等待載入更多內容
ScrollToBottom(3)

# 取得標題
titleTags = driver.find_elements(By.TAG_NAME, "h2")
for titleTag in titleTags:
    print(titleTag.text)


driver.close()
