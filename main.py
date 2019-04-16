import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://ethstats.net'

if __name__=='__main__':
    driver = webdriver.Chrome('/Users/janghanbin/Downloads/chromedriver')
    # wait for resource
    driver.implicitly_wait(20)
    driver.get(url)
    actions = ActionChains(driver)
    bars = driver.find_elements_by_class_name('big-info')

    for bar in bars:
        if bar.text == 'BLOCK PROPAGATION':
            his = bar.get_attribute('histogram')

            gs = bar.find_elements_by_xpath("//histogram/*[name()='svg']/*[name()='g']/*[name()='g']")

            for g in gs:
                if g.get_attribute('class') == 'bars':
                    bar_list = g.find_elements_by_tag_name('g')
                    for bar in bar_list:
                        bar.click()
                        print('hi')


    driver.close()
    print()



