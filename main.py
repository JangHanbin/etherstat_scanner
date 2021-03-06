from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
datetime.now().strftime('%Y-%m-%d %H:%M:%S')

import re
import dbconfig
url = 'https://ethstats.net'

if __name__=='__main__':

    driver = webdriver.Chrome(input('Input Chrome Selenium driver path : '))

    # wait for resource
    driver.implicitly_wait(20)

    driver.get(url)
    actions = ActionChains(driver)
    regex = re.compile(r'(-\s*|:\s*)(.*\d)')
    db = dbconfig.MysqlController()

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
                                pros = list()
                                bar_list = g.find_elements_by_tag_name('g')
                                for bar in bar_list:
                                    tmp = list()
                                    try:
                                        bar.click()
                                    except:
                                        # remove line graph for click bar
                                        driver.execute_script('document.getElementsByClassName("line")[0].remove()')
                                        bar.click()
                                        pass
                                    # actions.move_to_element(bar).click().perform()
                                    tool_tip = driver.find_elements_by_class_name('tooltip-inner')
                                    for tool in tool_tip:
                                        values = tool.text.split('\n')
                                        for value in values:
                                            tmp.append(regex.search(value).group(2))
                                    tmp.append(datetime.now().now().strftime('%Y-%m-%d %H:%M:%S'))
                                    pros.append(tmp.copy())
                                db.insert_values(pros)
                                sleep(10)
        except Exception as e:
            print(e)
            continue


    driver.close()
    print()



