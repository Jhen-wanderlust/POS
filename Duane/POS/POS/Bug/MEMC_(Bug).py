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
driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.label')[index].innerText == 'MEMC'){find_element = true;    }document.querySelectorAll('.label')[index].innerText;index++;}if(find_element){document.querySelectorAll('.label')[index-1].click();}")
time.sleep(1) 
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-memc/ion-content/div[1]/ion-fab/button/ion-icon').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-row/ion-col/ion-item[1]/div[1]/div/ion-input/input').send_keys('123456789012345678901234567890123456789012345')
time.sleep(1)
memc = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-row/ion-col/ion-item[1]/div[1]/div/ion-input/input').get_attribute('value')

if len(memc) > 40:
    pymsgbox.alert('MAXIMUM OF 40 CHARACTERS: ❌',timeout=3000)
    bug.append('MAXIMUM OF 40 CHARACTERS: ❌')
else:
    pymsgbox.alert('PASSED ✅',timeout=3000)

time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-row/ion-col/ion-item[2]/div[1]/div/ion-input/input').send_keys('12345678901')
time.sleep(1)
memc_val = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-row/ion-col/ion-item[2]/div[1]/div/ion-input/input').get_attribute('value')
time.sleep(1)

if int(memc_val) > 9999999999:
    pymsgbox.alert('MUST INDICATE (MAXIMUM OF 10 NUMBERS ONLY): ❌',timeout=5000)
    bug.append('MUST INDICATE (MAXIMUM OF 10 NUMBERS ONLY) ❌')
else:
    pymsgbox.alert('PASSEd ✅',timeout=5000)

time.sleep(1)
l = len(memc_val)
while l > 0:
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-row/ion-col/ion-item[2]/div[1]/div/ion-input/input').send_keys(Keys.BACKSPACE)
    l -= 1

time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-row/ion-col/ion-item[2]/div[1]/div/ion-input/input').send_keys('452e21')
m_val = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-row/ion-col/ion-item[2]/div[1]/div/ion-input/input').get_attribute('value')

find = 0
for i in m_val:
    if i.isalpha():
        find += 1

if find > 0:
    pymsgbox.alert('MUST NOT ACCEPT CHAR/STR ❌\n' + str(find) + ' CHAR/STR FOUND ❌',timeout=5000)     
    bug.append('MUST NOT ACCEPT CHAR/STR ❌')
else:
    pymsgbox.alert('PASSED ✅',timeout=5000)

time.sleep(1)
if len(bug) > 0:
    bugs = "\n".join(bug)
    pymsgbox.alert(bugs)
else:
    pymsgbox.alert('ALL PASSED ✅') 