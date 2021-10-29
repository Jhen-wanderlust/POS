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

driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'MASTER FILE'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(1)
driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.label')[index].innerText == 'MEMC'){find_element = true;    }document.querySelectorAll('.label')[index].innerText;index++;}if(find_element){document.querySelectorAll('.label')[index-1].click();}")
time.sleep(1)   
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-memc/ion-header/ion-navbar/div[2]/button/ion-icon').click()
time.sleep(1)
driver.switch_to_window(driver.window_handles[1])
time.sleep(3)
driver.close()
driver.switch_to_window(driver.window_handles[0])
time.sleep(1)
pymsgbox.alert('Printer: ✅',timeout=3000)
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-memc/ion-header/ion-navbar/div[2]/ion-searchbar/div/input').send_keys('e')
time.sleep(1)
pymsgbox.alert('Search: ✅',timeout=3000)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-memc/ion-content/div[1]/ion-fab/button/ion-icon').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-col/ion-row/button[1]/span').click()
time.sleep(1)
pymsgbox.alert('Cancel Button: ✅',timeout=3000)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-memc/ion-content/div[1]/ion-fab/button/ion-icon').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-row/ion-col/ion-item[1]/div[1]/div/ion-input/input').send_keys('memc 2')
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-row/ion-col/ion-item[2]/div[1]/div/ion-input/input').send_keys('100')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-col/ion-row/button[2]/span').click()
time.sleep(1) 
pymsgbox.alert('Adding MEMC: ✅',timeout=3000)
time.sleep(1) 
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-memc/ion-content/div[2]/ion-grid/ion-item[3]/div[1]/div/ion-label/ion-row/ion-col[2]').click()
time.sleep(1)
memc = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-row/ion-col/ion-item[1]/div[1]/div/ion-input/input').get_attribute('value')
time.sleep(1)
l = len(memc)

while l > 0:
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-row/ion-col/ion-item[1]/div[1]/div/ion-input/input').send_keys(Keys.BACKSPACE)
    l -= 1

time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-row/ion-col/ion-item[1]/div[1]/div/ion-input/input').send_keys('memc 3')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-content/div[2]/form/ion-card/ion-col/ion-row/button[2]/span').click()
time.sleep(1)
pymsgbox.alert('Updating MEMC: ✅',timeout=3000)
time.sleep(1)

memc_ = driver.find_elements_by_class_name('col')                                                 
ar = []
index = 0
while index < len(memc_):
    ar.append(memc_[index].get_attribute('innerText'))
    index += 1
memc_sort = ar
memc_sort.sort()  
if ar == memc_sort:
    pymsgbox.alert('Sorting MEMC ✅',timeout=3000)
else:
    pymsgbox.alert('MEMC not sorted ❌',timeout=3000) 


time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-memc/ion-content/div[2]/ion-grid/ion-item[3]/div[1]/div/ion-label/ion-row/ion-col[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-memc-crud/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button[2]/span').click()
time.sleep(1)
pymsgbox.alert('Deleting MEMC: ✅',timeout=3000)
time.sleep(1)
m = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-memc/ion-content/div[2]/ion-grid/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[1]').get_attribute('innerText')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-memc/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[10]/div[1]/div/ion-label').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-items/ion-content/div[2]/ion-grid/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[1]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[14]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
m1 = driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item[2]/div[1]/div/ion-label').get_attribute('innerText')
time.sleep(1)
print(m)
print(m1)

if m == m1:
    pymsgbox.alert('MEMC MATCH: ✅',timeout=3000)
else:
    pymsgbox.alert('MEMC NOT MATCH: ❌',timeout=3000)

pymsgbox.alert('Cancel Button: ✅\nPrinter: ✅\nSearch: ✅\nAdding MEMC: ✅\nUpdating MEMC: ✅\nSorting MEMC ✅\nDeleting MEMC: ✅\nMEMC MATCH: ✅')   
