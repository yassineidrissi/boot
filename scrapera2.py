from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# set the headers and user string

driver = webdriver.Chrome('/Users/yassine/Documents/boot/chromedriver')
driver.get("https://candidature.1337.ma/piscines")
print(driver.title)

driver.quit()

URL = 'https://candidature.1337.ma/piscines'
#!stop here
# send a request to fetch HTML of the page
# create the soup object
# change the encoding to utf-8
# soup.encode('utf-8')

user = "yassine1337idrissi@gmail.com"
password = "Yassin@0661535096"
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
#print(soup.prettify())

# function to check if the price has dropped below 20,000
# def check_price():
  #print(price)

  #converting the string amount to float
#   converted_price = float(price[0:5])
#   print(converted_price)
#   if(converted_price < 20000):
#     send_mail()

  #using strip to remove extra spaces in the title
print(price)
print(title)




# function that sends an email if the prices fell down
# def send_mail():
#   server = smtplib.SMTP('smtp.gmail.com', 587)
#   server.ehlo()
#   server.starttls()
#   server.ehlo()

#   server.login('email@gmail.com', 'password')

#   subject = 'Price Fell Down'
#   body = "Check the amazon link https://www.amazon.in/Bose-SoundLink-Wireless-Around-Ear-Headphones/dp/B0117RGG8E/ref=sr_1_11?qid=1562395272&refinements=p_89%3ABose&s=electronics&sr=1-11 "

#   msg = f"Subject: {subject}\n\n{body}"
  
#   server.sendmail(
#     'sender@gmail.com',
#     'receiver@gmail.com',
#     msg
#   )
#   #print a message to check if the email has been sent
#   print('Hey Email has been sent')
#   # quit the server
#   server.quit()

# #loop that allows the program to regularly check for prices
# while(True):
#   check_price()
#   time.sleep(60 * 60)