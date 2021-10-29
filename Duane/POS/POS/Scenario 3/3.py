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
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)




driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[1]/button/div[1]/div').click()
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[1]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[3]/div[1]/div/ion-label/ion-row/ion-col[6]/button/div[1]/div').click()
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[3]/div[1]/div/ion-label/ion-row/ion-col[6]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[3]/button/div[1]/div').click()
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[3]/button/div[1]/div').click()
time.sleep(1)


d = driver.find_element_by_class_name('seatheader')
l = len(d.find_elements_by_tag_name('h2'))
length = l / 4
i = 0
fishFillet = 0
extraRice = 0
nilagaVatE = 0

t = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[2]/ion-content/div[2]/ion-list[1]/button/div[1]/h2').get_attribute('innerText')
pos_total = t[2:]
pos_total = pos_total.replace(',','')
iwv_price = []
while i < int(length):
    items = driver.find_elements_by_class_name('itemcode')
    price = driver.find_elements_by_class_name('seatTotal')
    
    if items[i].get_attribute('innerText') == "FISH FILLET":
        p = price[(i*2)+2].get_attribute('innerText')
        iwv = p[2:]
        iwv_price.append(float(iwv))
        fishFillet += 1  
    if items[i].get_attribute('innerText') == "NILAGA 'VAT E\"":
        nilagaVatE += 1      
    if items[i].get_attribute('innerText') == "EXTRA RICE":
        p = price[(i*2)+2].get_attribute('innerText')
        iwv = p[2:]
        iwv_price.append(float(iwv))
        extraRice += 1    
    i += 1 

price = driver.find_elements_by_class_name('seatTotal')
time.sleep(1)
total = []
length = l / 2
i = 2
while i < length:
    total.append(float((price[i].get_attribute('innerText')[2:])))
    i += 2    

time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[3]/button/span').click()
time.sleep(3)
driver.switch_to.alert.accept() 
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[6]/button/span').click()    
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[2]/div/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[1]/span/div[1]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-form/ion-content/div[2]/form/ion-item[1]/div[1]/div/ion-input/input').send_keys('customer')
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-form/ion-content/div[2]/form/ion-item[2]/div[1]/div/ion-input/input').send_keys('1')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-form/ion-header/ion-navbar/ion-buttons[2]/button').click()
time.sleep(2)


pymsgbox.alert('Fish Fillet: ' + str(fishFillet) + '\n' + 'Extra Rice: ' + str(extraRice) + '\n' + 'Nilaga Vat E: ' + str(nilagaVatE)  + '\n' + 'POS_Subtotal: ' + str(pos_total) + '\n' + 'Computation Subtotal: ' + str(sum(total)), timeout=7000)

if float(pos_total) == float(sum(total)):
    pymsgbox.alert("Subtotal Value Match ✅",timeout=4000)
else:
    pymsgbox.alert("Subtotal Value Not Match ❌",timeout=4000)

seat = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[3]/h4').get_attribute('innerText')
seat = seat[6:]

item_wout_vat_price = round(float(sum(total)) - float(sum(iwv_price)),2) 
pax_vatable = round(float(sum(iwv_price) / int(seat)),2)
sales_without_vat = round(float((pax_vatable) / 1.12) + float(item_wout_vat_price),2) 
vat_adjustment = round(float(pax_vatable) -  (float(sales_without_vat) - float(item_wout_vat_price)),2)    
pax_without_vat = round(float(item_wout_vat_price / int(seat)),2) 
senior = round((float((pax_vatable / 1.12) + pax_without_vat) * 0.2),2)  
Ftotal = round((float(sum(total)) - float(vat_adjustment) - float(senior)),2) 
vatabale_sales = round(float(float((pax_vatable * (int(seat)-1))) / 1.12),2)
vat_amount = round(float(float((pax_vatable * (int(seat)-1))) - float(vatabale_sales)),2)
vat_exempt_sales = round(float((pax_vatable) / 1.12) + float(item_wout_vat_price),2)


i = int(((l/4)*2)+15)
vat = driver.find_elements_by_class_name('pDetails')
pos_vat_adjustment = vat[i-8].get_attribute('innerText')
pos_sales_without_vat = vat[i-6].get_attribute('innerText')
pos_senior = vat[i-4].get_attribute('innerText')
pos_Ftotal = vat[i].get_attribute('innerText')
pos_vatable_sales = vat[i+2].get_attribute('innerText')
pos_vat_amount = vat[i+4].get_attribute('innerText')
pos_vat_exempt_sales = vat[i+6].get_attribute('innerText')

pos_vat_adjustment = pos_vat_adjustment.replace(',','')
pos_sales_without_vat = pos_sales_without_vat.replace(',','')
pos_senior = pos_senior.replace(',','')
pos_Ftotal = pos_Ftotal.replace(',','')
pos_vatable_sales = pos_vatable_sales.replace(',','')
pos_vat_amount = pos_vat_amount.replace(',','')
pos_vat_exempt_sales = pos_vat_exempt_sales.replace(',','')
pos_vat_adjustment = float((pos_vat_adjustment)[2:])
pos_senior = float((pos_senior)[2:])
time.sleep(1)

pymsgbox.alert('Vat Adjustment: ' + str(vat_adjustment) + '\n' + 'POS Vat Adjustment: ' + str(pos_vat_adjustment), timeout = 3000)
if float(vat_adjustment) == float(pos_vat_adjustment):
    pymsgbox.alert('Vat Adjustment Match ✅',timeout = 3000)
else:
    pymsgbox.alert('Vat Adjustment Not Match ❌',timeout = 3000)

time.sleep(0.5)

pymsgbox.alert('Sales Without Vat: ' + str(sales_without_vat) + '\n' + 'Sales Without Vat: ' + str(pos_sales_without_vat), timeout = 3000)
if float(sales_without_vat) == float(pos_sales_without_vat):
    pymsgbox.alert('Sales Without Vat Match ✅',timeout = 3000)
else:
    pymsgbox.alert('Sales Without Vat Not Match ❌',timeout = 3000)

time.sleep(0.5)

pymsgbox.alert('Senior: ' + str(senior) + '\n' + 'POS Senior: ' + str(pos_senior), timeout = 3000)
if float(senior) == float(pos_senior):
    pymsgbox.alert('Senior Match ✅',timeout = 3000)
else:
    pymsgbox.alert('Senior Not Match ❌',timeout = 3000)  

time.sleep(0.5)

pymsgbox.alert('Total: ' + str(Ftotal) + '\n' + 'POS Total: ' + str(pos_Ftotal), timeout = 3000)
if float(Ftotal) == float(pos_Ftotal):
    pymsgbox.alert('Total Match ✅',timeout = 3000)
else:
    pymsgbox.alert('Total Not Match ❌',timeout = 3000)      

time.sleep(0.5)

pymsgbox.alert('Vatable Sales: ' + str(vatabale_sales) + '\n' + 'POS Vatable Sales: ' + str(pos_vatable_sales), timeout = 3000)
if float(vatabale_sales) == float(pos_vatable_sales):
    pymsgbox.alert('Vatable Sales Match ✅',timeout = 3000)
else:
    pymsgbox.alert('Vatable Sales Not Match ❌',timeout = 3000)     

time.sleep(0.5)

pymsgbox.alert('Vatable Amount: ' + str(vat_amount) + '\n' + 'POS Vatable Amount: ' + str(pos_vat_amount), timeout = 3000)
if float(vat_amount) == float(pos_vat_amount):
    pymsgbox.alert('Vat Amount Match ✅',timeout = 3000)
else:
    pymsgbox.alert('Vat Amount Not Match ❌',timeout = 3000)   

time.sleep(0.5)

pymsgbox.alert('Vat Exempt Sales: ' + str(vat_exempt_sales) + '\n' + 'POS Vat Exempt Sales: ' + str(pos_vat_exempt_sales), timeout = 3000)
if float(vat_exempt_sales) == float(pos_vat_exempt_sales):
    pymsgbox.alert('Vat Exempt Sales Match ✅',timeout = 3000)
else:
    pymsgbox.alert('Vat Exempt Sales Not Match❌',timeout = 3000)    

