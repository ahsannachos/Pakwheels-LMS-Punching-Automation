from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get('https://lms.pakeventures.com/login')
driver.implicitly_wait(7000)
username = driver.find_element(By.ID, "username")
time.sleep(1)
username.send_keys("enter your id")
password = driver.find_element(By.ID, "password")
time.sleep(1)
password.send_keys("enter your password")
loginbutton= driver.find_element(By.NAME, "login")
loginbutton.click()
LMS = driver.find_element(By.LINK_TEXT, "LMS")
LMS.click()
Requests = driver.find_element(By.LINK_TEXT, "Requests")
Requests.click()
punch=driver.find_element(By.LINK_TEXT, "Punching Request")
punch.click()
with open("backenddate.txt", "r+") as f:
    dateread = f.read().strip()
    if dateread:
        previousdate = datetime.strptime(dateread, "%Y-%m-%d")
        newdate = previousdate + timedelta(days=1)
    else:
        newdate = datetime(2025, 4, 4)
        
    f.seek(0)    
    f.write(newdate.strftime("%Y-%m-%d"))
    f.truncate()
datecorrect = newdate.strftime("%Y-%m-%d")
date = driver.find_element(By.ID, "date")
date.send_keys(datecorrect)
punchin = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
time.sleep(1)
punchin.click()
times = driver.find_element(By.ID, "punch_in_time")
time.sleep(1)
times.click()
timeclick = driver.find_element(By.CSS_SELECTOR, "option[value='09:00']") #select your time
time.sleep(1)
timeclick.click()
HR = Select(driver.find_element(By.ID, "approved_by")) 
HR.select_by_value("2045") #inspect the webpage and add your assignee
time.sleep(1)
watcher = Select(driver.find_element(By.CLASS_NAME, "multiple"))
watcher.select_by_value("1646") #inspect the webpage and add your watcher
reason = driver.find_element(By.ID, "reason")
reason.click()
time.sleep(1)
reason.send_keys("Forgot Punch In")
apply = driver.find_element(By.CSS_SELECTOR, "input[name='commit']")
time.sleep(2)
apply.click()
