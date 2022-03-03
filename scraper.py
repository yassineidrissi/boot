from http.server import executable
from turtle import xcor
import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import logging
import json
import bs4
import requests
from bs4 import BeautifulSoup

URL = 'https://candidature.1337.ma/piscines'


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/Users/yassine/Documents/boot/chromedriver', options=chrome_options)

headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
}
page = requests.get(URL, headers=headers)
# time.sleep(5)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

# print(soup)
user = "yassine1337idrissi@gmail.com"
password = "Yassin@0661535096"

driver.get(URL)
print(driver.text)
username_login = driver.find_element_by_id("string email optional")
password_login = driver.find_element_by_class_name("password optional")
# username_login.send_keys(user)
# time.sleep(1)
# password_login.send_keys(password)
user = soup.find("input",{"class":"string email optional"})
#how i will know that this code is work
print(user)

piscine = soup.find()
price = soup.find(id="corePrice_desktop")

# button = driver.find_element_by_tag_name("Sign in")
time.sleep(2)
button.click()
time.sleep(2)
soup2 = BeautifulSoup(page.content,'html.parser')
if soup2.text != soup.text:
    print(soup2.text)

# print(piscine)
# print(username_login)
# print(title)