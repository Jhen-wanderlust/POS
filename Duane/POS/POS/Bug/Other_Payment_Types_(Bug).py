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
time.sleep(2)
driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.label')[index].innerText == 'Other Payment Types'){find_element = true;    }document.querySelectorAll('.label')[index].innerText;index++;}if(find_element){document.querySelectorAll('.label')[index-1].click();}")
time.sleep(2)


pymsgbox.alert('PASSED ✅',timeout=5000)

    
time.sleep(1)    
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-payment-type/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
# CASH FUND
driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'CASH FUND'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(2)
buttons = driver.find_elements_by_class_name('button-inner')
buttons[15].click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item/div[1]/div/ion-label/ion-row/ion-col/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[3]/button/span').click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[6]/button/span').click()
time.sleep(1)
driver.execute_script("document.querySelectorAll('#menus')[0].scrollTo(0, 100000);")
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[4]/ion-list[3]/button/div[1]/div').click()
time.sleep(1)     
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/numpad/ion-content/div[2]/button/span').click()    
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-content/div[2]/form/ion-item[3]/div[1]/div/ion-input/input').send_keys('09123456789012345')
time.sleep(1)
contact = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-content/div[2]/form/ion-item[3]/div[1]/div/ion-input/input').get_attribute('value')
time.sleep(1)

l = len(contact)
if int(l) != 11:
    pymsgbox.alert('CONTACT NUMBER MUST BE 11 NUMBERS ONLY: ❌',timeout=5000)
    bug.append('CONTACT NUMBER MUST BE 11 NUMBERS ONLY: ❌')
else:
        pymsgbox.alert('PASSED ✅',timeout=5000)


time.sleep(1)
find = 0
for j in contact:
    if j.isdigit():
        continue
    else:
        find += 1

time.sleep(1)
if find > 0:
    pymsgbox.alert('CONTACT NUMBER MUST NOT ACCEPT CHARACTERS / SPECIAL CHARACTERS: ❌',timeout=5000)
    bug.append('CONTACT NUMBER MUST NOT ACCEPT CHARACTERS / SPECIAL CHARACTERS: ❌')
else:
    pymsgbox.alert('PASSED ✅',timeout=5000)

time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-content/div[2]/form/ion-item[4]/div[1]/div/ion-input/input').send_keys('1234-5678-9000')
time.sleep(1)
tin = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-content/div[2]/form/ion-item[4]/div[1]/div/ion-input/input').get_attribute('value')
time.sleep(1)

l = len(tin)
if int(l) != 14:
    pymsgbox.alert('TIN NUMBER LENGTH MUST BE 12 ONLY: ❌',timeout=5000)
    bug.append('TIN NUMBER LENGTH MUST BE 12 ONLY: ❌')
else:
        pymsgbox.alert('PASSED ✅',timeout=5000)

time.sleep(1)
find = 0
for k in tin:
    if k.isdigit() or k == "-":
        continue
    else:
        find += 1
        
time.sleep(1)
if find > 0:
    pymsgbox.alert('TIN NUMBER MUST NOT ACCEPT CHARACTER OR SPECHIAL CHARACTERS EXCEPT " - ": ❌',timeout=5000)
    bug.append('TIN NUMBER MUST NOT ACCEPT CHARACTER OR SPECHIAL CHARACTERS EXCEPT " - ": ❌')
else:
    pymsgbox.alert('PASSED ✅',timeout=5000)

time.sleep(1)
if len(bug) > 0:                                                                                                    
    bugs = "\n".join(bug)
    pymsgbox.alert(bugs)
else:
        pymsgbox.alert('ALL PASSED ✅') 