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
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-security-code/ion-content/div[2]/ion-grid/ion-row[5]/ion-col[2]/input").send_keys("CRO-YPW-AHW-ZWN-NOZ-AHR-NCN-EPC-YYH-PAO")
time.sleep(1)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-security-code/ion-content/div[2]/ion-grid/ion-row[6]/ion-col/button/span").click()
time.sleep(2)

#input user code
driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/ion-card[2]/ion-list/ion-item[1]/div[1]/div/ion-input/input").send_keys("lstv")
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

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)

#pay cash
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[4]/div[1]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-footer/ion-row/a[2]').click()
time.sleep(1)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
obj = driver.switch_to.alert
time.sleep(1)
obj.accept()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button/span').click()
time.sleep(1)

#ITEM 2
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
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

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)

#pay cash
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[4]/div[1]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-footer/ion-row/a[2]').click()
time.sleep(1)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
obj = driver.switch_to.alert
time.sleep(1)
obj.accept()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button/span').click()
time.sleep(1)

#ITEM 3
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

#caldereta
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[4]/button/div[1]').click()
time.sleep(1)

#adobo
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[1]/button/div[1]/div').click()
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

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)

#pay cash
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[4]/div[1]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-footer/ion-row/a[2]').click()
time.sleep(1)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
obj = driver.switch_to.alert
time.sleep(1)
obj.accept()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button/span').click()
time.sleep(1)

#item 4
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

#burger steak
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[5]/button/div[1]/div').click()
time.sleep(1)
#EXTRA RICE
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[3]/div[1]/div/ion-label/ion-row/ion-col[6]/button/div[1]/div').click()
time.sleep(1)
#NILAGA 'VAT E"
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[3]/button/div[1]/div').click()
time.sleep(1)
#SODA
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[3]/div[1]/div/ion-label/ion-row/ion-col[5]/button/div[1]/div').click()
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

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)

#pay cash
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[4]/div[1]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-footer/ion-row/a[2]').click()
time.sleep(1)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
obj = driver.switch_to.alert
time.sleep(1)
obj.accept()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button/span').click()
time.sleep(1)

#ITEM 5
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

#FISH FILLET
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[1]/button/div[1]/div').click()
time.sleep(1)
#CALDERETA
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[4]/button/div[1]/div').click()
time.sleep(1)
#NILAGA 'VAT E"
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

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)

#pay cash
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[4]/div[1]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-footer/ion-row/a[2]').click()
time.sleep(1)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
obj = driver.switch_to.alert
time.sleep(1)
obj.accept()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button/span').click()
time.sleep(1)

#ITEM 6
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

#ADOBO
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[1]/button/div[1]/div').click()
time.sleep(1)
#SISIG
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[5]/button/div[1]/div').click()
time.sleep(1)
#NILAGA 'VAT E"
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

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)

#pay cash
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[4]/div[1]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-footer/ion-row/a[2]').click()
time.sleep(1)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
obj = driver.switch_to.alert
time.sleep(1)
obj.accept()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button/span').click()
time.sleep(1)

#ITEM 7
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('3')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

#caldereta
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('3')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[4]/button/div[1]/div').click()
time.sleep(1)
#SInigang
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('3')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[2]/button/div[1]/div').click()
time.sleep(1)
#NILAGA 'VAT E"
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('3')
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

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)

#pay cash
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[4]/div[1]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-footer/ion-row/a[2]').click()
time.sleep(1)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
obj = driver.switch_to.alert
time.sleep(1)
obj.accept()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button/span').click()
time.sleep(1)


#ITEM 8
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('4')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

#caldereta
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('4')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[4]/button/div[1]/div').click()
time.sleep(1)
#SISIG
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('4')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[5]/button/div[1]/div').click()
time.sleep(1)
#NILAGA 'VAT E"
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('4')
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

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)

#pay cash
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[4]/div[1]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-footer/ion-row/a[2]').click()
time.sleep(1)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
obj = driver.switch_to.alert
time.sleep(1)
obj.accept()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button/span').click()
time.sleep(1)

#ITEM 9
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('4')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)

#SISIG
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('4')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[5]/button/div[1]/div').click()
time.sleep(1)
#NILAGA 'VAT E"
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('4')
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

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)

#pay cash
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[4]/div[1]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-footer/ion-row/a[2]').click()
time.sleep(1)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
obj = driver.switch_to.alert
time.sleep(1)
obj.accept()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button/span').click()
time.sleep(1)

#ITEM 10
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-content/div[2]/ion-tabs/ion-tab[1]/page-table-view[2]/ion-content/div[2]/div/button[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('5')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
#SINIGANG
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('5')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[1]/div[1]/div/ion-label/ion-row/ion-col[2]/button/div[1]/div').click()
time.sleep(1)

#SISIG
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-footer/ion-toolbar/div[2]/ion-row/ion-col[2]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/div/input').send_keys('3')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[4]/button[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-ordering/ion-content/div[2]/div/div[1]/ion-list/ion-item[2]/div[1]/div/ion-label/ion-row/ion-col[5]/button/div[1]/div').click()
time.sleep(1)
#NILAGA 'VAT E"
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

driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstv')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-grid/ion-card[2]/ion-card-content/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input').send_keys('lstventures')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-auth-password/ion-content/div[2]/ion-card/form/ion-row/ion-col/button/span').click()
time.sleep(1)

#pay cash
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-order-preview/ion-content/div[2]/div/div[1]/div/ion-list[4]/div[1]/button/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-custom-alert/ion-footer/ion-row/a[2]').click()
time.sleep(1)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
press ('enter')
time.sleep(2)
obj = driver.switch_to.alert
time.sleep(1)
obj.accept()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button/span').click()
time.sleep(1)

#BACK TO HOME
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-orders/ion-header/ion-navbar/ion-buttons/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-popover/div/div[2]/div/popover/ion-list/button[2]/div[1]/div').click()
time.sleep(1)

#reports
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-home/ion-content/div[2]/ion-list/button[7]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-reports/ion-content/div[2]/ion-list/button[4]/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[2]/ion-row[1]/ion-col/ion-item/div[1]/div/ion-select/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/div/button[10]/span/div[2]').click()
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
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[1]/ion-card-content/ion-row/ion-col[2]/ion-item/ion-checkbox/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[3]/ion-row[2]/ion-col[2]/ion-item/ion-checkbox/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-content/div[2]/form/ion-grid/ion-card[3]/ion-row[2]/ion-col[1]/ion-item/ion-checkbox/button/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ion-app/ion-modal/div/page-report-option/ion-header/ion-navbar/div[2]/ion-title/div/button/span').click()
time.sleep(1)

#SAVE FILE
driver.maximize_window()
time.sleep(4)
press('p')
time.sleep(3)
press('enter') 
time.sleep(2)

#GROSS SALES
file = open("C:/Users/SERAN/Downloads/p.csv")
gs_value = (file.readlines())[26]
gs_val = gs_value[13:]
print(gs_val)

file = open("C:/Users/SERAN/Downloads/SCENARIO 5.csv")
gs_value1 = (file.readlines())[597]
gs_val2 = gs_value1[14:23]
gs_val3 = gs_val2.replace(",", "")
print(gs_val3)

if float(gs_val) == float(gs_val3):
    print("GROSS SALES VOID IN SCENARIO 5 MATCHED IN DAILY SALES REPORT")
    time.sleep(2)
else:
    print("GROSS SALES VOID IN SCENARIO 5 DO NOT MATCH IN DAILY SALES REPORT")
    time.sleep(2)

#LESS POST VOIID
file = open("C:/Users/SERAN/Downloads/p.csv")
value = (file.readlines())[9]
val = value[-2]
print(val)

file = open("C:/Users/SERAN/Downloads/SCENARIO 5.csv")
value1 = (file.readlines())[598]
val2 = value1[-3]
print(val2)

if int(val) == int(val2):
    print("LESS POST VOID IN SCENARIO 5 MATCHED IN DAILY SALES REPORT")
    time.sleep(2)
else:
    print("LESS POST VOID IN SCENARIO 5 DO NOT MATCH IN DAILY SALES REPORT")
    time.sleep(2)

#LESS DISCOUNTS
file = open("C:/Users/SERAN/Downloads/p.csv")
ld_value = (file.readlines())[10]
ld_val1 = ld_value[16:]
print(ld_val1)

file = open("C:/Users/SERAN/Downloads/SCENARIO 5.csv")
ld_value1 = (file.readlines())[599]
ld_val2 = ld_value1[15:18]
print(ld_val2)

if int(ld_val1) == int(ld_val2):
    print("LESS DISCOUNT IN SCENARIO 5 MATCHED IN DAILY SALES REPORT")
    time.sleep(2)
else:
    print("LESS DISCOUNT IN SCENARIO 5 DO NOT MATCH IN DAILY SALES REPORT")
    time.sleep(2)

#LESS SERVICE CHARGE
file = open("C:/Users/SERAN/Downloads/p.csv")
sc_value = (file.readlines())[11]
sc_val1 = sc_value[21:]
print(sc_val1)

file = open("C:/Users/SERAN/Downloads/SCENARIO 5.csv")
sc_value1 = (file.readlines())[600]
sc_val2 = sc_value1[21:27]
print(sc_val2)

if float(sc_val1) == float(sc_val2):
    print("LESS SERVICE CHARGE IN SCENARIO 5 MATCHED IN DAILY SALES REPORT")
    time.sleep(2)
else:
    print("LESS SERVICE CHARGE IN SCENARIO 5 DO NOT MATCH IN DAILY SALES REPORT")
    time.sleep(2)

#Less VAT Adj
file = open("C:/Users/SERAN/Downloads/p.csv")
vat_value = (file.readlines())[12]
vat_val1 = vat_value[14:]
print(vat_val1)

file = open("C:/Users/SERAN/Downloads/SCENARIO 5.csv")
vat_value1 = (file.readlines())[601]
vat_val2 = vat_value1[14:15]
print(vat_val2)

if int(vat_val1) == int(vat_val2):
    print("LESS VAT ADJ  IN SCENARIO 5 MATCHED IN DAILY SALES REPORT")
    time.sleep(2)
else:
    print("LESS VAT ADJ  IN SCENARIO 5 DO NOT MATCH IN DAILY SALES REPORT")
    time.sleep(2)


#TOTAL VAT SALES
file = open("C:/Users/SERAN/Downloads/p.csv")
tv_value = (file.readlines())[13]
tv_val1 = tv_value[17:]
print(tv_val1)

file = open("C:/Users/SERAN/Downloads/SCENARIO 5.csv")
tv_value1 = (file.readlines())[603]
tv_val2 = tv_value1[17:24]
print(tv_val2)

if float(tv_val1) == float(tv_val2):
    print("TOTAL VAT SALES  IN SCENARIO 5 MATCHED IN DAILY SALES REPORT")
    time.sleep(2)
else:
    print("TOTAL VAT SALES  IN SCENARIO 5 DO NOT MATCH IN DAILY SALES REPORT")
    time.sleep(2)

#Total NO. of Transaction
file = open("C:/Users/SERAN/Downloads/p.csv")
tn_value = (file.readlines())[15]
tn_val1 = tn_value[26:]
print(tn_val1)

file = open("C:/Users/SERAN/Downloads/SCENARIO 5.csv")
tn_value1 = (file.readlines())[606]
tn_val2 = tn_value1[24:26]
print(tn_val2)

if float(tn_val1) == float(tn_val2):
    print("TOTAL NUMBER OF TRANSACTIONS  IN SCENARIO 5 MATCHED IN DAILY SALES REPORT")
    time.sleep(2)
else:
    print("TOTAL NUMBER OF TRANSACTIONS  IN SCENARIO 5 DO NOT MATCH IN DAILY SALES REPORT")
    time.sleep(2)

#Total # of PAX
file = open("C:/Users/SERAN/Downloads/p.csv")
pax_value = (file.readlines())[16]
pax_val1 = pax_value[18:]
print(pax_val1)

file = open("C:/Users/SERAN/Downloads/SCENARIO 5.csv")
pax_value1 = (file.readlines())[607]
pax_val2 = pax_value1[16:18]
print(pax_val2)

if float(pax_val1) == float(pax_val2):
    print("TOTAL NUMBER OF PAX  IN SCENARIO 5 MATCHED IN DAILY SALES REPORT")
    time.sleep(2)
else:
    print("TOTAL NUMBER OF PAX  IN SCENARIO 5 DO NOT MATCH IN DAILY SALES REPORT")
    time.sleep(2)

#Total # of Quantity
file = open("C:/Users/SERAN/Downloads/p.csv")
tq_value = (file.readlines())[17]
tq_val1 = tq_value[11:]
print(tq_val1)

file = open("C:/Users/SERAN/Downloads/SCENARIO 5.csv")
tq_value1 = (file.readlines())[608]
tq_val2 = tq_value1[16:18]
print(tq_val2)

if float(tq_val1) == float(tq_val2):
    print("TOTAL NUMBER OF PAX  IN SCENARIO 5 MATCHED IN DAILY SALES REPORT")
    time.sleep(2)
else:
    print("TOTAL NUMBER OF PAX  IN SCENARIO 5 DO NOT MATCH IN DAILY SALES REPORT")
    time.sleep(2)











