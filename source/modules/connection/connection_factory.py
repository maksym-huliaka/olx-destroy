import os
import re
import time

#import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.support.ui import Select

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
        prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                        'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                        'notifications': 2, 'auto_select_certificate': 2,
                                                        'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                        'media_stream_mic': 2, 'media_stream_camera': 2,
                                                        'protocol_handlers': 2,
                                                        'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                        'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                        'metro_switch_to_desktop': 2,
                                                        'protected_media_identifier': 2, 'app_banner': 2,
                                                        'site_engagement': 2,
                                                        'durable_storage': 2}}

        #chrome_options.add_argument('--proxy-server=socks5://' + proxy)
        chrome_options.add_argument('--proxy-server=%s' % proxy)
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    #driver = webdriver.Chrome(options=chrome_options)
    return driver


def get_proxy():
    driver = getDriver("")
    driver.get("http://spys.one/en/https-ssl-proxy/")
    time.sleep(1)
    select = Select(driver.find_element_by_id('xpp'))
    select.select_by_value('2')
    time.sleep(1)
    select = Select(driver.find_element_by_id('xpp'))
    select.select_by_value('2')
    time.sleep(1)
    rawList = driver.find_elements_by_css_selector("font.spy14")
    ipList = []
    for i in rawList:
        ipList.append(i.text)

    regex = re.compile(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+')
    rawList = list(filter(regex.match, ipList))
    rawList = filter_proxies(rawList)
    driver.close()
    return rawList


def has_connection(driver):
    try:
        driver.find_element_by_id("headerLogo")
        return True
    except:
        return False


def get_proxy_driver():
    proxyList = get_proxy()
    hasInternet = False
    for proxy in proxyList:
        print("Checking proxy: " + proxy)
        proxy_established_driver = getDriver(proxy)
        proxy_established_driver.set_page_load_timeout(90)
        try:
            proxy_established_driver.get("http://olx.ua")
            proxy_established_driver.find_element_by_id("headerLogo")
            hasInternet = True
            break
        except:
            proxy_established_driver.close()
            print("BAD proxy! Finding another..")

    if hasInternet is True:
        print("is Connected")
        return proxy_established_driver
    else:
        return get_proxy_driver()



def get_proxy_driver2():
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
