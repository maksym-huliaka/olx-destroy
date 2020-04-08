from selenium import webdriver
import secrets

def getProxy():
    driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
    driver.get("http://spys.one/en/socks-proxy-list/")
    elem = driver.find_elements_by_css_selector("font.spy14")
    i = 0
    proxy_array=[]
    for el in elem:
        if i==4:
            proxy_array.append(el.text)
            i = 0
        i = i+1

    proxy_array = proxy_array[:len(proxy_array)-3]
    driver.close()
    return secrets.choice(proxy_array)
