import requests
import time
from bs4 import BeautifulSoup
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
driver = webdriver.Chrome(chromedriver_autoinstaller.install(),options = options)
driver.get('https://leetcode.com/TMHsu')
time.sleep(12)
html_source = driver.page_source
Soup = BeautifulSoup(html_source,'html.parser')
cur = Soup.find('div',class_='text-label-1 dark:text-dark-label-1 flex items-center text-2xl')
print(cur.text)
#cur = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="absolute top-0 left-0"]')))
#print(cur.text)
