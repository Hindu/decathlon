#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By

import time, unittest 
import config
import sys 

def popup_close(browser):
    WDW(browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "popup-footer")))
    browser.find_element_by_xpath('//*[@id="window-1"]/div/a[1]').click()

def wait_for(me, browser):
    try:
        if me[0] == '.':
            return WDW(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, me[1:])))
        elif me[0] == '#':
            return WDW(browser, 10).until(EC.element_to_be_clickable((By.ID, me[1:])))
        elif me[0] == '/':
            return WDW(browser, 10).until(EC.element_to_be_clickable((By.XPATH, me)))
        else:
            print "We got someting different from classes and ids!"
    except:
        print 'Unexpected error:',  sys.exc_info()[0], sys.exc_traceback.tb_lineno
        print "On this page: " + browser.current_url + " we didn't find the me element!"

def registration(type, browser):
    if type == 'no-registration':
        case_1 = browser.find_element_by_id('cb_noregister').click()
        next_button_1 = browser.find_element_by_css_selector('#cb_noregister_h > .next').click()
    elif type == 'social':
	    return True #TODO 'To fix it in the next version'
    elif type == 'authorisation':
	    wait_for('#NEW_LOGIN', browser).send_keys(config.stager_login)
	    wait_for('#USER_PASSWORD', browser).send_keys(config.stager_password)
	    browser.find_element_by_xpath('//*[@id="cb_auth_h"]/form/fieldset[3]/input').click()
    elif type == 'cb_register':
	    return True #TODO 'We will this catch a capcha one day '