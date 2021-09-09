from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common import alert
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
import random
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

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[10]/div[1]/div/ion-label').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-items/ion-content/div[1]/ion-fab/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('A1000')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('Adobo')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('Adobo')
time.sleep(1)
item = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input').get_attribute('value')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[4]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item[1]/div[1]/ion-radio/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[5]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item/div[1]/ion-radio/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[6]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item/div[1]/ion-radio/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[7]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[1]/span/div[1]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]').click()
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[9]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('100')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[10]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('120')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[11]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('100')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[12]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item[1]/div[1]/ion-radio/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[1]/ion-grid/ion-row[13]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item[2]/div[1]/ion-radio/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-items-crud/ion-content/div[2]/form/ion-card[2]/ion-row/ion-col/button[2]/span').click()
time.sleep(1)

item1 = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-items/ion-content/div[2]/ion-grid/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[2]').get_attribute('innerText')
time.sleep(1)
if item == item1:
    driver.execute_script("alert('ITEM ADDED SUCCESSFULLY✅');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)
else:
    driver.execute_script("alert('BUG❌');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-items/ion-header/ion-navbar/div[2]/ion-searchbar/div/input').send_keys('Adobo')
time.sleep(1)
search = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-items/ion-header/ion-navbar/div[2]/ion-searchbar/div/input').get_attribute('value')
time.sleep(1)
search1 = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-items/ion-content/div[2]/ion-grid/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[2]').get_attribute('innerText')
time.sleep(1)
if search == search1:
    driver.execute_script("alert('SEARCH TESTING MATCHED✅');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)
else:
    driver.execute_script("alert('BUG❌');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)   

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-items/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-home/ion-content/div[2]/ion-list/button[5]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

cashiering = driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item/div[1]/div/ion-label/ion-row/ion-col/button/div[1]/div/ion-label').get_attribute('innerText')
time.sleep(1)
if item == cashiering:
    driver.execute_script("alert('Item in Masterfile macthed in Cashiering✅');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)
else:
    driver.execute_script("alert('BUG❌');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)   
driver.execute_script("alert('POSITIVE TESTING DONE:PASSED✅');")
time.sleep(5)
driver.switch_to.alert.accept() 
time.sleep(3)

















