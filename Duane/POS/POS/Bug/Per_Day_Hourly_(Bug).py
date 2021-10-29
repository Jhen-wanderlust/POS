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


bug = 0
driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'REPORTS'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-reports/ion-content/div[2]/ion-list/button[4]/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[2]/ion-row[1]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[6]/span/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[2]/ion-row[2]/ion-col[1]/ion-item/div[1]/div/ion-datetime/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-picker-cmp/div/div[1]/div[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[2]/ion-row[2]/ion-col[2]/ion-item/div[1]/div/ion-datetime/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-picker-cmp/div/div[1]/div[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[3]/ion-row[2]/ion-col[2]/ion-item/ion-checkbox/button/span').click()
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[3]/ion-row[2]/ion-col[1]/ion-item/ion-checkbox/button/span').click()
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[1]/ion-card-content/ion-row/ion-col[2]/ion-item/ion-checkbox/button/span').click()
time.sleep(1)

cbx = driver.find_elements_by_class_name('item-cover')
now = datetime.datetime.now()

if now.strftime("%A") == "Sunday":
    day = 0
elif now.strftime("%A") == "Monday":  
    day = 1
elif now.strftime("%A") == "Tuesday":  
    day = 2
elif now.strftime("%A") == "Wednesday":  
    day = 3
elif now.strftime("%A") == "Thursday":  
    day = 4
elif now.strftime("%A") == "Friday": 
    day = 5
elif now.strftime("%A") == "Saturday":  
    day = 6

time.sleep(1)
index = 8
lst = [0,1,2,3,4,5,6,7,'SUNDAY','MONDAY','TUESDAY','WEDNEDAY','THURSDAY','FRIDAY','SATURDAY']
for index in range(index,7):
    if index != day:
        if cbx[index].is_enabled():
            pymsgbox.alert(lst[index] + " MUST BE DISABLE ❌",timeout = 3000)
            bug += 1
        else:
            pymsgbox.alert(lst[index] + " ✅",timeout = 3000)

time.sleep(2)
if bug > 0:
    pymsgbox.alert('DAYS THAT DOES NOT EXIST IN THE SPECIFC DATE MUST BE DISABLE ❌')
else:
    pymsgbox.alert('ALL PASSED ✅')