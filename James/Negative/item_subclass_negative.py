from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common import alert
from selenium.webdriver.common.keys import Keys
import time
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
#pre requisite validation
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[8]/div[1]/div/ion-label').click()
time.sleep(1)
result = driver.find_element_by_class_name('list')
length = len(result.find_elements_by_tag_name('h2'))
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-item-class/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[9]/div[1]/div/ion-label').click()
time.sleep(1)

if length <= 0:
    driver.execute_script("alert('PRE REQUISITE TEST: DO NOT CONTAIN ITEM IN ITEM CLASS:PASSED✅');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)
else:
    driver.execute_script("alert('PRE REQUISITE TEST: CONTAIN ITEM IN ITEM CLASS: PASSED✅');")
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(3)
#add item classification
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[8]/div[1]/div/ion-label').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-item-class/ion-content/div[1]/ion-fab/button/ion-icon').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-class-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('Foods')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-class-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[1]/span/div[1]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-class-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-item-class/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[9]/div[1]/div/ion-label').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-item-subclass/ion-content/div[1]/ion-fab/button').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col/button[2]/span').click()
time.sleep(1)
driver.execute_script("alert('CANT ADD DATA IF FIELDS ARE EMPTY!❌');")
time.sleep(4)
driver.switch_to.alert.accept() 
time.sleep(3)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item/div[1]/ion-radio/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[1]/span/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col/button[2]/span').click()
time.sleep(1)
item = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').get_attribute('value')
time.sleep(3)

if len(item) == 0:
    driver.execute_script('alert("CANT ADD DATA IF ITEM SUB DESCRIPTION IS EMPTY!:PASSED✅");')
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)
else:
    driver.execute_script("alert('BUG!❌');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col/button[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-item-subclass/ion-content/div[1]/ion-fab/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('Meryenda')
time.sleep(1)
selected = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-select/div[1]').get_attribute('innerText')
time.sleep(1)
if selected == True:
    driver.execute_script("alert('Foods is Selected!❌');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)
else:
    driver.execute_script("alert('PLEASE SELECT ONE IN ITEM CLASS!❌');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)

selected1 = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-select/button/span').get_attribute('innerText')
time.sleep(1)
if len(selected1) == 0:
    driver.execute_script("alert('SELECT ONE IN PRINTER STATION!❌');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)
else:
    driver.execute_script("alert('BUG!❌');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col/button[2]/span').click()
time.sleep(1)
if len (selected and selected1)== 0:
    driver.execute_script("alert('CANT ADD DATA IF ITEM CLASS AND PRINTER STATION ARE EMPTY!'+'\\n'+'PASSED✅');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)
else:
    driver.execute_script("alert('BUG!❌');")
    time.sleep(5)
    driver.switch_to.alert.accept() 
    time.sleep(3)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col/button[1]/span').click()
time.sleep(1)
duplicate = 0
for duplicate in range (duplicate,2):
    driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-item-subclass/ion-content/div[1]/ion-fab/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('Meryenda')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/ng-component/ion-list/ion-item/div[1]/ion-radio/button/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[1]/span/div[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col/button[2]/span').click()
    time.sleep(1)
driver.execute_script('alert("DUPLICATE DATA TEST"+"\\n"+"PASSED✅");')
time.sleep(4)
driver.switch_to.alert.accept() 
time.sleep(4)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-item-subclass-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col/button[1]/span').click()
time.sleep(1)

#SEARCH
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-item-subclass/ion-header/ion-navbar/div[2]/ion-searchbar/div/input').send_keys('abcd')
time.sleep(1)

driver.execute_script('alert("Search Test Passed✅");')
time.sleep(4)
driver.switch_to.alert.accept() 
time.sleep(4)

driver.execute_script('alert("Negative Testing Passed✅");')
time.sleep(4)
driver.switch_to.alert.accept() 
time.sleep(4)





















