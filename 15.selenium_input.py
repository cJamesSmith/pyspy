from selenium import webdriver
import time

chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://healthreport.zju.edu.cn/ncov/wap/default/index')
driver.find_element_by_xpath('//*[@id="username"]').send_keys('3170101751')  # 学号
driver.find_element_by_xpath('//*[@id="password"]').send_keys('ch13758212508')  # 密码
driver.find_element_by_xpath('//*[@id="dl"]').click()  # 登陆
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[19]/div/div/div[1]').click()  # 是否在校
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[23]/div/input').click()  # 位置
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[26]/div/div/div[2]').click()  # 家人
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[38]/div/div/div/span[2]').click()  # 承诺
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[5]/div/a').click()  # 提交
time.sleep(2)
driver.quit()
