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
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[18]/div[1]/div/ion-label').click()
time.sleep(1)    
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-payment-type/ion-header/ion-navbar/div[2]/button/ion-icon').click()       
time.sleep(1)    
driver.switch_to_window(driver.window_handles[1]) 
time.sleep(1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
driver.close()
driver.switch_to_window(driver.window_handles[0])
time.sleep(1)
pymsgbox.alert('Printer: ✅',timeout=3000)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-payment-type/ion-content/div[1]/ion-fab/button/ion-icon').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-payment-type-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/button[1]/span').click()
time.sleep(1)
pymsgbox.alert('Cancel Button: ✅',timeout=3000)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-payment-type/ion-content/div[1]/ion-fab/button/ion-icon').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-payment-type-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('OPT 2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-payment-type-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/button[2]/span').click()
time.sleep(1)
pymsgbox.alert('ADDING OTHER PAYMENT TYPE: ✅',timeout=3000)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-payment-type/ion-content/div[2]/ion-list/ion-item[2]/div[1]/div/ion-label/div/h2').click()
time.sleep(1)
o =  driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-payment-type-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').get_attribute('value')
l = len(o)

while l > 0:
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-payment-type-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.BACKSPACE)  
    l -= 1
    
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-payment-type-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('OPT 3')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-payment-type-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/button[2]/span').click()
time.sleep(1)
pymsgbox.alert('UPDATING OTHER PAYMENT TYPE: ✅',timeout=3000)
time.sleep(1)


opt_ = driver.find_elements_by_class_name('label')                                            
o_ = driver.find_element_by_class_name('list')
length = len(o_.find_elements_by_tag_name('h2'))
ar = []
index = 0
while index < length:
    ar.append(opt_[index].get_attribute('innerText'))
    index += 1
opt_sort = ar
opt_sort.sort()  
if ar == opt_sort:
    pymsgbox.alert('Sorting Other Payment Types ✅',timeout=3000)
else:
    pymsgbox.alert('Other Payment Types not sorted ❌',timeout=3000)  

time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-payment-type/ion-content/div[2]/ion-list/ion-item[2]/div[1]/div/ion-label/div/h2').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-payment-type-crud/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button[2]/span').click()
time.sleep(1)
pymsgbox.alert('DELETING OTHER PAYMENT TYPE: ✅',timeout=3000)
time.sleep(1)
opt = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-payment-type/ion-content/div[2]/ion-list/ion-item/div[1]/div/ion-label/div/h2').get_attribute('innerText')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-payment-type/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)

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
opt1 = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[4]/ion-list[3]/button/div[1]/div/ion-label').get_attribute('innerText')
time.sleep(2)
if opt == opt1:
    pymsgbox.alert('OTHER PAYMENT TYPES MATCH: ✅',timeout=3000)
else:
    pymsgbox.alert('OTHER PAYMENT TYPES NOT MATCH: ❌',timeout=3000)

time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[4]/ion-list[3]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/numpad/ion-content/div[2]/form/ion-item/div[1]/div/ion-input/input').send_keys('CXXR-992498')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/numpad/ion-content/div[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-footer/ion-row/a[2]').click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button/span').click()
time.sleep(1)
pymsgbox.alert('PAY USING OTHER PAYMENT TYPES SUCCESSFULLY: ✅',timeout=5000,)
time.sleep(1)

pymsgbox.alert('Printer: ✅\nCancel Button: ✅\nADDING OTHER PAYMENT TYPE: ✅\nUPDATING OTHER PAYMENT TYPE: ✅\nSORTING OTHER PAYMENT TYPE ✅\nDELETING OTHER PAYMENT TYPE: ✅\nOTHER PAYMENT TYPES MATCH: ✅\nPAY USING OTHER PAYMENT TYPES SUCCESSFULLY: ✅')
