import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://ethstats.net'

if __name__=='__main__':
    # driver = webdriver.Chrome(input('Input Chrome Selenium driver path : '))
    driver = webdriver.Chrome('/Users/janghanbin/Downloads/chromedriver')
    # wait for resource
    driver.implicitly_wait(30)
    driver.get(url)
    actions = ActionChains(driver)
    while True:
        try:
            bars = driver.find_elements_by_class_name('big-info')
            for bar in bars:
                # This step for avoid refresh parsing error
                for bar in bar.find_elements_by_class_name('small-title'):
                    if bar.text == 'BLOCK PROPAGATION':
                        gs = bar.find_elements_by_xpath("//histogram/*[name()='svg']/*[name()='g']/*[name()='g']")

                        for g in gs:
                            if g.get_attribute('class') == 'bars':

                                bar_list = g.find_elements_by_tag_name('g')
                                for bar in bar_list:
                                    bar.click()
                                    tool_tip = driver.find_elements_by_class_name('tooltip-inner')
                                    for tool in tool_tip:
                                        values = tool.text.split('\n')
                                        for value in values:
                                            print(value)
                                        print('------------')
                                sleep(10)
        except Exception as e:
            print('propagation graph updated during parsing.')
            print(e)
            continue


    driver.close()
    print()



