import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://fund.cnyes.com/Fixedincome/search.aspx'

# 建立chromedriver的執行黨路徑
options=Options()
options.add_experimental_option("detach", True)
options.chrome_executable_path = "D:\Python 3.10\crawler_selenium\crawler_selenium1\chromedriver.exe"

# 建立driver實體物件 用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
driver.get(url=url)

# 計價幣別
driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_DD_classCurrent"]').click()
driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_DD_classCurrent"]/option[1]').click()

# 投資區域（全球市場）
driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_DropDownList1"]').click()
driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_DropDownList1"]/option[8]').click()

# 基金組別（高收益債）
driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_DropDownList2"]').click()
driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_DropDownList2"]/option[7]').click()

# 年化配息率（0%）
driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/div[4]/div[1]/select[1]').click()
driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/div[4]/div[1]/select[1]/option[2]').click()

# 至（10%以上）
driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/div[4]/div[1]/select[2]').click()
driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/div[4]/div[1]/select[2]/option[10]').click()

# 配息頻率
driver.find_element(By.XPATH, '//*[@id="div_type"]').click()
driver.find_element(By.XPATH, '//*[@id="div_type"]/option[1]').click()

# 搜尋
driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/div[4]/div[3]/button').click()

time.sleep(5)

# 一年績效排序
driver.find_element(By.XPATH, '/html/body/div[2]/section[3]/div/div[4]/table[2]/thead/tr/th[3]/select').click()
driver.find_element(By.XPATH, '/html/body/div[2]/section[3]/div/div[4]/table[2]/thead/tr/th[3]/select/option[5]').click()

time.sleep(5)

html_source = driver.page_source

# driver.close()

soup = BeautifulSoup(html_source, 'lxml')

fund_dict = {
    '基金名稱': [],
    '淨值': [],
    '三年績效': [],
    '配息日': [],
    '配息金額': [],
    '年化配息率': [],
    '晨星評級': [],
    '連結': []
}

for tr in soup.select_one('tbody').select('tr'):

    morning_star = len(tr.select('td')[5].select('li.on'))


    fund_dict['基金名稱'].append(tr.select('td')[0].text.strip())
    fund_dict['淨值'].append(tr.select('td')[1].text.strip().split('\n')[0])
    fund_dict['三年績效'].append(tr.select('td')[2].text.strip())
    fund_dict['配息日'].append(tr.select('td')[3].text.strip().split('\n')[-1].strip())
    fund_dict['配息金額'].append(tr.select('td')[4].text.strip().split('\n')[0].strip())
    fund_dict['年化配息率'].append(tr.select('td')[4].text.strip().split('\n')[-1].strip())
    fund_dict['晨星評級'].append(morning_star)
    fund_dict['連結'].append('https://fund.cnyes.com' + tr.select('td')[0].a['href'].strip().replace(' ', '%20'))

print(fund_dict)



df = pd.DataFrame(fund_dict)
df.set_index('基金名稱', inplace=True)
print(df)



date = datetime.today().strftime("%Y%m%d")
file_name = '{}_全球高收益債基金.csv'.format(date)
df.to_csv(file_name, encoding='utf_8_sig')