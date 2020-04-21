from modules.connection.proxy_factory import get_driver


def test_fingers():
    print("[WAIT][TEST] Checking for fingerprints..")
    driver = get_driver("")
    driver.get('https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html')
    driver.save_screenshot("modules/fingerprint/screenshot4.png")
    driver.close()
    print("[OK][TEST] Fingerprints passed")
