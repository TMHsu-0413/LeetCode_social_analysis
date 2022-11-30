import requests
import json
import collections
import time
import bisect
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Edge()

# Get US users current contest ranking
def get_rank(user,state):
    if state == 'US':
        driver.get(f'https://leetcode.com/{user}')
    elif state == 'CN':
        driver.get(f'https://leetcode.cn/u/{user}')
    try:
        cur = None
        counter = 0
        while cur == None and counter < 20:
            html_source = driver.page_source
            Soup = BeautifulSoup(html_source,'html.parser')
            cur = Soup.find('div',class_='text-label-1 dark:text-dark-label-1 flex items-center text-2xl')
            counter += 1
            time.sleep(.2)
        return int(cur.text.replace(',',''))
    except:
        return 0