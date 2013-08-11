#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import sys
sys.path.append( 'lib' )
import unittest, smlibrary, time, httplib, urllib2
import config

class Sportmaster(unittest.TestCase):
  
  def setUp(self):
    self.browser = webdriver.Chrome('/home/vaka/Downloads/chromedriver')    
  def test_oddity_1(self): #he is a newbie on our site who wants to buy some stuff without registration, with delivery to his address 
    browser = self.browser
    try:          
    # First let's buy a nice <skateboard>
      url = 'etalonsm.datalinecentre.ru/catalog/sport/roliki_skeytbordy_samokaty/skeytbordy/'
      browser.get('http://' + config.login + ':' + config.password + '@' + url) # Let's open a page with <skateboards>
      smlibrary.popup_close(browser) 

      browser.find_elements_by_css_selector('.picture > a')[2].click() # Let's take the third in the row

      smlibrary.wait_for('#buyLink2', browser).click() # Let's put the nice <skateboard> in the basket 

      smlibrary.wait_for('.bb_continue', browser).click() # We would like to continue shopping

      #url = 'www.dev.datalinecentre.ru/catalog/sportivnaya_odezhda/aksessuary/ryukzaki/1199237/' # it will fail
      url = 'etalonsm.datalinecentre.ru/catalog/sport/plavanie/ochki_dlya_plavaniya/1192250/' #second let's find lovely <swim glasses>
      browser.get('http://' + config.login + ':' + config.password + '@' + url)
      
      smlibrary.wait_for('#buyLink2', browser).click() #We would like to buy everything  
      smlibrary.wait_for('.bb_makeorder', browser).click() #We would like to make an order
      smlibrary.wait_for('#basketOrderButton2', browser).click() # Let's pass our basket page as fast as we can

      smlibrary.registration('no-registration', browser) # Let's take the first case of our registration form: "Купить без регистрации"

      # Let's fill a Contact-Delivery page with some cyrillic!
      smlibrary.wait_for('#ORDER_PROP_5', browser).send_keys(config.name_guy_1)
      smlibrary.wait_for('#ORDER_PROP_14', browser).send_keys(config.phone_number_guy_1)
      smlibrary.wait_for('#ORDER_PROP_4', browser).send_keys(config.email_guy_1)
      
      delivery_city = browser.find_element_by_id('ORDER_PROP_162')
      select = Select(delivery_city)
      select.select_by_visible_text('Москва')
      time.sleep(1)
      smlibrary.wait_for('#ORDER_PROP_164', browser).send_keys(u'Кочновский проезд')
      smlibrary.wait_for('#ORDER_PROP_165', browser).send_keys('4')

      smlibrary.wait_for('#ORDER_PROP_173', browser).click() # We have an elevator in our building
      smlibrary.wait_for('#ORDER_PROP_214', browser).click() # Let's agree with a delivery policy

      smlibrary.wait_for('#contButton', browser).click() # Some clicky clicks 
      smlibrary.wait_for('#contButton', browser).click() # Some clicky clicks
      time.sleep(6) # We should wait for a KIS response
      browser.find_elements_by_class_name('strangebutton')[0].click() # Do you think that the process of purchasing is a bit overextended, don't you?
      time.sleep(10) # We are celebrating that we have made the order!

      happyscreenshot = 'screenshots/robots/case_1/monkeys_vs_robots' + time.strftime("%Y-%m-%d_%H-%M-%S") + '.png' # We are happy to make a happy screenshot
      browser.get_screenshot_as_file(happyscreenshot)     
      print "Well done, my dear. Now you are the owner of something which we could find cheaper in the Decatlon! We have made a screenshot for you: " + happyscreenshot
      
    except: # if something went wrong    
      
      print 'Unexpected error:',  sys.exc_info()[0], sys.exc_traceback.tb_lineno # print error and line number
      screenshot = 'screenshots/errors/case_1/monkeys_vs_robots' + time.strftime("%Y-%m-%d_%H-%M-%S") + '.png'
      browser.get_screenshot_as_file(screenshot)     
      print "Don't worry, we made a screenshot for you! Look at " + screenshot
    
  def test_oddity_2(self):#it is any legal entity who wants to buy some items with registration, without delivery
    browser = self.browser
    try:          
    # First let's buy a cool ball
      url = 'etalonsm.datalinecentre.ru/catalog/sport/basketbol/myachi/'
      browser.get('http://' + config.login + ':' + config.password + '@' + url)
      smlibrary.popup_close(browser) 

      browser.find_elements_by_css_selector('.picture > a')[2].click()# Let's take the second in the row

      smlibrary.wait_for('#buyLink2', browser).click() #Let's put the nice ball in the basket 
      smlibrary.wait_for('.bb_makeorder', browser).click() #We would like to make an order
      smlibrary.wait_for('#basketOrderButton2', browser).click() # Let's pass our basket page as fast as we can

      smlibrary.registration('authorisation', browser) # Let's take the thrid case of our registration form: "Вы уже зарегистрированы"
      
      # Are you a 'Юридическое лицо', aren't you?
      person = smlibrary.wait_for('#PERSON_TYPE', browser) 
      select = Select(person)
      select.select_by_visible_text(u'Юридическое лицо')
           
      browser.refresh() #we are looking for a new updating page
      
      smlibrary.wait_for('//*[@id="ORDER_PROP_9"]', browser).send_keys(config.phone_number_guy_2) # We are filling the number field
      
      # We are located in Абакан city
      delivery_city = browser.find_element_by_id('ORDER_PROP_179') 
      select = Select(delivery_city)
      select.select_by_visible_text('Абакан')

      browser.find_elements_by_css_selector('.megatabs1 > li')[1].click() # Let's pick our item up in the nearest shop in Абакан city
      time.sleep(5)
      browser.find_elements_by_css_selector('.ps_address')[0].click() # The first availible address

      smlibrary.wait_for('//*[@id="ORDER_PROP_8"]', browser).send_keys(config.company_name) # Cuddle Bug Inc an Russian based local cosy manufacturing firm that focuses on producing the best bike shelves in Moscow region and solving some test issues with Selenium.
      smlibrary.wait_for('#ORDER_PROP_215', browser).click() # Let's agree with a delivery policy

      smlibrary.wait_for('#contButton', browser).click() # Some clicky clicks
      time.sleep(6) # We should wait for a KIS response

      browser.find_elements_by_class_name('strangebutton')[0].click() 
      time.sleep(10) # We are celebrating that we have made the order!

      happyscreenshot = 'screenshots/robots/case_2/monkeys_vs_robots' + time.strftime("%Y-%m-%d_%H-%M-%S") + '.png' # We are happy to make a happy screenshot
      browser.get_screenshot_as_file(happyscreenshot)     
      print "Well done, my dear. Now you are the owner of something which we can find cheaper in the Decatlon! We have made a screenshot for you: " + happyscreenshot
      
    except: # if something went wrong      
      
      print 'Unexpected error:',  sys.exc_info()[0], sys.exc_traceback.tb_lineno # print error and line number
      screenshot = 'screenshots/errors/case_2/monkeys_vs_robots' + time.strftime("%Y-%m-%d_%H-%M-%S") + '.png'
      browser.get_screenshot_as_file(screenshot)     
      print "Don't worry, we made a screenshot for you! Look at " + screenshot

  
  def tearDown(self):
    self.browser.close()
    
if __name__== "__main__":
  unittest.main()