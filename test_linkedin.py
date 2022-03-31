# Write a selenium test script for the following actions to be automated
# * do a google search for “LinkedIn  “ . From the search result, click  the link to www.linkedin.com and login with your credentials and view your profile
# Note : take LinkedIn account first , if you don’t have one

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

email = input("Enter email:")
password = input("Enter password:")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.linkedin.com/")
driver.find_element_by_name("session_key").send_keys(email)
time.sleep(5)
driver.find_element_by_name("session_password").send_keys(password)
time.sleep(5)
driver.find_element_by_xpath("/html/body/main/section[1]/div/div/form/button").click()
time.sleep(5)
driver.close()
print("tested succesfully")

