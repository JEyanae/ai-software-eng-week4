
# test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()  # or specify path like webdriver.Chrome(executable_path="C:/AI SOFTWARE ENGINEERING/chromedriver-win64/chromedriver-win64/chromedriver.exe")

# Open local HTML file
driver.get("file:///C:/AI%20SOFTWARE%20ENGINEERING/login.html")

# Interact with elements
driver.find_element(By.ID, "username").send_keys("test_user")
driver.find_element(By.ID, "password").send_keys("test_pass")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
login_button = wait.until(EC.presence_of_element_located((By.ID, "loginBtn")))
login_button.click()

# Optional: wait before closing
time.sleep(2)
driver.quit()