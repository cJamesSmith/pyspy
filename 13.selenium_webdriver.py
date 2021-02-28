from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.save_screenshot('ss.png')
print(driver.title)
driver.quit()