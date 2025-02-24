from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def GetTitle():
    tags = driver.find_elements(By.CLASS_NAME, "title")  # 找到html 的 class標籤名稱
    for tag in tags:
        print(tag.text)

def GetMoreTitle(time = 1):
    x = 0
    while x < time:
        link = driver.find_element(By.LINK_TEXT, "‹ 上頁")  # 找到html中標籤內的文字
        link.click()
        GetTitle()
        x += 1

# 建立chromedriver的執行黨路徑
options = Options()
options.chrome_executable_path = "D:\Python 3.10\crawler_selenium\crawler_selenium1\chromedriver.exe"

# 建立driver實體物件 用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # 視窗最大化
# 連線到ptt stock版 印出標題
driver.get("https://www.ptt.cc/bbs/stock/index.html")
# print(driver.page_source)

# 取得首頁文章標題
GetTitle()
# 取得上一頁的文章標題
GetMoreTitle()

driver.close()