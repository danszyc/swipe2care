import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import sqlite3
from dotenv import load_dotenv
import os

conn = sqlite3.connect(r"/Users/danielszyc/Library/Application Support/Google/Chrome/Profile 2/Cookies")

# Create a cursor
cursor = conn.cursor()

# Execute a SELECT statement to retrieve the cookies
cursor.execute("SELECT host_key, name, value, path, expires_utc FROM cookies")

# Fetch all the results
cookies = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()

options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--user-data-dir=/Users/danielszyc/Library/Application Support/Google/Chrome/Profile 2')
options.add_argument('--headless')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

'''for cookie in cookies:
  if 'neu' not in cookie[0] and 'duo' not in cookie[0]:
    continue
  #print(cookie)
  selenium_cookie = {
  'name': cookie[1],
  'value': cookie[2],
  'path': cookie[3],
  'expiry': cookie[4],
  'secure': False }
  if len(cookie) == 6:
    selenium_cookie['secure'] = cookie[5]
  try:
    driver.add_cookie(selenium_cookie)
  except: 
    continue'''

driver.get("https://huskycardcenter.neu.edu/student/welcome.php")

load_dotenv('.env')
username = driver.find_element(By.NAME, "j_username")
password = driver.find_element(By.NAME, "j_password")
username.send_keys(os.getenv('USERNAME'))
password.send_keys(os.getenv('PASSWORD'))

# navigate to CBORD welcome page https://huskycardcenter.neu.edu/student/welcome.php
driver.find_element(By.NAME, "_eventId_proceed").click()
while driver.current_url != 'https://huskycardcenter.neu.edu/student/welcome.php':
  time.sleep(1)
# navigate to Swipe2Care page https://huskycardcenter.neu.edu/common/local_mealdonation.php
driver.find_element(By.LINK_TEXT, "Swipe2Care").click()
# navigate to Swipe Donation page https://huskycardcenter.neu.edu/common/local_donate.php
driver.find_element(By.TAG_NAME, "input").click()

for i in range(3,0,-1):
  print('Attempting to donate '+str(i)+" swipes...")
  num_meals = driver.find_element(By.NAME, "meals_to_donate")
  num_meals.send_keys(str(i))
  driver.find_elements(By.TAG_NAME, "input")[1].click()
  driver.save_screenshot('screenshots/ss'+str(i)+'.png')
  try:
    e = driver.find_element(By.TAG_NAME, "h2")
    if e.text != 'Donation Submitted':
      raise Exception()
    print('Success: '+str(i)+' swipes donated')
    break
  except:
    print('Error: '+e.text)
    if e.text != "Above Weekly Donation Limit":
      driver.find_elements(By.TAG_NAME, "input")[0].click()#return to meal input page
    break

driver.save_screenshot('screeenshots/ss.png')
driver.quit()


