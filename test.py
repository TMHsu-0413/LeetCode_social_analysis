import requests
import time
from bs4 import BeautifulSoup
import html5lib
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#print(chromedriver_autoinstaller.install())
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--disable-extensions")
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
ua = UserAgent()
user_agent = ua.random
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.get(f'https://leetcode.com/TMHsu')
time.sleep(10)
html_source = driver.page_source
Soup = BeautifulSoup(html_source,'html.parser')
cur = Soup.find_all('div',class_='flex flex-col space-y-1')
print(Soup.find_all('div',class_='flex items-start space-x-[9px]'))