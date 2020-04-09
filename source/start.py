from modules.proxy_getter import findWorkingProxy
from selenium import webdriver
import chromedriver_binary

good_proxy = findWorkingProxy()

def getDriver():
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=socks5://' + good_proxy)
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    return driver

min_sum = '500'
max_sum = '1000'
search_link = 'https://www.olx.ua/elektronika/noutbuki-i-aksesuary/?search%5Bfilter_float_price%3Afrom%5D='+ min_sum + '&search%5Bfilter_float_price%3Ato%5D=' + max_sum


driver = getDriver()
driver.get(search_link)

ads = driver.find_elements_by_css_selector(".marginright5.link.linkWithHash.detailsLink")

for ad in ads:
    ad_link = ad.get_attribute('href')
    ad_driver = getDriver()
    ad_driver.get(ad_link)
    description = ad_driver.find_element_by_id("textContent").text

    print(ad.text)
    print(description)
    print(ad_link + '\n')
    ad_driver.close()






