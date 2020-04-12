from selenium import webdriver
import re

from modules.path import CHROMEDRIVER_PATH, GOOGLE_CHROME_PATH


def getDriver(proxy):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = GOOGLE_CHROME_PATH
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

        chrome_options.add_argument('--proxy-server=socks5://' + proxy)
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
    return driver


def get_proxy():
    driver = getDriver("")
    driver.get("http://spys.one/en/socks-proxy-list/")
    rawList = driver.find_elements_by_css_selector("font.spy14")
    ipList = []
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
    except:
        return False


def find_working_proxy():
    hasInternet = False
    proxyList = get_proxy()
    while not hasInternet:
        proxy = proxyList.pop()
        print("Checking proxy: " + proxy)
        driver = getDriver(proxy)
        driver.set_page_load_timeout(90)
        try:
            driver.get("http://olx.ua")
            hasInternet = has_connection(driver)
        except:
            print("BAD proxy! Finding another..")
            hasInternet = False

        driver.close()
    print("is Connected: " + proxy)

    return proxy
