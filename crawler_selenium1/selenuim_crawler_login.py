from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def ScrollToBottom(t=1):
    x = 0
    while x < t:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 捲動視窗到底部
        time.sleep(2)
        x += 1

# 建立chromedriver的執行黨路徑
options=Options()
options.add_experimental_option("detach", True)
options.chrome_executable_path = "D:\Python 3.10\crawler_selenium\crawler_selenium1\chromedriver.exe"

# 建立driver實體物件 用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)

# 連線到Lativ網站
driver.get("https://www.lativ.com.tw/Home/Login_Register")
usernameInput = driver.find_element(By.ID,"login_ac")
passwordInput = driver.find_element(By.ID,"login_pw")

# 自動輸入帳號密碼
usernameInput.send_keys("0966650857")
passwordInput.send_keys("ky03110311")

# 按下登入按鈕
signinBth = driver.find_element(By.ID,"login_btn")
signinBth.send_keys(Keys.ENTER)

driver.get("https://www.lativ.com.tw/OnSale/2P75DUP/MEN")

ScrollToBottom(3)
tags = driver.find_elements(By.CLASS_NAME,"any_display_name")
for tag in tags:
    print(tag.text)

# prices = driver.find_elements(By.CLASS_NAME,"currency symbol")
# for price in prices:
#     print(price.text)
time.sleep(10)

