from entities.publication import Publication

from modules.proxy_getter import getDriver, find_working_proxy
from modules.publication_filter import filter_by_time, filter_by_words

def get_clean_publications(publications, proxy):
    publications = filter_by_time(publications)
    pubs_list = []

    pub_driver = getDriver(proxy)
    for pub in publications:
        pub_title = pub.find_element_by_css_selector(".marginright5.link.linkWithHash.detailsLink").text
        pub_link = pub.find_element_by_class_name('linkWithHash').get_attribute('href')
        pub_price = pub.find_element_by_class_name('price').text
        if not filter_by_words(pub_title):
            continue

        pub_desc=""
        while True:
            try:
                pub_driver.get(pub_link)
                print(pub_driver.page_source())
                pub_desc = pub_driver.find_element_by_id("textContent").text
            except:
                print("CANT FIND element by id")
                pub_driver = getDriver(find_working_proxy())
                continue
            break

        if not filter_by_words(pub_desc):
            continue

        publication = Publication(pub_link, pub_title, pub_desc, pub_price)
        pubs_list.append(publication)
    pub_driver.close()
    return pubs_list


def get_publications(min_sum, max_sum):
    proxy = find_working_proxy()
    search_link = 'https://www.olx.ua/elektronika/noutbuki-i-aksesuary/?search%5Bfilter_float_price%3Afrom%5D='+ min_sum \
                  + '&search%5Bfilter_float_price%3Ato%5D=' + max_sum
    publications = ""
    driver = getDriver(proxy)
    while True:
        try:
            driver.get(search_link)
            publications = driver.find_elements_by_css_selector(".offer-wrapper")
        except:
            print("CANT find element by css selector! Trying to find another proxy..")
            driver = getDriver(find_working_proxy())
            continue
        break
    clean_publications = get_clean_publications(publications, proxy)
    driver.close()
    return clean_publications

