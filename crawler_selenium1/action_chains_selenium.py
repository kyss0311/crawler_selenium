# https://www.youtube.com/watch?v=OISEEL5eBqg
# action chains 自動玩遊戲
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
options.chrome_executable_path = "D:\Python 3.10\crawler_selenium\crawler_selenium1\chromedriver.exe"



def waitfor_id(id):
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, id))  # 這裡一定要兩個括號
    )

# 建立driver實體物件 用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # 視窗最大化
driver.get("https://orteil.dashnet.org/cookieclicker/")

# 等待網頁跑出 (By.ID, "languageSelectHeader") 最多20秒
waitfor_id("languageSelectHeader")

# 找到中文 點擊
link = driver.find_element(By.ID, "langSelect-ZH-CN")
link.click()

# 等待網頁跑出 (By.ID, "bakeryName") 最多20秒
waitfor_id("bakeryName")

driver.implicitly_wait(5)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")

items = [driver.find_element(By.ID, "productPrice"+str(i))for i in range(19)]

value = [items[i].text for i in range(19)]
for x in range(19):
    if value[x] == '':
        value[x] = '0'

print(value)
actions = ActionChains(driver)

for i in range(5000):
    actions.click(cookie)
    actions.perform()
    count = cookie_count.text.replace(" 块饼干", "").replace("每秒： 0", "")
    print(count)
    values = 0
    for j in range(18, 0, -1):
        if value[j] != '0':
            values += 1
    print(values)
    # for j in range(values):
    #     if int(value[j]) <= int(count):
    #         upgrade_actions = ActionChains(driver)
    #         upgrade_actions.move_to_element(items[j])
    #         upgrade_actions.click()
    #         upgrade_actions.perform()




# 寫actions.perform()才會執行上面的動作
# actions.perform()
