import time

from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome("C:\chromedriver.exe")
    context.driver.maximize_window()


def after_scenario(context, scenario):
    print('Driver is closing now')
    context.driver.close()
