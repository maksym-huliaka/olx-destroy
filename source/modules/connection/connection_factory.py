# import chromedriver_binary
import os
from gzip import compress, decompress

from lxml import html
from lxml.etree import ParserError
from lxml.html import builder
from selenium import webdriver
from seleniumwire import webdriver

from modules.path import FILE_JS_INJECTOR

script_elem_to_inject = builder.SCRIPT(open(FILE_JS_INJECTOR, 'r').read())


def inject(req, req_body, res, res_body):
    if res.headers.get_content_subtype() != 'html' or res.status != 200 or res.getheader('Content-Encoding') != 'gzip':
        return None
    try:
        parsed_html = html.fromstring(decompress(res_body))
    except ParserError:
        return None
    try:
        parsed_html.head.insert(0, script_elem_to_inject)
    except IndexError:
        return None
    return compress(html.tostring(parsed_html))


def get_driver(proxy):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36")
    chrome_options.add_argument("window-size=1200,800")
    wire_options = None
    if proxy:
        wire_options = {
            'custom_response_handler': inject,
            'proxy': {
                'http': "http://lol:kek@" + proxy,
                'https': "https://lol:kek@" + proxy,
                'no_proxy': 'localhost,127.0.0.1,dev_server:8080',
            }
        }

    driver = webdriver.Chrome(seleniumwire_options=wire_options,
                              executable_path=os.environ.get("CHROMEDRIVER_PATH"),
                              options=chrome_options)
    driver.header_overrides = {'Accept-Encoding': 'gzip'}
    return driver
