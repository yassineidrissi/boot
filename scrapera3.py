import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import certifi
import os
from twilio.rest import Client  # Twilio library

# Point Python to the certificate bundle
os.environ['SSL_CERT_FILE'] = certifi.where()

# Twilio credentials - replace these with your actual values
 # Your phone number to call

# Initialize the Twilio client
client = Client(account_sid, auth_token)

def call_me():
    """Call your number using Twilio to send a voice message alert."""
    try:
        call = client.calls.create(
            to=destination_number,
            from_=twilio_number,
            # TwiML instructions: this message will be spoken in the call.
            twiml='<Response><Say voice="alice" language="en-US">Alert! There is a new piscine detected. Please check the website immediately.</Say></Response>'
        )
        print(f"Call initiated successfully. Call SID: {call.sid}")
    except Exception as e:
        print(f"Error initiating call: {e}")

# Your login credentials
user = "atmanidrissi99@gmail.com"
password = "RAJA1949idrissi@"

# Setup undetected ChromeDriver with stealth options
options = uc.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-default-apps')
options.add_argument("--start-maximized")
# Optional: set a custom user agent to further mimic a real browser
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

# Launch the browser using undetected-chromedriver
driver = uc.Chrome(options=options)

# Go to the login page
driver.get("https://admission.1337.ma/en/users/sign_in")
print("Page title:", driver.title)
time.sleep(2)

# Log in by filling out the form
driver.find_element(By.NAME, "email").send_keys(user)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(5)

# Check if the account is not verified
if "not verified" in driver.page_source.lower():
    print("❌ Your account is not verified.")
else:
    print("✅ Login attempt finished. Check if you are logged in.")

# Create an initial BeautifulSoup object to compare against later
oldsoup = BeautifulSoup(driver.page_source, "html.parser")

# Monitor the page for changes (i.e., a new piscine)
while True:
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    
    # Compare the new page's soup with the previous one
    if soup != oldsoup:
        print("🚨 A new piscine has been detected!")
        # When a change is detected, call the function to alert you via phone
        call_me()
    else:
        print("No new piscine detected.")

    # Update oldsoup for the next iteration
    oldsoup = soup
    time.sleep(10)

# Optionally close the browser (unreachable in this infinite loop, unless you break out)
driver.quit()
