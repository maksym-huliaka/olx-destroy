import sys

from models.publication import Publication
from modules.database.repository.impl import word_repository

from modules.connection.connection_factory import getDriver, get_proxy_driver
from modules.publication_filter import filter_by_time, filter_by_words


def get_clean_publications(publications, url, proxy_established_driver):
    publications = filter_by_time(publications, url)
    pubs_list = []
    words = word_repository.get(url.category)
    short_pub_list=[]
    for pub in publications:
        pub_title = pub.find_element_by_css_selector(".marginright5.link.linkWithHash.detailsLink").text
        pub_link = pub.find_element_by_class_name('linkWithHash').get_attribute('href')
        pub_price = pub.find_element_by_class_name('price').text
        if not filter_by_words(pub_title, words):
            continue
        short_pub_list.append(Publication(pub_link,pub_title,"",pub_price))

    for pub in short_pub_list:
        pub_desc=""
        while True:
            try:
                proxy_established_driver.get(pub.link)
                print(pub.link)
                pub_desc = proxy_established_driver.find_element_by_id("textContent").text
            except:
                print("CANT FIND element by id",sys.exc_info()[0])
                proxy_established_driver.close()
                proxy_established_driver = get_proxy_driver()
                continue
            break

        if not filter_by_words(pub_desc, words):
            print(pub.link)
            continue
        pub.description=pub_desc
        pubs_list.append(pub)
    return pubs_list


def get_publications(url):
    publications = ""
    proxy_established_driver = get_proxy_driver()
    while True:
        try:
            proxy_established_driver.get(url.url)
            publications = proxy_established_driver.find_elements_by_class_name("offer-wrapper")
        except:
            print("CANT find element by css selector! Trying to find another proxy..",sys.exc_info()[0])
            proxy_established_driver = get_proxy_driver()
            continue
        break
    clean_publications = get_clean_publications(publications, url, proxy_established_driver)
    proxy_established_driver.close()
    return clean_publications

