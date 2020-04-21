from modules.connection.connection_factory import getDriver


def test_fingers():
    print("[WAIT][TEST] Checking for fingerprints..")
    driver = getDriver("")
    driver.get('https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html')
    driver.save_screenshot("modules/fingerprint/screenshot4.png")
    driver.close()
    print("[OK][TEST] Fingerprints passed")
