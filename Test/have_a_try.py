from selenium import webdriver


driver = webdriver.Chrome()
url_1 = 'https://www.baidu.com'
url_2 = 'https://www.douban.com'
driver.get(url_1)
driver.execute_script('window.open("%s")' % url_2)

