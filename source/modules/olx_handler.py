from entities.publication import Publication
import chromedriver_binary

from modules.proxy_getter import getDriver


def getPublications(min_sum, max_sum, proxy):

    search_link = 'https://www.olx.ua/elektronika/noutbuki-i-aksesuary/?search%5Bfilter_float_price%3Afrom%5D='+ min_sum + '&search%5Bfilter_float_price%3Ato%5D=' + max_sum
    driver = getDriver(proxy)
    driver.get(search_link)

    publications = driver.find_elements_by_css_selector(".marginright5.link.linkWithHash.detailsLink")
    pubs_list = list
    for pub in publications:
        pub_driver = getDriver(proxy)
        pub_link = pub.get_attribute('href')
        pub_driver.get(pub_link)

        pub_desc = pub_driver.find_element_by_id("textContent").text

        publication = Publication(pub_link, pub.text, pub_desc)
        publication.print()
        pubs_list.append(publication)

        pub_driver.close()