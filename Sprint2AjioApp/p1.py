from selenium import webdriver
from LIBRARY.config import Config
from DATA.reading_objects import ReadExcel
import re
import time
import pytest

# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument("--disable-notification")
#
from selenium import webdriver
from LIBRARY.config import Config
from DATA.reading_objects import ReadExcel
import re
import time
import pytest

# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument("--disable-notification")
#
# chrome_option.add_argument("--disable-infobars")
#
# chrome_option.add_argument("start-maximized")
#
# chrome_option.add_argument("--disable-extensions")
#
# chrome_option.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications": 2})
#
# chrome_option.add_argument("use-fake-ui-for-media-stream")
# time.sleep(3)

class  Notification:
    obj_1=ReadExcel()
    locator_n=obj_1.read_locator(Config.notification_sheet)



    def _init_(self,driver):
        self.driver=driver
    def enter_email(self,email):
         locator=self.locator_n["fb_email"]
         self.driver.find_element(*locator).send_keys(email)

    def enter_pwd(self,password):
        locator=self.locator_n["fb_password"]
        self.driver.find_element(*locator).send_keys(password)
    def click_login(self):
        locator=self.locator_n["fb_login"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    # def icon_display(self):
    #     locator = self.locator_n["fb_notification icon"]
    #     self.driver.find_element(*locator)

    def icon_click(self):
         locator = self.locator_n["fb_notification icon_click"]
         self.driver.find_element(*locator).click()
         time.sleep(2)

    def click_seeall_option(self):
        locator = self.locator_n["notification_see all"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def all_option_click(self):
        locator = self.locator_n["all_option"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def unread(self):
        locator = self.locator_n["unread"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    # def like_img(self):
    #     locator = self.locator_n["like_img"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(2)
    #
    # def comment_img(self):
    #     locator = self.locator_n["comment"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(2)
    #
    # def display_time(self):
    #         locator = self.locator_n["display_time"]
    #         self.driver.find_element(*locator).display()
    #         time.sleep(2)

# fn=Notification()
# fn.enter_email()
# fn.enter_pwd()
# fn.click_login()
# fn.icon_display()
# fn.icon_click()
# fn.click_seeall_option()
# fn.all_option_click()
#fn.unread()
# fn.like_img()
# fn.comment_img()
# fn.display_time()