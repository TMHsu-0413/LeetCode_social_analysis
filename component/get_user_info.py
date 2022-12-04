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
driver = webdriver.Firefox()

# Get US users current contest ranking
def get_info(user,state):
    if state == 'US':
        driver.get(f'https://leetcode.com/{user}')
    elif state == 'CN':
        driver.get(f'https://leetcode.cn/u/{user}')
    cur = None
    language = None
    company,title,school = None,None,None
    # get ranking
    html_source = driver.page_source
    Soup = BeautifulSoup(html_source,'html.parser')
    # get company and school
    if state == 'US':
        company,title,school = get_company_US(user,Soup)
    elif state == 'CN':
        company,title,school = get_company_CN(user,Soup)
    # ranking tag
    # 等待這個div@class出現再往下做  Explicit wait
    cur = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="text-label-1 dark:text-dark-label-1 flex items-center text-2xl"]')))
    #cur = Soup.find('div',class_='text-label-1 dark:text-dark-label-1 flex items-center text-2xl')
    # 等待這個span@class出現再往下做  Explicit wait
    language = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//span[@class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full text-label-3 dark:text-dark-label-3 bg-fill-3 dark:bg-dark-fill-3"]')))
    #language = Soup.find('span',class_='inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full text-label-3 dark:text-dark-label-3 bg-fill-3 dark:bg-dark-fill-3').text
    language = language.text
    print(int(cur.text.replace(',','')),company,title,school,language)
    return [int(cur.text.replace(',','')),company,title,school,language]

def get_company_CN(user,data):
    company,title,school = None,None,None
    Soup = data.find_all('div',class_='relative mb-[10px]')
    for el in Soup:
        # get company
        if el.find('path')['d'] == 'M7.5 7V5c0-1.484 1.242-2.667 2.75-2.667h3.5c1.508 0 2.75 1.183 2.75 2.667v2H19a3 3 0 013 3v8a3 3 0 01-3 3H5a3 3 0 01-3-3v-8a3 3 0 013-3h2.5zm2 0h5V5c0-.357-.325-.667-.75-.667h-3.5c-.425 0-.75.31-.75.667v2zM5 9a1 1 0 00-1 1v8a1 1 0 001 1h2.5V9H5zm4.5 0v10h5V9h-5zm7 0v10H19a1 1 0 001-1v-8a1 1 0 00-1-1h-2.5z':
            for i,child in enumerate(el.find('div',class_='ml-[8px] w-[calc(100%-26px)] break-all leading-[17px]').find(class_='flex').children):
                # company
                if i == 0:
                    company = child
                elif i == 2:
                    title = child
        # get school 
        elif el.find('path')['d'] == 'M13.465 3.862a3 3 0 00-2.957-.048L2.61 8.122a1 1 0 000 1.756L5 11.18v6.27c0 .59.26 1.15.74 1.491 1.216.86 3.75 2.409 6.26 2.409s5.044-1.548 6.26-2.409c.48-.34.74-.901.74-1.491v-6.27l1.4-.98v4.7a.9.9 0 101.8 0V9.572a1 1 0 00-.493-.862l-8.242-4.848zM18.82 9l-5.862 3.198a2 2 0 01-1.916 0L5.18 9l5.862-3.198a2 2 0 011.916 0L18.82 9zM17 16.687a.937.937 0 01-.413.788c-.855.565-2.882 1.774-4.587 1.774-1.705 0-3.732-1.209-4.587-1.774A.936.936 0 017 16.687V12.27l3.562 1.945a3 3 0 002.876 0L17 12.27v4.417z':
            school = el.text
    return [company,title,school]

def get_company_US(user,data):
    company,title,school = None,None,None
    Soup = data.find_all('div',class_='flex items-start space-x-[9px]')
    for el in Soup:
        # company icon path
        if el.find('path')['d'] == 'M7.5 7V5c0-1.484 1.242-2.667 2.75-2.667h3.5c1.508 0 2.75 1.183 2.75 2.667v2H19a3 3 0 013 3v8a3 3 0 01-3 3H5a3 3 0 01-3-3v-8a3 3 0 013-3h2.5zm2 0h5V5c0-.357-.325-.667-.75-.667h-3.5c-.425 0-.75.31-.75.667v2zM5 9a1 1 0 00-1 1v8a1 1 0 001 1h2.5V9H5zm4.5 0v10h5V9h-5zm7 0v10H19a1 1 0 001-1v-8a1 1 0 00-1-1h-2.5z':
            info = el.text.split('|')
            for i in range(len(info)):
                if i == 0:
                    company = info[i].strip()
                elif i == 1:
                    title = info[i].strip()
        # scholl icon path
        elif el.find('path')['d'] == 'M13.465 3.862a3 3 0 00-2.957-.048L2.61 8.122a1 1 0 000 1.756L5 11.18v6.27c0 .59.26 1.15.74 1.491 1.216.86 3.75 2.409 6.26 2.409s5.044-1.548 6.26-2.409c.48-.34.74-.901.74-1.491v-6.27l1.4-.98v4.7a.9.9 0 101.8 0V9.572a1 1 0 00-.493-.862l-8.242-4.848zM18.82 9l-5.862 3.198a2 2 0 01-1.916 0L5.18 9l5.862-3.198a2 2 0 011.916 0L18.82 9zM17 16.687a.937.937 0 01-.413.788c-.855.565-2.882 1.774-4.587 1.774-1.705 0-3.732-1.209-4.587-1.774A.936.936 0 017 16.687V12.27l3.562 1.945a3 3 0 002.876 0L17 12.27v4.417z':
            school = el.text
    return [company,title,school]
