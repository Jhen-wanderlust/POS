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
time.sleep(1)
press('enter')
time.sleep(1)
press('enter')
time.sleep(1)
press('enter')
time.sleep(1)
press('enter')
time.sleep(1)

obj = driver.switch_to.alert
time.sleep(1)
obj.accept()
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('1')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

#MEMC COMBO 1
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[2]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/combo-picker/ion-content/div[2]/ion-scroll/div/div/ion-toolbar/div[2]/button/span').click()
time.sleep(1)



#MEMC COMBO 2 VAT E
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[3]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/combo-picker/ion-content/div[2]/ion-scroll/div/div/ion-toolbar/div[2]/button/span').click()
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[2]/ion-content/div[2]/ion-list[1]/ion-list[3]/div/ion-item-sliding/ion-item/div[1]/div/ion-label/button/h2[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-action-sheet/div/div/div[1]/button[5]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div[2]/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[2]/ion-content/div[2]/ion-list[1]/ion-list[6]/div/ion-item-sliding/ion-item/div[1]/div/ion-label/button/h2[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-action-sheet/div/div/div[1]/button[5]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div[2]/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
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
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[1]/span/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)

#senior info
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-form/ion-content/div[2]/form/ion-item[1]/div[1]/div/ion-input/input').send_keys('Senior')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-form/ion-content/div[2]/form/ion-item[2]/div[1]/div/ion-input/input').send_keys('123456')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-form/ion-header/ion-navbar/ion-buttons[2]/button').click()
time.sleep(1)

#price
memc_combo_1 = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[5]/div[1]/h4[2]').get_attribute('innerText')
time.sleep(1)
memc_combo_2 = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[6]/div[1]/h4[2]').get_attribute('innerText')
time.sleep(1)
st = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[7]/h4[2]').get_attribute('innerText')
time.sleep(1)

print('price',memc_combo_1)
print('price',memc_combo_2)
print('price',st)

#subtotal computation
subtotal =  float (memc_combo_1) + float (memc_combo_2)
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
print('subtotal computation',st)
print('subtotal computation',subtotal)

#VAT ADJUSTMENT
#MEMC LESS SALES WITHOUT VAT (MEMC)
memc = 200
vat_adj= 200/1.12
less_vat = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[8]/h4[2]').get_attribute('innerText')
time.sleep(1)
less_vat1 = less_vat[2:]
vat_comp = memc - vat_adj
vat_comp2 = (np.round(vat_comp, 2))
if float(less_vat1) == vat_comp2:
    driver.execute_script('alert("VAT ADJUSTMENT COMPUTATION MATCHED✅ ");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("VAT ADJUSTMENT COMPUTATION DOES NOT MATCH❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
print('VAT ADJUSTMENT computation',less_vat1)
print('VAT ADJUSTMENT computation',vat_comp2)

#SALES WITHOUT VAT
#MEMC ITEMS/ 1.12 + VAT EXEMPT ITEMS // 100/1.12 + 230 (319.2857143)
wo_vat = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[9]/h4[2]').get_attribute('innerText')
time.sleep(1)
wo_vat1 = vat_adj + float(memc_combo_2)
wo_vat2 = (np.round(wo_vat1, 2))
if float(wo_vat) == wo_vat2:
    driver.execute_script('alert("SALES WITHOUT VAT COMPUTATION MATCHED✅ ");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("SALES WITHOUT VAT COMPUTATION DOES NOT MATCH❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
print('SALES WITHOUT VAT computation',wo_vat)
print('SALES WITHOUT VAT computation',wo_vat2)

#SENIOR
#MEMC SALES WITHOUT VAT MEMC* .20
senior_disc = 0.20
senior = vat_adj * senior_disc
senior2 = (np.round(senior, 2))
sen= driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[10]/h4[2]').get_attribute('innerText')
time.sleep(1)
sen2 = sen[2:]
if senior2 == float(sen2):
    driver.execute_script('alert("SENIOR DISCOUNT COMPUTATION MATCHED✅ ");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("SENIOR DISCOUNT COMPUTATION DOES NOT MATCH❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
print('SENIOR DISCOUNT computation',senior2)
print('SENIOR DISCOUNT computation',sen2)

#SERVICE CHARGE DISCOUNT
#DISCOUNT * SERVICE CHARGE PERCENT
sc_disc= driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[11]/h4[2]').get_attribute('innerText')
time.sleep(1)
sc= 0.10
sc_disc1 = float(sen2) * sc
sc_disc2 = (np.round(sc_disc1, 2))
if float(sc_disc) == sc_disc2:
    driver.execute_script('alert("SERVICE CHARGE DISCOUNT COMPUTATION MATCHED✅ ");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("SERVICE CHARGE DISCOUNT COMPUTATION DOES NOT MATCH❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
print('SERVICE CHARGE DISCOUNT computation',sc_disc)
print('SERVICE CHARGE DISCOUNT computation',sc_disc2)

#SERVICE CHARGE
#VATABLE ITEM/1.12 *SERVICE CHARGE PERCENT
#VAT EXEMPT*SERVICE CHARGE AMOUNT
#SUMMATION
#LESS SERVICE CHARGE DISCOUNT
service_charge = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[12]/h4[2]').get_attribute('innerText')
time.sleep(1)
vat_item = (float(memc_combo_1)/1.12)*sc
vat_exempt= float(memc_combo_2) * sc
summation= vat_item + vat_exempt
summation2 = summation - 3.5714287
summation3= (np.round(summation2,2))
if float(service_charge) == summation3:
    driver.execute_script('alert("SERVICE CHARGE  COMPUTATION MATCHED✅ ");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("SERVICE CHARGE  COMPUTATION DOES NOT MATCH❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
print('SERVICE CHARGE  computation',service_charge)
print('SERVICE CHARGE  computation',summation3)

#TOTAL //460+41.75-10.71-17.857
#SUBTOTAL+ SERVICE CHARGE less vat adj less senior amount

total = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[13]/h4[2]').get_attribute('innerText')
time.sleep(1)
total2 = float(st) + float(service_charge) - float (less_vat1) - float(sen2)
total3 = (np.round(total2,2))
if float(total) == total3:
    driver.execute_script('alert("TOTAL COMPUTATION MATCHED✅ ");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("TOTAL COMPUTATION DOES NOT MATCH❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
print('TOTAL computation',total)
print('TOTAL computation',total3)

driver.execute_script('alert("ITEM 9 IN SCENARIO 7 & 8 PASSED!✅ ");')
time.sleep(4)
driver.switch_to.alert.accept() 
time.sleep(4)



