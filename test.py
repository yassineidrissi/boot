from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

service = Service('/Users/yassine/Documents/boot/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
print("Page Title:", driver.title)

time.sleep(5)
driver.quit()
