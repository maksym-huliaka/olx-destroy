from selenium import webdriver
from scripts.proxy_getter import getProxy

def has_connection(driver):
    try:
        driver.find_element_by_xpath('//span[@jsselect="heading" and @jsvalues=".innerHTML:msg"]')
        return False
    except: return True

hasInternet = False
while not hasInternet:
    PROXY = getProxy()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(executable_path=r"../driver/chromedriver.exe", options=chrome_options)
    driver.get("http://olx.ua")
    hasInternet = has_connection(driver)
    if not hasInternet:
        driver.close()
print("isConnected")







