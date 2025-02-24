# 每次使用selenuim都要檢查chromedriver的版本跟 chrome版本是否相同
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
options.add_experimental_option("detach", True)
options.chrome_executable_path = "D:\Python 3.10\crawler_selenium\crawler_selenium1\chromedriver.exe"

# 建立driver實體物件 用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # 視窗最大化
driver.get("https://www.google.com/")
driver.save_screenshot("screenshot-google.png")
driver.get("https:///www.youtube.com/")

# 取得網頁標題
print(driver.title)

# 找到輸入欄 輸入NBA 並且搜尋 螢幕別圖
search = driver.find_element(By.NAME, "search_query")
search.clear()  # 先清除預設文字
search.send_keys("NBA")
search.send_keys(Keys.RETURN)
# driver.save_screenshot("screenshot-yt.png")

# 等待網頁跑出 (By.ID, "title") 最多10秒
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "title"))  # 這裡一定要兩個括號
)

time.sleep(5)
link = driver.find_element(By.LINK_TEXT, "40歲老當益壯 LeBron James飛身拉桿暴扣 ｜ NBA美國職籃")
link.click()
time.sleep(5)
# 回上一頁
driver.back()

# 回下一頁
# driver.forward()

# 捲動視窗並等待載入更多內容
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 捲動視窗到底部
time.sleep(2)


# 取得標題
tags = driver.find_elements(By.ID, "video-title")
for tag in tags:
    print(tag.text)





# time.sleep(5)
# driver.close()
