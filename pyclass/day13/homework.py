from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

with webdriver.Chrome(options=options) as driver:
    wait = WebDriverWait(driver, 10)

    driver.get("https://data.stats.gov.cn/easyquery.htm?cn=A01")

    data_head = driver.find_element_by_xpath('//*[@id="table_main"]/thead')
    data_head = data_head.find_elements_by_tag_name('th')
    head_list = []
    for row in data_head:
        head_list.append(row.text)
    print(head_list)
    data_body = driver.find_element_by_xpath(
        '//*[@id="main-container"]/div[2]/div[2]/div[2]/div/div[3]/table/tbody').get_attribute('innerText')
    rows = str(data_body).split('\n')
    data_list = []
    for row in rows:
        data_list.append(row.split('\t'))
    print(data_list)

