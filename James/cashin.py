from selenium import webdriver
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
time.sleep(2)


driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'CASH IN'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(2)
buttons = driver.find_elements_by_class_name('button-inner')
index = 11      
for index in range(index,24):
    if index == 24:
        buttons[23].click()
        time.sleep(2)
    buttons[index].click()
    time.sleep(1)

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-cashinout/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)

driver.execute_script('alert("ALL BUTTONS ARE WORKING PROPERLY: ✅ ");')
time.sleep(4)
driver.switch_to.alert.accept()
time.sleep(4)  

driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'CASH IN'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(1)

buttons = driver.find_elements_by_class_name('button-inner')  
for x in range(0,3):
    if x==0:
        buttons[15].click()
        time.sleep(2)
    buttons[21].click()
    time.sleep(2)
        
co_value = driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-cashinout/ion-content/div[2]/ion-item/div[1]/div/ion-input/input').get_attribute('value')     
time.sleep(2)
buttons[24].click()
time.sleep(2)


driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys("EXCESS")
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(2)
press('enter')
time.sleep(2)
press('enter')
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
press('enter')
time.sleep(2)
press('enter')
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

driver.execute_script('alert("ALL BUTTONS ARE WORKING PROPERLY: ✅" +"\\n"+"\\n" ++"\\n" +"CASH IN HAS BEEN SUCCESSFULLY SAVE: ✅ ");')           
time.sleep(5)

driver.switch_to.alert.accept()
time.sleep(2)

driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'CASH FUND'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(2)

buttons = driver.find_elements_by_class_name('button-inner')
for x in range(0,4):
    if x==0:
        buttons[15].click()
        time.sleep(1)
    buttons[21].click()
    time.sleep(1)
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(2)
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
driver.switch_to.alert.accept()
time.sleep(2)


driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/popover/ion-list/button[2]/div[1]/div').click()
time.sleep(2)

driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'CASH DECLARATION'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-cash-declaration/ion-content/div[2]/ion-grid/ion-row[4]/ion-col[3]/ion-item/div[1]/div/ion-input/input').send_keys(10)
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-cash-declaration/ion-content/div[2]/ion-grid/ion-row[6]/ion-col[1]/button/span').click()
time.sleep(2)
driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'REPORTS'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-reports/ion-content/div[2]/ion-list/button[1]/div[1]/div').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-xread-filter/ion-content/div[2]/form/ion-card[2]/ion-card-content/ion-row/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button/span/div[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-xread-filter/ion-content/div[2]/form/ion-card[3]/ion-row[2]/ion-col[1]/ion-item/ion-checkbox/button/span').click()
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-xread-filter/ion-content/div[2]/form/ion-card[3]/ion-row[2]/ion-col[2]/ion-item/ion-checkbox/button/span').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-xread-filter/ion-content/div[2]/form/ion-card[4]/ion-card-content/ion-row/ion-col[2]/button/span').click()
time.sleep(4)
driver.switch_to_window(driver.window_handles[1])
driver.minimize_window()
time.sleep(4)
press('p')
time.sleep(3)
press('enter') 
time.sleep(2)
press('enter')
time.sleep(2)
driver.switch_to_window(driver.window_handles[1])
driver.maximize_window()
time.sleep(3)

file = open("C:/Users/SERAN/Downloads/p.csv")
value = (file.readlines())[28]
index = 9
x = (value[index:len(value)])
print(x)
print(co_value)
if int(co_value) == int(x):
    driver.execute_script('alert("CASH IN VALUE MATCHED IN X-READING REPORT");')
else:
    driver.execute_script('alert("CASH IN VALUE DO NOT MATCHED IN X-READING REPORT");')


