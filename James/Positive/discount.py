from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common import alert
from selenium.webdriver.common.keys import Keys
import time
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
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-security-code/ion-content/div[2]/ion-grid/ion-row[5]/ion-col[2]/input").send_keys("HEW-YRP-NWA-ANH-EWP-TCW-PNM-NHO-PYA-APH")
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

#click MASTER FILE
driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'MASTER FILE'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(2)

#discount by amount
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[13]/div[1]/div/ion-label').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-discount/ion-content/div[1]/ion-fab/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('REG')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('Regular')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item[1]/div[1]/ion-radio/button/span').click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('10')
time.sleep(1)
amount = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col/ion-item/div[1]/div/ion-input/input').get_attribute('value')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[6]/ion-col/button[2]/span').click()
time.sleep(1)
reg = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-discount/ion-content/div[2]/ion-list/ion-item/div[1]/div/ion-label/div/h2').get_attribute('innerText')
time.sleep(1)


#discount by percent
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-discount/ion-content/div[1]/ion-fab/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('STD')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('Student')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item[2]/div[1]/ion-radio/button/span').click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('5')
time.sleep(1)
percent = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col/ion-item/div[1]/div/ion-input/input').get_attribute('value')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[5]/ion-col/ion-list/ion-radio-group/ion-item[2]/div[1]/ion-radio/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-discount-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[6]/ion-col/button[2]/span').click()
time.sleep(1)
std = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-discount/ion-content/div[2]/ion-list/ion-item[2]/div[1]/div/ion-label/div/h2').get_attribute('innerText')
time.sleep(1)



driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-discount/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-home/ion-content/div[2]/ion-list/button[5]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item/div[1]/div/ion-label/ion-row/ion-col[1]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[3]/button/span').click()
time.sleep(1)

press('enter')
time.sleep(1)
press('enter')
time.sleep(1)
press('enter')
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(2)
press('enter')
time.sleep(1)
press('enter')
time.sleep(1)
press('enter')
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[6]/button/span').click()
time.sleep(1)
bal= driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[10]/h4[2]').get_attribute('innerText')
time.sleep(1)

if int (float(bal)) == 150.00:
    driver.execute_script('alert("BALANCE IS 150 PESOS");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("BUG❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)

print (bal)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[2]/div/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
reg1 = driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[3]/span/div[2]').get_attribute('innerText')
time.sleep(1)
std1 = driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[4]/span/div[2]').get_attribute('innerText')
time.sleep(1)
if reg == reg1 and std == std1:
    driver.execute_script('alert("DISCOUNT IN MASTERFILE REFLECTS IN CASHIERING✅");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("BUG❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)

driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[3]/span/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div[1]/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div[2]/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

bal1 = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[11]/h4[2]').get_attribute('innerText')
time.sleep(1)
total = int (float(bal))- int (float(bal1))
if  int (total) == int (amount):
    driver.execute_script('alert("DISCOUNT SUCCESFULLY APPLIED!✅ ");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("BUG❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
print(amount)
print (total)

#percent
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[2]/div/div/ion-item/div[1]/button/span/ion-icon').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button[2]/span').click()
time.sleep(1)
if int (float(bal)) == 150.00:
    driver.execute_script('alert("BALANCE IS 150 PESOS");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("BUG❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[2]/div/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[4]/span/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div[1]/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div[2]/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

bal2= driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[2]/div/div[11]/h4[2]').get_attribute('innerText')
time.sleep(1)

total1 = int (percent) / 100 
total2 = int(float(bal)) - float(bal2)
total3 = float(total2) / int(float(bal))

print (bal2)
print(total1)
print(total2)
print(total3)
if float(total3) == float(total1):
    driver.execute_script('alert("DISCOUNT BY PERCENT SUCCESSFULL APPLIED✅");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("BUG❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)














