import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--disable-extensions")
options.add_argument("--headless")
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
unit = {'K':1000,'M':1000000}
# Get US users current contest ranking
def get_info(user,state):
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    cur = None
    language = None
    # company and school
    company,title,school = None,None,None
    # community stats
    views,solution,discuss,reputation,reput_level = None,None,None,None,None
    try:
        if state == 'US':
            driver.get(f'https://leetcode.com/{user}')
        elif state == 'CN':
            driver.get(f'https://leetcode.cn/u/{user}')
        # 等待這個div@class出現再往下做  Explicit wait
        # ranking tag
        cur = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="text-label-1 dark:text-dark-label-1 flex items-center text-2xl"]')))
        #
        #print(cur.get_attribute("textContent").replace(',',''))
        # 等待這個span@class出現再往下做  Explicit wait
        # language tag
        language = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//span[@class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full text-label-3 dark:text-dark-label-3 bg-fill-3 dark:bg-dark-fill-3"]')))
        language = language.text
        #print(language)
        # get company and school
        if state == 'US':
            html_source = driver.page_source
            Soup = BeautifulSoup(html_source,'html.parser')
            company,title,school = get_company_US(user,Soup)
            views,solution,discuss,reputation = get_stats_US(user,Soup)
        elif state == 'CN':
            html_source = driver.page_source
            Soup = BeautifulSoup(html_source,'html.parser')
            company,title,school = get_company_CN(user,Soup)
            views,reput_level = get_stats_CN(user,Soup)
        #print('print data')
        data = [int(cur.get_attribute("textContent").replace(',','')),company,title,school,language,views,solution,discuss,reputation,reput_level]
        #print(data)
        time.sleep(random.randint(1,8))
        return data
        driver.close()
    except Exception as e:
        print(e)
        driver.close()
        return [0,None,None,None,None,None,None,None,None,None]

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
    print('get_company')
    Soup = data.find_all(class_='flex items-start space-x-[9px]')
    for el in Soup:
        # get company
        if el.find('path')['d'] == 'M7.5 7V5c0-1.484 1.242-2.667 2.75-2.667h3.5c1.508 0 2.75 1.183 2.75 2.667v2H19a3 3 0 013 3v8a3 3 0 01-3 3H5a3 3 0 01-3-3v-8a3 3 0 013-3h2.5zm2 0h5V5c0-.357-.325-.667-.75-.667h-3.5c-.425 0-.75.31-.75.667v2zM5 9a1 1 0 00-1 1v8a1 1 0 001 1h2.5V9H5zm4.5 0v10h5V9h-5zm7 0v10H19a1 1 0 001-1v-8a1 1 0 00-1-1h-2.5z':
            info = el.text.split('|')
            for i in range(len(info)):
                if i == 0:
                    company = info[i].strip()
                elif i == 1:
                    title = info[i].strip()
        # get school
        elif el.find('path')['d'] == 'M13.465 3.862a3 3 0 00-2.957-.048L2.61 8.122a1 1 0 000 1.756L5 11.18v6.27c0 .59.26 1.15.74 1.491 1.216.86 3.75 2.409 6.26 2.409s5.044-1.548 6.26-2.409c.48-.34.74-.901.74-1.491v-6.27l1.4-.98v4.7a.9.9 0 101.8 0V9.572a1 1 0 00-.493-.862l-8.242-4.848zM18.82 9l-5.862 3.198a2 2 0 01-1.916 0L5.18 9l5.862-3.198a2 2 0 011.916 0L18.82 9zM17 16.687a.937.937 0 01-.413.788c-.855.565-2.882 1.774-4.587 1.774-1.705 0-3.732-1.209-4.587-1.774A.936.936 0 017 16.687V12.27l3.562 1.945a3 3 0 002.876 0L17 12.27v4.417z':
            school = el.text
    return [company,title,school]

def get_stats_CN(user,data):
    reput_level,views = None,0
    for i,child in enumerate(data.find('div',class_='mt-4 flex flex-col space-y-4').children):
        # get reputation level
        if i == 0:
            reput_level = child.text[-2:]
        # get views
        elif i == 1:
            views = child.find('div').text[4:]
            if views[-1] in unit:
                views = int(float(views[:-1]) * unit[views[-1]])
            else:
                views = int(views)
    return views,reput_level

def get_stats_US(user,data):
    print('get stats')
    views,solution,discuss,reputation = 0,0,0,0
    all_data = data.find_all(class_='mt-4 flex flex-col space-y-4')
    for j in range(len(all_data)):
        if len(all_data[j]) != 4:
            continue
        for i,child in enumerate(all_data[j].children):
            #print(child.find('div').text)
            if i == 0:
                views = child.find('div').text[5:]
                if views[-1] in unit:
                    views = int(float(views[:-1]) * unit[views[-1]])
                else:
                    views = int(views)
            elif i == 1:
                solution = child.find('div').text[8:]
                if solution[-1] in unit:
                    solution = int(float(solution[:-1]) * unit[solution[-1]])
                else:
                    solution = int(solution)
            elif i == 2:
                discuss = child.find('div').text[7:]
                if discuss[-1] in unit:
                    discuss = int(float(discuss[:-1]) * unit[discuss[-1]])
                else:
                    discuss = int(discuss)
            elif i == 3:
                reputation = child.find('div').text[10:]
                if reputation[-1] in unit:
                    reputation = int(float(reputation[:-1]) * unit[reputation[-1]])
                else:
                    reputation = int(reputation)
    return views,solution,discuss,reputation