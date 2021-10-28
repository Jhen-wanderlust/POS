import datetime
import os
import re
import time
from tkinter.constants import S
import keyboard
import openpyxl
import pyautogui
import pymsgbox
from keyboard import press
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'CASH FUND'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(2)
buttons = driver.find_elements_by_class_name('button-inner')
time.sleep(1)
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

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[5]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[6]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[5]/button/div[1]/div').click()

time.sleep(1)

d = driver.find_element_by_class_name('seatheader')
l = len(d.find_elements_by_tag_name('h2'))
length = l / 4
i = 0
burgerSteak = 0
friedChicken = 0
sisigVatE = 0
t = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[2]/ion-content/div[2]/ion-list[1]/button/div[1]/h2').get_attribute('innerText')
pos_total = t[2:]

while i < int(length):
    items = driver.find_elements_by_class_name('itemcode')
    if items[i].get_attribute('innerText') == "BURGER STEAK":
        burgerSteak += 1 
    if items[i].get_attribute('innerText') == "FRIED CHICKEN":
        friedChicken += 1  
    if items[i].get_attribute('innerText') == "SISIG VAT E":
        sisigVatE += 1         
    i += 1    

 
price = driver.find_elements_by_class_name('seatTotal')
total = []
length = l / 2
i = 2
while i < length:
    total.append(float((price[i].get_attribute('innerText')[2:])))
    i += 2    

pymsgbox.alert('Sisig Vat E: ' + str(sisigVatE) + '\n' + 'Fried Chicken: ' + str(friedChicken) + '\n' + 'Burger Steak: '+ str(burgerSteak) + '\n' + 'POS_Total: ' + str(pos_total) + '\n' + 'Computation Total: ' + str(sum(total)), timeout=7000)

if float(pos_total) == float(sum(total)):
    pymsgbox.alert("Total Value Match ✅",timeout=4000)
else:
    pymsgbox.alert("Total Value Not Match ❌",timeout=4000)

time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[3]/button/span').click()
time.sleep(3)
driver.switch_to.alert.accept() 
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[6]/button/span').click()    
time.sleep(1)


i = int(((l/4)*2)+15)
vat = driver.find_elements_by_class_name('pDetails')
pos_vatable_sales = vat[i].get_attribute('innerText')
pos_vat_amount = vat[i+2].get_attribute('innerText')
pos_vat_exempt_sales = vat[i+4].get_attribute('innerText')

vatable_sales = (float(sum(total)) - round(float(pos_vat_exempt_sales),2)) / 1.12
vat_amount = (float(sum(total)) - round(float(pos_vat_exempt_sales),2)) - vatable_sales
vat_exempt_sales = float(sum(total)) - (float(sum(total)) - round(float(pos_vat_exempt_sales),2))

pymsgbox.alert('Vatable Sales: ' + str(round(vatable_sales,2)) + '\n' + 'POS Vatable Sales: ' + str(pos_vatable_sales), timeout=5000)
time.sleep(1)
if vatable_sales == float(pos_vatable_sales) or round(vatable_sales,2) == float(pos_vatable_sales):
    pymsgbox.alert("Vatable Sales Match ✅",timeout=5000)
else:
    pymsgbox.alert("Vatable Sales Not Match ❌",timeout=5000)

pymsgbox.alert('Vat Amount: ' + str(round(vat_amount,2)) + '\n' + 'POS Vat Amount: ' + str(pos_vat_amount), timeout=5000)
time.sleep(1)
if vat_amount == float(pos_vat_amount) or round(vat_amount,2) == float(pos_vat_amount):
    pymsgbox.alert("Vat Amount Match ✅",timeout=5000)
else:
    pymsgbox.alert("Vat Amount Not Match ❌",timeout=5000)

pymsgbox.alert('Vat Exempt Sales: ' + str(round(vat_exempt_sales,2)) + '\n' + 'POS Vat Exempt Sales: ' + str(pos_vat_exempt_sales), timeout=5000)
time.sleep(1)
if vat_exempt_sales == float(pos_vat_exempt_sales) or round(vat_exempt_sales,2) == float(pos_vat_exempt_sales):
    pymsgbox.alert("Vat Exempt Sales Match ✅",timeout=5000)
else:
    pymsgbox.alert("Vat Exempt Sales Match ❌",timeout=5000)












