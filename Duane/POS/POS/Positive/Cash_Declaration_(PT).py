from selenium.common.exceptions import WebDriverException 
from tkinter.constants import S
import keyboard
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from keyboard import press
import pymsgbox
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import datetime
import os
import re 

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
buttons[15].click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/popover/ion-list/button[2]/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-home/ion-content/div[2]/ion-list/button[4]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-cash-declaration/ion-content/div[2]/form/ion-grid/ion-row[6]/ion-col[3]/button/span').click()
time.sleep(1)
pymsgbox.alert('CANCEL BUTTON ✅',timeout=3000)  
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-home/ion-content/div[2]/ion-list/button[4]/span').click()
time.sleep(1)

cd = driver.find_elements_by_class_name('text-input')
time.sleep(1)

total = []

for i in range(2):
    for x in range(12):
        cd[x].click()
        press('5')
        time.sleep(0.25)
        value = cd[x].get_attribute('value')
        if x == 0:
            value = float(value) * 0.05
        elif x == 1:
            value = float(value) * 0.10
        elif x == 2:
            value = float(value) * 0.25
        elif x == 3:
            value = float(value) * 1
        elif x == 4:
            value = float(value) * 5
        elif x == 5:
            value = float(value) * 10        
        elif x == 6:
            value = float(value) * 20
        elif x == 7:
            value = float(value) * 50
        elif x == 8:
            value = float(value) * 100      
        elif x == 9:
            value = float(value) * 200
        elif x == 10:
            value = float(value) * 500
        elif x == 11:
            value = float(value) * 1000
            
            
        if i == 1:                 
            time.sleep(0.25)
            total.append(value)  

    if i == 0:
        driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-cash-declaration/ion-content/div[2]/form/ion-grid/ion-row[6]/ion-col[2]/button/span').click()
        time.sleep(1)
        pymsgbox.alert('CLEAR BUTTON ✅',timeout=3000)    

    if i == 1:
        val = cd[12].get_attribute('value')    
        total1 = val.replace(",","")
        time.sleep(1)

        if sum(total) == int(float(total1)):
            pymsgbox.alert('CASH DECLARATION TOTAL MATCH ✅\n' + str(sum(total)) + ' = ' + total1,timeout=5000)
        else:
            pymsgbox.alert('CASH DECLARATION TOTAL MATCH ❌',timeout=5000)

time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-cash-declaration/ion-content/div[2]/form/ion-grid/ion-row[6]/ion-col[1]/button/span').click()
time.sleep(1)
pymsgbox.alert('CASH DECLARATION SAVE ✅',timeout=3000) 
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-home/ion-content/div[2]/ion-list/button[7]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-reports/ion-content/div[2]/ion-list/button[1]/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-xread-filter/ion-content/div[2]/form/ion-card[3]/ion-row[2]/ion-col[2]/ion-item/ion-checkbox/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-xread-filter/ion-content/div[2]/form/ion-card[3]/ion-row[2]/ion-col[1]/ion-item/ion-checkbox/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-xread-filter/ion-content/div[2]/form/ion-card[2]/ion-card-content/ion-row/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button/span/div[1]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-xread-filter/ion-content/div[2]/form/ion-card[4]/ion-card-content/ion-row/ion-col[2]/button/span').click()
time.sleep(4)
driver.switch_to_window(driver.window_handles[1])
driver.minimize_window()
time.sleep(1)
press('p')
time.sleep(1)
press('enter')
time.sleep(1)
press('q')
time.sleep(1)
press('enter')
time.sleep(1)
driver.maximize_window()
time.sleep(1)

file = open("C:/Users/ASUS/Downloads/p.csv")
value = (file.readlines())[32]
index = 13
x = (value[index:len(value)])
cash_declare = int(x)

if sum(total) == int(cash_declare):
    pymsgbox.alert('CASH DECLARATION VALUE MATCH ✅\n' + str(sum(total)) + ' = ' + str(cash_declare),timeout=6000)
else:
    pymsgbox.alert('CASH DECLARATION NOT MATCH ❌',timeout=5000)

time.sleep(1)
pymsgbox.alert('CANCEL BUTTON ✅\nCLEAR BUTTON ✅\nCASH DECLARATION TOTAL MATCH ✅\nCASH DECLARATION SAVE ✅\nCASH DECLARATION VALUE MATCH ✅')
