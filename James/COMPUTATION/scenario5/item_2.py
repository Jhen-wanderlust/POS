from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common import alert
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
from keyboard import press
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("nwapp=C:/Program Files (x86)/LSTV/POS/frontend/KRAKEN_RESTO.exe")

driver = webdriver.Chrome("C:/Users/SERAN/Desktop/Selenium Jar Files/nwjs-sdk-v0.54.0-win-x64/chromedriver", options= options)

#maximize window
driver.maximize_window()
time.sleep(2)

#login
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(4)
time.sleep(1)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[8]/ion-col/button[2]/span").click()
time.sleep(2)
driver.switch_to.alert.accept() 
time.sleep(3)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-security-code/ion-content/div[2]/ion-grid/ion-row[5]/ion-col[2]/input").send_keys("CCW-PCH-TPP-AWA-EXH-PNO-AHP-NWX-NNP-ZRW")
time.sleep(1)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-security-code/ion-content/div[2]/ion-grid/ion-row[6]/ion-col/button/span").click()
time.sleep(2)

#input user code
driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/ion-card/ion-list/ion-item[1]/div[1]/div/ion-input/input").send_keys("lstv")
time.sleep(1)

#input password
driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/ion-card/ion-list/ion-item[2]/div[1]/div/ion-input/input").send_keys("lstventures")
time.sleep(1)

#click login
driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/div/button[1]/span").click()
time.sleep(3)

#cashfund
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-home/ion-content/div[2]/ion-list/button[3]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/numpad/ion-content/div[2]/div/ion-grid/ion-row[2]/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/numpad/ion-content/div[2]/div/ion-grid/ion-row[4]/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(1)

press('enter')
time.sleep(2)
press('enter')
time.sleep(2)
press('enter')
time.sleep(2)
press('enter')
time.sleep(2)
press('enter')
time.sleep(2)

obj = driver.switch_to.alert
time.sleep(1)
obj.accept()
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

#sinigang
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[2]/button/div[1]/div').click()
time.sleep(1)
#nilaga
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[3]/button/div[1]/div').click()
time.sleep(1)

#billout
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[6]/button/span').click()
time.sleep(1)

press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
obj.accept()
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[2]/div/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[3]/span/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)

#price
sinigang = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[5]/div/h4[2]').get_attribute('innerText')
time.sleep(1)
nilaga = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[6]/div/h4[2]').get_attribute('innerText')
time.sleep(1)
st = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[7]/h4[2]').get_attribute('innerText')
time.sleep(1)

#subtotal computation
subtotal =  float (sinigang) + float (nilaga)
if float(st) == subtotal:
    driver.execute_script('alert("SUBTOTAL COMPUTATION MATCHED✅ ");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("SUBTOTAL COMPUTATION DOES NOT MATCH❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
print(st)
print(subtotal)

#discount computation
reg_dsc = 0.10
regular = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[10]/h4[2]').get_attribute('innerText')
time.sleep(1)
regular1 = regular[2:]
reg = float(st) * reg_dsc
if reg == float(regular1):
    driver.execute_script('alert("DISCOUNT COMPUTATION MATCHED AND APPLIED✅ ");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("DISCOUNT COMPUTATION DOES NOT MATCH AND APPLY❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)  
print(reg)
print(regular1)
#service charge computation
sc_total = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[11]/h4[2]').get_attribute('innerText')
time.sleep(1)
sc = 0.10
vatable =  + float (sinigang) / 1.12 * reg_dsc
string_vat = str(vatable)
string_vat1 =string_vat[0:5]


#vat exempt computation
vat_exempt = float(nilaga) * sc

srvc_chrg= float(string_vat1)+ vat_exempt

if float(sc_total) == srvc_chrg:
    driver.execute_script('alert("SERVICE CHARGE MATCHED AND APPLIED✅ ");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("SERVICE CHARGE DOES NOT MATCH AND APPLY❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4) 

print(sc_total)
print( srvc_chrg)

#total amount computation
total_amount = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[12]/h4[2]').get_attribute('innerText')
time.sleep(1)
total_disc = reg - srvc_chrg

total1 = float(st) - total_disc
if float (total_amount) == total1:
    driver.execute_script('alert("TOTAL AMOUNT COMPUTATION MATCHED ✅ ");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("TOTAL AMOUNT DOES NOT MATCH ❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4) 

driver.execute_script('alert("ITEM 2 COMPUTATION IN SCENARIO 5 PASSED✅");')
time.sleep(4)
driver.switch_to.alert.accept() 
time.sleep(4) 
print(total_amount)
print(total1)
