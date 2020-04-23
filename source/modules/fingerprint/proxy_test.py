import time

from modules.connection.connection_factory import get_driver

def check_driver_2ip(proxy):
    driver = get_driver(proxy)
    driver.get("http://2ip.ru")
    time.sleep(10)
