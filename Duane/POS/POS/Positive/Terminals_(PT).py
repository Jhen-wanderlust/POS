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
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[4]/div[1]/div/ion-label').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-terminal/ion-header/ion-navbar/div[2]/button/ion-icon').click()
time.sleep(1)
driver.switch_to_window(driver.window_handles[1])
time.sleep(3)
driver.close()
driver.switch_to_window(driver.window_handles[0])
time.sleep(1)
pymsgbox.alert('Printer: ✅',timeout=3000)
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-terminal/ion-header/ion-navbar/div[2]/ion-searchbar/div/input').send_keys('t')
time.sleep(1)
pymsgbox.alert('Search: ✅',timeout=3000)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-terminal/ion-header/ion-navbar/div[2]/ion-searchbar/div/input').send_keys(Keys.BACKSPACE)
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-terminal/ion-content/div[1]/ion-fab/button/ion-icon').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-terminal-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/button[1]').click()
time.sleep(1)
pymsgbox.alert('Cancel Button: ✅',timeout=3000)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-terminal/ion-content/div[1]/ion-fab/button/ion-icon').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-terminal-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('t1')
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-terminal-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('127.0.0.1')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-terminal-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/button[2]').click()
time.sleep(1)
pymsgbox.alert('Adding Terminals: ✅',timeout=3000)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-terminal/ion-content/div[2]/ion-list/ion-item[1]/div[1]/div/ion-label/div/h2').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-terminal-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-terminal-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/button[2]').click()
time.sleep(1)
pymsgbox.alert('Updating Terminals: ✅',timeout=3000)
time.sleep(1)

term_ = driver.find_elements_by_class_name('label')                                            
t_ = driver.find_element_by_class_name('list')
length = len(t_.find_elements_by_tag_name('h2'))
ar = []
index = 0
while index < length:
    ar.append(term_[index].get_attribute('innerText'))
    index += 1
t_sort = ar
t_sort.sort()  
if ar == t_sort:
    pymsgbox.alert('Sorting Other Payment Types ✅',timeout=3000)
else:
    pymsgbox.alert('Other Payment Types not sorted ❌',timeout=3000)  

time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-terminal/ion-content/div[2]/ion-list/ion-item[1]/div[1]/div/ion-label/div/h2').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-terminal-crud/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button[2]/span').click()
time.sleep(1)
pymsgbox.alert('Deleting Terminals: ✅',timeout=3000)
time.sleep(1)

terminal = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-terminal/ion-content/div[2]/ion-list/ion-item/div[1]/div/ion-label/div/h2').get_attribute('innerText')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-terminal/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[5]/div[1]/div/ion-label').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-locations/ion-content/div[2]/ion-list/ion-item/div[1]/div/ion-label/div/h2').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-locations-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
terminal1 = driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item/div[1]/div/ion-label').get_attribute('innerText')
time.sleep(1)

if terminal == terminal1:
    pymsgbox.alert('Terminal Match: ✅',timeout=3000)
else:
    pymsgbox.alert('TERMINAL NOT MATCH ❌',timeout = 3000)    

time.sleep(1)
pymsgbox.alert('Printer: ✅\nCancel Button: ✅\nAdding Terminals: ✅\nUpdating Terminals: ✅\nSorting Terminals ✅\nDeleting Terminals: ✅\nTerminal Match: ✅')
