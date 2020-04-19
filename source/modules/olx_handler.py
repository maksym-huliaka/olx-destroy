import sys
import traceback

from models.publication import Publication
from modules.database.repository.impl import word_repository

from modules.proxy_getter import getDriver, find_working_proxy
from modules.publication_filter import filter_by_time, filter_by_words

def get_clean_publications(publications, proxy, url):
    publications = filter_by_time(publications, url)
    pubs_list = []
    words = word_repository.get(url.category)
    pub_driver = getDriver(proxy)
    for pub in publications:
        pub_title = pub.find_element_by_css_selector(".marginright5.link.linkWithHash.detailsLink").text
        pub_link = pub.find_element_by_class_name('linkWithHash').get_attribute('href')
        pub_price = pub.find_element_by_class_name('price').text
        if not filter_by_words(pub_title, words):
            continue

        pub_desc=""
        while True:
            try:
                pub_driver.get(pub_link)
                print(pub_link)
                pub_desc = pub_driver.find_element_by_id("textContent").text
            except:
                print("CANT FIND element by id",sys.exc_info()[0])
                pub_driver = getDriver(find_working_proxy())
                continue
            break

        if not filter_by_words(pub_desc, words):
            continue

        publication = Publication(pub_link, pub_title, pub_desc, pub_price)
        pubs_list.append(publication)
    pub_driver.close()
    return pubs_list


def get_publications(url):
    proxy = find_working_proxy()
    publications = ""
    driver = getDriver(proxy)
    while True:
        try:
            driver.get(url.url)
            publications = driver.find_elements_by_class_name("offer-wrapper")
        except:
            print("CANT find element by css selector! Trying to find another proxy..",sys.exc_info()[0])
            driver = getDriver(find_working_proxy())
            continue
        break
    clean_publications = get_clean_publications(publications, proxy, url)
    driver.close()
    return clean_publications

