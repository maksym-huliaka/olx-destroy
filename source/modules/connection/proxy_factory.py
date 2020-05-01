import time

from modules.connection.connection_factory import get_driver
from modules.connection.proxy_tester import filter_proxies
from modules.publication_filter import get_current_time

proxy_list=[]

def get_proxy():
    driver = get_driver("")
    driver.get("https://hidemy.name/ru/proxy-list/?maxtime=900&type=hs#list")
    time.sleep(6)
    trs = driver.find_elements_by_css_selector('tr')
    proxies =[]
    for tr in trs:
        proxy = tr.find_elements_by_css_selector("td")[0].text+":"+tr.find_elements_by_css_selector("td")[1].text
        proxies.append(proxy)
    driver.close()
    driver.quit()
    proxies = filter_proxies(proxies)
    print(get_current_time()+" [OK][PROXY] Found: %s" %len(proxies))
    return proxies


def get_proxy_driver():
    print(get_current_time()+" [WAIT][DRIVER] Prepearing proxy driver..")
    global proxy_list
    if not proxy_list:
        print(get_current_time()+" [WAIT][DRIVER] Proxy list is empty! Getting new List...")
        while True:
            try:
                proxy_list = get_proxy()
                if proxy_list:
                    break
                else:
                    print(get_current_time()+" [WAIT][DRIVER] Proxy list is empty! Getting new List...")
            except:
                print(get_current_time()+" [ERROR][PROXY] Can't catch proxies. Trying again..")

    proxy = proxy_list.pop()
    proxy_established_driver = get_driver(proxy)
    print(get_current_time()+" [OK][DRIVER] Driver with proxy is initialized")
    return proxy_established_driver
