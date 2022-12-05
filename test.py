import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get(f'https://leetcode.com/zokumyoin/')
time.sleep(3)
html_source = driver.page_source
Soup = BeautifulSoup(html_source,'html.parser')
reput_level,views = None,0
for i,child in enumerate(Soup.find('div',class_='mt-4 flex flex-col space-y-4').children):
    # get reputation level
    if i == 0:
        views = int(child.find('div').text[5:])
    # get views
    elif i == 1:
        solution = int(child.find('div').text[8:])
    elif i == 2:
        discuss = int(child.find('div').text[7:])
    elif i == 3:
        reputation = int(child.find('div').text[10:])