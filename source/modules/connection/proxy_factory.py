import time

from modules.connection.connection_factory import get_driver
from modules.connection.proxy_tester import filter_proxies

proxy_list=[]

def get_proxy():
    driver = get_driver("")
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
    proxy_established_driver = get_driver(proxy)
    print("[OK][DRIVER] Driver with proxy is initialized")
    return proxy_established_driver
