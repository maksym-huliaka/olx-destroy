from selenium import webdriver
import re

def getProxy():
    driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
    driver.get("http://spys.one/en/socks-proxy-list/")
    rawList = driver.find_elements_by_css_selector("font.spy14")
    ipList=[]
    for i in rawList:
        ipList.append(i.text)

    regex = re.compile(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+')
    rawList = list(filter(regex.match, ipList))
    driver.close()
    return rawList



def has_connection(driver):
    try:
        driver.find_element_by_id("headerLogo")
        return True
    except: return False



def findWorkingProxy():
    hasInternet = False
    proxyList = getProxy()
    while not hasInternet:
        PROXY = proxyList.pop()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=socks5://' + PROXY)
        driver = webdriver.Chrome(executable_path=r"../driver/chromedriver.exe", options=chrome_options)
        driver.get("http://olx.ua")
        hasInternet = has_connection(driver)
        if not hasInternet:
            driver.close()
    print("isConnected")
    print(PROXY)
    return PROXY
