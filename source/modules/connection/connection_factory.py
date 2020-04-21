import os
import re
import time

import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from modules.connection.proxy_tester import filter_proxies

def getDriver(proxy):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-extensions')
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36")
    chrome_options.add_argument("window-size=1200,800")
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
    #driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options)
    return driver


proxy_list=[]


def get_proxy():
    driver = getDriver("")
    driver.get("https://hidemy.name/ru/proxy-list/")
    time.sleep(6)
    trs = driver.find_elements_by_css_selector('tr')
    proxies =[]
    for tr in trs:
        proxy = tr.find_elements_by_css_selector("td")[0].text+":"+tr.find_elements_by_css_selector("td")[1].text
        proxies.append(proxy)
    driver.close()
    proxies = filter_proxies(proxies)
    print("[OK][PROXY] Found: %s" %len(proxies))
    return proxies


def get_proxy_driver():
    print("[WAIT][DRIVER] Prepearing proxy driver..")
    global proxy_list
    if not proxy_list:
        print("[WAIT][DRIVER] Proxy list is empty! Getting new List...")
        proxy_list = get_proxy()
    proxy = proxy_list.pop()
    proxy_established_driver = getDriver(proxy)
    print("[OK][DRIVER] Driver with proxy is initialized")
    return proxy_established_driver
