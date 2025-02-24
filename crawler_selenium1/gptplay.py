from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

def auto_play_cookie_clicker():
    # 配置 WebDriver（請替換為你的 WebDriver 路徑）

    options = Options()
    options.add_experimental_option("detach", True)
    options.chrome_executable_path = "D:\Python 3.10\crawler_selenium\crawler_selenium1\chromedriver.exe"

    # 打開 Cookie Clicker 網站
    driver = webdriver.Chrome(options=options)
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    # 等待網頁載入
    time.sleep(5)  # 視網速可能需要增加時間

    # 選擇語言（默認選擇英文）
    try:
        english_language = driver.find_element(By.ID, "langSelect-EN")
        english_language.click()
        time.sleep(2)
    except Exception as e:
        print("語言選擇失敗：", e)

    # 定位主要的 Cookie 按鈕
    cookie = driver.find_element(By.ID, "bigCookie")

    # 定位 Cookie 數量顯示
    cookie_count = driver.find_element(By.ID, "cookies")

    # 初始化 ActionChains
    actions = ActionChains(driver)
    actions.click(cookie)

    # 定位升級物品
    items = [driver.find_element(By.ID, f"product{i}") for i in range(18)]

    # 自動點擊和購買邏輯
    start_time = time.time()
    while True:
        # 點擊 Cookie
        actions.perform()

        # 每 5 秒檢查一次升級
        if time.time() - start_time > 5:
            count = int(cookie_count.text.split(" ")[0].replace(",", ""))

            # 從最後一個物品開始嘗試購買
            for item in reversed(items):
                try:
                    item_price = item.get_attribute("class")
                    if "enabled" in item_price:
                        item.click()
                except Exception:
                    pass

            # 重置計時器
            start_time = time.time()

        # 控制總執行時間或手動退出
        time.sleep(0.01)

if __name__ == "__main__":
    auto_play_cookie_clicker()
