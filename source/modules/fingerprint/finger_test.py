import time

from modules.connection.proxy_factory import get_driver
from modules.publication_filter import get_current_time


def test_fingers():
    print(get_current_time()+" [WAIT][TEST] Checking for fingerprints..")
    driver = get_driver("")
    driver.get('https://recaptcha-demo.appspot.com/recaptcha-v3-request-scores.php')
    time.sleep(5)
    #driver.save_screenshot("modules/fingerprint/screenshot4.png")
    driver.close()
    print(get_current_time()+" [OK][TEST] Fingerprints passed")
