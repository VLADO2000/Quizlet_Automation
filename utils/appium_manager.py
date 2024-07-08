from contextlib import contextmanager
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService


"""
Main reasom of appium_manager existance is levaraging of 
appium automation process to get app activity for 
desired capabilities 
"""

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'

@contextmanager
def appium_service():
    service = AppiumService()
    try:
        service.start(
            args=["--address", APPIUM_HOST, "-p", str(APPIUM_PORT)],
            timeout_ms=20000,
        )
        yield service
    finally:
        service.stop()


def create_android_driver(custom_capabilities):
    options = UiAutomator2Options()
    options.platform_name = "Android"

    options.load_capabilities(custom_capabilities)

    return webdriver.Remote(
        f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


@contextmanager
def android_driver(options):
    driver = None
    try:
        driver = create_android_driver(options)
        yield driver
    except Exception as e:
        raise
    finally:
        if driver:
            driver.quit()

