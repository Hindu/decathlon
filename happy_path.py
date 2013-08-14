#coding=utf-8
import ConfigParser
import codecs
from selenium import webdriver
from selenium.webdriver.support.ui import Select


import sys
sys.path.append( 'lib' )
import unittest, smlibrary, time

class Sportmaster(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

        self.appConfig = ConfigParser.RawConfigParser(allow_no_value=True)
        self.appConfig.readfp(codecs.open("app.cfg", "r", "utf8"))

        self.testConfig = ConfigParser.RawConfigParser(allow_no_value=True)
        self.testConfig.readfp(codecs.open("test.cfg", "r", "utf8"))

    #he is a newbie on our site who wants to buy some stuff without registration, with delivery to his address
    def test_oddity_1(self):
        browser = self.browser
        appConfig = self.appConfig
        testConfig = self.testConfig
        try:                    
            # First let's buy a nice <skateboard>
            # Let's open a page with <skateboards>
            self.redirect(appConfig.get("host", "name") + '/catalog/sport/roliki_skeytbordy_samokaty/skeytbordy/')
            smlibrary.popup_close(browser) 

            # Let's take the third in the row
            browser.find_elements_by_css_selector('.picture > a')[2].click()

            # Let's put the nice <skateboard> in the basket
            smlibrary.wait_for('#buyLink2', browser).click()
            # We would like to continue shopping
            smlibrary.wait_for('.bb_continue', browser).click()

            #url = 'www.dev.datalinecentre.ru/catalog/sportivnaya_odezhda/aksessuary/ryukzaki/1199237/' # it will fail

            #second let's find lovely <swim glasses>
            self.redirect(appConfig.get("host", "name") + '/catalog/sport/plavanie/ochki_dlya_plavaniya/1192250/')

            #We would like to buy everything
            smlibrary.wait_for('#buyLink2', browser).click()
            #We would like to make an order
            smlibrary.wait_for('.bb_makeorder', browser).click()
            # Let's pass our basket page as fast as we can
            smlibrary.wait_for('#basketOrderButton2', browser).click()

            # Let's take the first case of our registration form: "Купить без регистрации"
            smlibrary.registration('no-registration', browser)

            # Let's fill a Contact-Delivery page with some cyrillic!
            smlibrary.wait_for('#ORDER_PROP_5', browser).send_keys(testConfig.get('test1', 'name_guy'))
            smlibrary.wait_for('#ORDER_PROP_14', browser).send_keys(testConfig.get('test1', 'phone_number_guy'))
            smlibrary.wait_for('#ORDER_PROP_4', browser).send_keys(testConfig.get('test1', 'email_guy'))
            
            delivery_city = browser.find_element_by_id('ORDER_PROP_162')
            select = Select(delivery_city)
            select.select_by_visible_text('Москва')
            time.sleep(1)
            smlibrary.wait_for('#ORDER_PROP_164', browser).send_keys(u'Кочновский проезд')
            smlibrary.wait_for('#ORDER_PROP_165', browser).send_keys('4')

            # We have an elevator in our building
            smlibrary.wait_for('#ORDER_PROP_173', browser).click()
            # Let's agree with a delivery policy
            smlibrary.wait_for('#ORDER_PROP_214', browser).click()

            smlibrary.wait_for('#contButton', browser).click()
            smlibrary.wait_for('#contButton', browser).click()

            # We should wait for a KIS response
            time.sleep(6)

            # Do you think that the process of purchasing is a bit overextended, don't you?
            browser.find_elements_by_class_name('strangebutton')[0].click()
            # We are celebrating that we have made the order!
            time.sleep(10)

            # We are happy to make a happy screenshot
            happyscreenshot = 'screenshots/robots/case_1/monkeys_vs_robots' + time.strftime("%Y-%m-%d_%H-%M-%S") + '.png'
            browser.get_screenshot_as_file(happyscreenshot)         
            print "Well done, my dear. Now you are the owner of something which we could find cheaper in the Decatlon! " \
                  "We have made a screenshot for you: " + happyscreenshot

        except:
            print 'Unexpected error:',    sys.exc_info()[0], sys.exc_traceback.tb_lineno
            screenshot = 'screenshots/errors/case_1/monkeys_vs_robots' + time.strftime("%Y-%m-%d_%H-%M-%S") + '.png'
            browser.get_screenshot_as_file(screenshot)         
            print "Don't worry, we made a screenshot for you! Look at " + screenshot

    #it is any legal entity who wants to buy some items with registration, without delivery
    def test_oddity_2(self):
        browser = self.browser
        appConfig = self.appConfig
        testConfig = self.testConfig
        try:                    
            # First let's buy a cool ball
            self.redirect(appConfig.get("host", "name") + '/catalog/sport/basketbol/myachi/')
            smlibrary.popup_close(browser) 

            # Let's take the second in the row
            browser.find_elements_by_css_selector('.picture > a')[2].click()

            #Let's put the nice ball in the basket
            smlibrary.wait_for('#buyLink2', browser).click()
            #We would like to make an order
            smlibrary.wait_for('.bb_makeorder', browser).click()
            # Let's pass our basket page as fast as we can
            smlibrary.wait_for('#basketOrderButton2', browser).click()

            # Let's take the thrid case of our registration form: "Вы уже зарегистрированы"
            smlibrary.registration('authorisation', browser)
            
            # Are you a 'Юридическое лицо', aren't you?
            person = smlibrary.wait_for('#PERSON_TYPE', browser) 
            select = Select(person)
            select.select_by_visible_text(u'Юридическое лицо')

            #we are looking for a new updating page
            browser.refresh()

            # We are filling the number field
            smlibrary.wait_for('//*[@id="ORDER_PROP_9"]', browser).send_keys(testConfig.get('test2', 'phone_number_guy'))
            
            # We are located in Абакан city
            delivery_city = browser.find_element_by_id('ORDER_PROP_179') 
            select = Select(delivery_city)
            select.select_by_visible_text('Абакан')

            # Let's pick our item up in the nearest shop in Абакан city
            browser.find_elements_by_css_selector('.megatabs1 > li')[1].click()
            time.sleep(5)
            browser.find_elements_by_css_selector('.ps_address')[0].click() # The first availible address

            # Cuddle Bug Inc an Russian based local cosy manufacturing firm that focuses on producing
            # the best bike shelves in Moscow region
            # and solving some test issues with Selenium.
            smlibrary.wait_for('//*[@id="ORDER_PROP_8"]', browser).send_keys(testConfig.get('company', 'name'))
            # Let's agree with a delivery policy
            smlibrary.wait_for('#ORDER_PROP_215', browser).click()

            smlibrary.wait_for('#contButton', browser).click()

            # We should wait for a KIS response
            time.sleep(6)

            browser.find_elements_by_class_name('strangebutton')[0].click()

            # We are celebrating that we have made the order!
            time.sleep(10)

            happyscreenshot = 'screenshots/robots/case_2/monkeys_vs_robots' + time.strftime("%Y-%m-%d_%H-%M-%S") + '.png' # We are happy to make a happy screenshot
            browser.get_screenshot_as_file(happyscreenshot)         
            print "Well done, my dear. Now you are the owner of something which we can find cheaper in the Decatlon! We have made a screenshot for you: " + happyscreenshot
            
        except:
            print 'Unexpected error:',    sys.exc_info()[0], sys.exc_traceback.tb_lineno # print error and line number
            screenshot = 'screenshots/errors/case_2/monkeys_vs_robots' + time.strftime("%Y-%m-%d_%H-%M-%S") + '.png'
            browser.get_screenshot_as_file(screenshot)         
            print "Don't worry, we made a screenshot for you! Look at " + screenshot

    
    def tearDown(self):
        self.browser.close()

    def redirect(self, url):
        self.browser.get('http://' + self.appConfig.get("usr", "login") + ':' + self.appConfig.get("usr", "password") + '@' + url)
        
if __name__== "__main__":
    unittest.main()