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

#click MASTER FILE
driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'MASTER FILE'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(2)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-masterfiles/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-item[1]/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[5]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[5]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('@')
time.sleep(1)
find = 0
header = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-header-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[5]/ion-col/ion-item/div[1]/div/ion-input/input').get_attribute('value')
time.sleep(1)
print (header)
for i in header:
    if i.isdigit() or i == "-":
        continue
    else:
        find  +=1
    
if find >0:
    driver.execute_script('alert("VAT MUST NOT ACCEPT SPECIAL CHARACTERS EXCEPT DASH -❌ " );')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)  
else:
    driver.execute_script('alert("PASSED✅");')
    time.sleep(4)
    driver.switch_to.alert.accept() 
    time.sleep(4)
print(find)


driver.execute_script('alert("FOR ENHANCEMENT:ALERT MUST INDICATE IF DATA UPDATED SUCCESSFULLY!");')
time.sleep(4)
driver.switch_to.alert.accept() 
time.sleep(4)