from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException, TimeoutException
import subprocess
import time
import os

print("Script started")

options =  webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")



driver = webdriver.Chrome(options=options)
driver.get("https://bdgame.in/code/docker.html")
time.sleep(5)

textarea_element = driver.find_element("id", "dockrr")

code = textarea_element.get_attribute('value')

file_name = "dockrr.py"

with open(file_name, "w") as file:
    file.write(code)

# os.system(f"python3 {file_name}")

driver.get("https://bdgame.in/code/newtest.html")
time.sleep(5)

textarea_element1 = driver.find_element("id", "newtest")

code1 = textarea_element1.get_attribute('value')

file_name1 = "newtest.py"

with open(file_name1, "w") as file:
    file.write(code1)

driver.get("https://bdgame.in/code/Pytho_code_1.html")
time.sleep(5)

textarea_element11 = driver.find_element("id", "pyco100")

code11 = textarea_element11.get_attribute('value')

file_name11 = "main.py"

with open(file_name11, "w") as file:
    file.write(code11)

os.system(f"python3 {file_name11}") 

