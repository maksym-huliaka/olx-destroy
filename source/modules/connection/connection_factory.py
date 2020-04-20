import os
import re
#import chromedriver_binary
from selenium import webdriver

from modules.connection.proxy_tester import filter_proxies


def getDriver(proxy):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    if proxy:
        #chrome_options.add_argument('--proxy-server=socks5://' + proxy)
        chrome_options.add_argument('--proxy-server=%s' % proxy)
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    #driver = webdriver.Chrome(options=chrome_options)
    return driver


def get_proxy():
    driver = getDriver("")
    driver.get("http://spys.one/en/https-ssl-proxy/")
    rawList = driver.find_elements_by_css_selector("font.spy14")
    ipList = []
    for i in rawList:
        ipList.append(i.text)

    regex = re.compile(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+')
    rawList = list(filter(regex.match, ipList))
    driver.close()
    raw_filtered_list = filter_proxies(rawList)
    return raw_filtered_list


def has_connection(driver):
    try:
        driver.find_element_by_id("headerLogo")
        return True
    except:
        return False


def get_proxy_driver():
    hasInternet = False
    proxyList = get_proxy()
    while not hasInternet:
        if not proxyList:
            print("ERROR! proxy list is empty")
            proxyList = get_proxy()
        proxy = proxyList.pop()
        print("Checking proxy: " + proxy)
        proxy_established_driver = getDriver(proxy)
        proxy_established_driver.set_page_load_timeout(90)
        try:
            proxy_established_driver.get("http://olx.ua")
            hasInternet = has_connection(proxy_established_driver)
        except:
            print("BAD proxy! Finding another..")
            hasInternet = False
    print("is Connected: " + proxy)

    return proxy_established_driver
