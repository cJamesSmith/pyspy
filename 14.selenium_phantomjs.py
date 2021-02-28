from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get('http://www.google.com')
driver.save_screenshot('site.png')
print(driver.title)
driver.quit()