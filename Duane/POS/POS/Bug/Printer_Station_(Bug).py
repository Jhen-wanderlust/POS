from selenium.common.exceptions import WebDriverException 
from tkinter.constants import S
import keyboard
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from keyboard import press
import pymsgbox
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import datetime
import os
import re 

chrome_options = Options()
chrome_options.add_argument("nwapp=C:/Program Files (x86)/LSTV/POS/frontend/KRAKEN_RESTO.exe")

driver = webdriver.Chrome("C:/Users/ASUS/OneDrive/Desktop/Python_Selenium/nwjs-sdk-v0.54.0-win-ia32/chromedriver",options=chrome_options)
driver.maximize_window()

time.sleep(3)
# LOG IN 
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(4)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[6]/ion-col[2]/ion-item/div[1]/div/ion-input/input").send_keys(80)
time.sleep(1)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[8]/ion-col/button[2]/span").click()
time.sleep(2)
driver.switch_to.alert.accept() 
time.sleep(5)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-security-code/ion-content/div[2]/ion-grid/ion-row[5]/ion-col[2]/input").send_keys("HMP-MOO-NCA-ANC-CCP-ZMO-AOH-NRP-CER-ANK")
time.sleep(1)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-security-code/ion-content/div[2]/ion-grid/ion-row[6]/ion-col/button/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/ion-card/ion-list/ion-item[1]/div[1]/div/ion-input/input").send_keys("lstv")
driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/ion-card/ion-list/ion-item[2]/div[1]/div/ion-input/input").send_keys("lstventures")
time.sleep(1)
driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/div/button[1]/span").click()
time.sleep(3)

bug = []
driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'MASTER FILE'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[5]/div[1]/div/ion-label').click()
time.sleep(1)  
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-locations/ion-content/div[1]/ion-fab/button/ion-icon').click()  
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-locations-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('ldhfgldfkjgl3045702834-jsldkfjlj9023w4fmsdf456345g')
time.sleep(1)
printer = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-locations-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').get_attribute('value')
time.sleep(1)

if len(printer) > 40:
    pymsgbox.alert('MAXIMUM LENGTH MUST BE 40 CHARACTERS ONLY ❌',timeout = 4000)
    bug .append('MAXIMUM LENGTH MUST BE 40 CHARACTERS ONLY ❌')
else:
    pymsgbox.alert('PASSED: ✅',timeout=3000)

time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-locations-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col[2]/ion-item/div[1]/div/ion-input/input').send_keys('345e')
time.sleep(1)
p_size = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-locations-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col[2]/ion-item/div[1]/div/ion-input/input').get_attribute('value')
print(p_size)
time.sleep(1)

if len(p_size) <= 0:
    pymsgbox.alert('PRINTER SIZE MUST NOT ACCEPT CHARACTERS ❌',timeout = 6000)
    bug.append('PRINTER SIZE MUST NOT ACCEPT CHARACTERS ❌')
else:
    pymsgbox.alert('PASSED: ✅',timeout=3000)

time.sleep(1)
if len(bug) > 0:
    bugs = "\n".join(bug)
    pymsgbox.alert(bugs)
else:
    pymsgbox.alert('ALL PASSED ✅')   