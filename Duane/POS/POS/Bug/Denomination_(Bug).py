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
driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.label')[index].innerText == 'Denomination'){find_element = true;    }document.querySelectorAll('.label')[index].innerText;index++;}if(find_element){document.querySelectorAll('.label')[index-1].click();}")
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-denomination/ion-content/div[1]/ion-fab/button/ion-icon').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-denomination-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('5')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-denomination-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/button[2]').click()        
time.sleep(1)
den = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-denomination/ion-content/div[2]/ion-list/ion-item[13]/div[1]/div/ion-label/div/h2').get_attribute('innerText')
time.sleep(1)

deno = driver.find_elements_by_class_name('label')                                            
d = driver.find_element_by_class_name('list')
length = len(d.find_elements_by_tag_name('h2'))

ar = []
index = 0
find= 0
while index < length:
    ar.append(deno[index].get_attribute('innerText'))
    if den == ar[index]:
        find += 1
        break
    index += 1    

if find > 0:
    pymsgbox.alert('DUPLICATE DATA: ❌',timeout=3000)
    bug.append('DUPLICATE DATA: ❌')
else:
    pymsgbox.alert('PASSED: ✅',timeout=3000)

time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-denomination/ion-content/div[2]/ion-list/ion-item[13]/div[1]/div/ion-label/div/h2').click()
time.sleep(1)
header = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-denomination-crud/ion-header/ion-navbar/div[2]/ion-title/div').get_attribute('innerText')
time.sleep(1)
val = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-denomination-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').get_attribute('value')
time.sleep(1)

if header == val:
    pymsgbox.alert('PASSED : ✅',timeout=3000)
else:
    pymsgbox.alert('HEADER NAME MUST BE SAME OF DENOMINATION VALUE : ❌',timeout=4000)
    bug.append('HEADER NAME MUST BE SAME OF DENOMINATION VALUE : ❌') 

time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-denomination-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('23e6e')
time.sleep(1)
den = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-denomination-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').get_attribute('value')
time.sleep(1)    
find = 0
for i in den:
    if i.isdigit():
        continue
    else:
        find += 1

time.sleep(1)
if find > 0:
    pymsgbox.alert('MUST NOT ACCEPT LETTERS AND SPECIAL CHARACTERS ' + str(find) + ' LETTERS/SPECIAL CHARACTERS FOUND ❌',timeout=4000) 
    bug.append('MUST NOT ACCEPT LETTERS AND SPECIAL CHARACTERS ' + str(find) + ' LETTERS/SPECIAL CHARACTERS FOUND ❌')
else:
    pymsgbox.alert('PASSED ✅',timeout=3000)

time.sleep(1)
if len(bug) > 0:
    bugs = "\n".join(bug)
    pymsgbox.alert(bugs)
else:
    pymsgbox.alert('ALL PASSED ✅')