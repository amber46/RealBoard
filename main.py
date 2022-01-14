from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import sys
from userpref import CLIENT_ID, USERNAME, PASSWORD

options = Options()
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://watt.real-board.com/#/")
assert "RealBoard Portal" in driver.title

# //form//input[@id='f_ea647817-6dcb-4ebd-9064-1dc11d0569d6']
# //form//input[@id='f_2d28c75d-b45c-484b-af92-5ba815bd073b']
# //form//input[@id='f_2ec59921-4a49-422c-9a8a-25a47fe7487c']

elem = driver.find_element(By.XPATH, "//form[1]//input[contains(@aria-label, 'מספר לקוח')]")
elem.clear()
elem.send_keys(CLIENT_ID)
elem = driver.find_element(By.XPATH, "//form[1]//input[contains(@aria-label, 'שם משתמש')]")
elem.clear()
elem.send_keys(USERNAME)
elem = driver.find_element(By.XPATH, "//form[1]//input[contains(@aria-label, 'סיסמה')]")
elem.clear()
elem.send_keys(PASSWORD)
elem.send_keys(Keys.RETURN)
sleep(2)  # for reload page

elem_warning = driver.find_elements(By.XPATH, "//span[contains(text(), 'אחתום מאוחר יותר')]")
if elem_warning:
    elem_warning[0].click()
sleep(2)  # for reload page

if len(sys.argv) > 1:
    if sys.argv[1] == "out":
        elem = driver.find_element(By.XPATH, "//div[contains(text(), 'דיווח יציאה')]")
    elif sys.argv[1] == "in":
        elem = driver.find_element(By.XPATH, "//div[contains(text(), 'דיווח כניסה')]")
    else:
        elem = driver.find_element(By.XPATH, "//span[contains(text(), 'התנתק')]")

elem.click()
sleep(2)  # for submit reload
driver.close()
