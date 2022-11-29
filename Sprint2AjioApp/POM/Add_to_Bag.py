import time
import pytest
from selenium import webdriver
from Data_ajio import reading_obj
# lo_obj = reading_obj.read_locators()
from Library.config import Config
from Data_ajio.reading_obj import ReadExcel
obj_1 = ReadExcel()
lo_obj = obj_1.read_locators(Config.Locator_sheet)
class Ajio:
    # obj_1 = ReadExcel()
    # lo_obj = obj_1.read_locators(Config.Locator_sheet)
    #
    def __init__(self,driver):
        self.driver=driver
    # def select_signin_button(self):
    #
    #     # locator = self.lo_obj['signIn_button']
    #     # self.driver.find_element(*locator).click
    #
    #
    #     self.driver.find_element(*lo_obj["signIn_button"]).click()
    #     time.sleep(2)
    # def enter_number(self,number):
    #     time.sleep(2)
    #     self.driver.find_element(*lo_obj['txt_number']).send_keys(number)
    #     time.sleep(5)
    #     self.driver.find_element(*lo_obj['continue_button']).click()
    #     time.sleep(30)
    #     self.driver.find_element(*lo_obj['start_button']).click()
    #     time.sleep(10)
    def search(self,element):
        # self.driver.find_element(*lo_obj['search_bar']).click()
        # time.sleep(2)
        time.sleep(2)
        self.driver.find_element(*lo_obj['search_bar']).send_keys(element)
        time.sleep(2)
        self.driver.find_element(*lo_obj['search_button']).click()
        time.sleep(2)
    def product(self):
            self.driver.find_element(*lo_obj['product_click']).click()
            time.sleep(2)

    def size_select(self,size):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.execute_script("window.scrollBy(0,300)", "")
        buttons=self.driver.find_elements(*lo_obj['size_select'])
        # print(len(buttons))
        for i in range(len(buttons)):
            time.sleep(2)
            if buttons[i].is_enabled() and buttons[i].text == size:
                buttons[i].click()
                break
        else:
            self.driver.quit()
            print('size is unavailable')
            time.sleep(2)


    def add_to_bag(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.driver.find_element(*lo_obj['add_to_bag_button']).click()
        time.sleep(2)
    def go_to_bag(self):
        # self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        self.driver.find_element(*lo_obj['go_to_bag_button']).click()
        time.sleep(2)
    def proceed_shopping(self):

        self.driver.find_element(*lo_obj['proceed_shopping']).click()
        time.sleep(2)

