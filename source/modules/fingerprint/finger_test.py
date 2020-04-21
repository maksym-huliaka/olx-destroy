from modules.connection.proxy_factory import get_driver


def test_fingers():
    print("[WAIT][TEST] Checking for fingerprints..")
    driver = get_driver("")
    driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    driver.save_screenshot("modules/fingerprint/screenshot4.png")
    html_source = driver.page_source
    print(html_source)
    driver.close()
    print("[OK][TEST] Fingerprints passed")
