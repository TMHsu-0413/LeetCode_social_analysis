import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get(f'https://leetcode.com/TMHsu/')
time.sleep(3)
html_source = driver.page_source
Soup = BeautifulSoup(html_source,'html.parser')
language = Soup.find('span',class_='inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full text-label-3 dark:text-dark-label-3 bg-fill-3 dark:bg-dark-fill-3').text
print(language)