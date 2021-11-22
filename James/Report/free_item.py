from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common import alert
from selenium.webdriver.common.keys import Keys
import time
import keyboard
import pandas as pd
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
time.sleep(2)
obj.accept()
time.sleep(2)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

#ITEM 1
#adobo
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[1]/button/div[1]/div').click()
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


#free transaction
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)

#reason
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-free-reason/ion-content/div[2]/form/ion-row[1]/ion-list').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-free-reason/ion-content/div[2]/form/ion-item/div[1]/div/ion-input/input').send_keys('FREE')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-free-reason/ion-content/div[2]/form/ion-row[2]/ion-item/div[1]/div/ion-label/button/span').click()
time.sleep(1)

press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)

driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/popover/ion-list/button[2]/div[1]/div').click()
time.sleep(1)

#Reports
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-home/ion-content/div[2]/ion-list/button[7]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-reports/ion-content/div[2]/ion-list/button[4]/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[2]/ion-row[1]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[4]/span/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[1]/ion-card-content/ion-row/ion-col[2]/ion-item/ion-checkbox/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[2]/ion-row[2]/ion-col[1]/ion-item/div[1]/div/ion-datetime/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-picker-cmp/div/div[1]/div[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[2]/ion-row[2]/ion-col[2]/ion-item/div[1]/div/ion-datetime/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-picker-cmp/div/div[1]/div[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[3]/ion-row[2]/ion-col[2]/ion-item/ion-checkbox/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[3]/ion-row[2]/ion-col[1]/ion-item/ion-checkbox/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-header/ion-navbar/div[2]/ion-title/div/button/span').click()
time.sleep(1)


#SAVE FILE
driver.maximize_window()
time.sleep(4)
press('f')
time.sleep(3)
press('enter') 
time.sleep(2)

