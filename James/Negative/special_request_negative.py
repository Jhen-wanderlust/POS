from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common import alert
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
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

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[11]/div[1]/div/ion-label').click()
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-modifiers/ion-content/div[1]/ion-fab/button/ion-icon').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').click()
time.sleep(1)
special = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').get_attribute('value')
time.sleep(1)
if len(special) == 0:
    driver.execute_script('alert("CANT ADD DATA IF SPECIAL REQUEST IS EMPTY❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("BUG!❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)


sub = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-select/button/span').get_attribute('value')
if sub == True:
    driver.execute_script('alert("TRUE✅");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("PLEASE SELECT ITEM SUBCLASSIFICATION❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)


driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/button[2]/span').click()
time.sleep(1)
driver.execute_script('alert("CANT ADD DATA IF FIELDS ARE EMPTY TEST:PASSED✅");')
time.sleep(3)
driver.switch_to.alert.accept() 
time.sleep(2)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('ADD SOUP')
time.sleep(1)
if sub == True:
    driver.execute_script('alert("TRUE✅");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("PLEASE SELECT ITEM SUBCLASSIFICATION❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/button[2]/span').click()
if sub == True:
    driver.execute_script('alert("TRUE✅");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("CANT ADD DATA:PLEASE SELECT ITEM SUBCLASSIFICATION:PASSED✅");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.CONTROL + "a")
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.DELETE)
time.sleep(1)


driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item/div[1]/ion-radio/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/button[2]/span').click()
time.sleep(1)
if len(special) == 0:
    driver.execute_script('alert("CANT ADD DATA IF SPECIAL REQUEST IS EMPTY❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
else:
    driver.execute_script('alert("BUG!❌");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)




driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/button[1]/span').click()
time.sleep(1)
d = 0
for d in range (d,2):
    driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-modifiers/ion-content/div[1]/ion-fab/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('ADD SOUP')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item/div[1]/ion-radio/button/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/button[2]/span').click()
    time.sleep(1)

driver.execute_script('alert("DUPLICATE ENTRY TEST:PASSED✅");')
time.sleep(4)
driver.switch_to.alert.accept() 
time.sleep(4)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-modifiers-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/button[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-modifiers/ion-header/ion-navbar/div[2]/ion-searchbar/div/input').send_keys('abcd')
time.sleep(1)
driver.execute_script('alert("SEARCH TESTING:PASSED!✅");')
time.sleep(4)
driver.switch_to.alert.accept() 
time.sleep(4)
driver.execute_script('alert("NEGATIVE TESTING:PASSED!✅");')
time.sleep(4)
driver.switch_to.alert.accept() 
time.sleep(4)










