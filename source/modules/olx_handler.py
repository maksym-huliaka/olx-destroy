from entities.publication import Publication
import chromedriver_binary

from modules.proxy_getter import getDriver, find_working_proxy
from modules.publication_filter import sort_by_time


def get_publications(min_sum, max_sum, proxy):

    search_link = 'https://www.olx.ua/elektronika/noutbuki-i-aksesuary/?search%5Bfilter_float_price%3Afrom%5D='+ min_sum + '&search%5Bfilter_float_price%3Ato%5D=' + max_sum
    driver = getDriver(proxy)
    publications =""
    while True:
        try:
            driver.get(search_link)
            publications = driver.find_elements_by_css_selector(".offer-wrapper")
        except:
            print("CANT FIND element by css selector")
            driver = getDriver(find_working_proxy())
            continue
        break


    publications = sort_by_time(publications)
    pubs_list = []

    for pub in publications:
        pub_driver = getDriver(proxy)
        pub_link = pub.find_element_by_class_name('linkWithHash').get_attribute('href')
        pub_desc=""
        while True:
            try:
                pub_driver.get(pub_link)
                pub_desc = pub_driver.find_element_by_id("textContent").text
            except:
                print("CANT FIND element by id")
                pub_driver = getDriver(find_working_proxy())
                continue
            break

        publication = Publication(pub_link, pub.text, pub_desc)
        publication.print()
        pubs_list.append(publication)
        pub_driver.close()
