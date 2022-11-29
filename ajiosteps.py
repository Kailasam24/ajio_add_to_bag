import time
from behave import *
from selenium import webdriver
@given('I launch browser')
def launch_browser(context):
    # context.driver.get(r'C:\Users\91996\Downloads\chromedriver_win32\chromedriver.exe')
    opt = webdriver.ChromeOptions()
    opt.add_argument("--disable-notifications")
    context.driver=webdriver.Chrome(options=opt)
    context.driver.implicitly_wait(30)

@when('I open ajio')
def open_ajio(context):
    context.driver.get("https://ajio.com/")
    context.driver.maximize_window()
    time.sleep(2)

@when('click on sign in')
def sign_in(context):
    time.sleep(2)
    context.driver.find_element("xpath", "//span[text()='Sign In / Join AJIO']").click()


@when(u'Enter valid number and OTP')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@name='username']").send_keys("9966250321")
    context.driver.find_element("xpath","//input[@class='login-btn']").click()


@when('click on login')
def log_in(context):
    time.sleep(30)
    context.driver.find_element("xpath", "//input[@class='login-form-inputs login-btn']").click()


@when('click on search page and enter "{element}"')
def search_element(context,element):
    time.sleep(10)
    context.driver.find_element_by_name("searchVal").send_keys(element)


@when('search element click and navigated')
def search_click(context):
    time.sleep(5)
    context.driver.find_element("xpath","//button[@class='rilrtl-button']").click()


@when('click on product and navigated')
def product(context):
    time.sleep(2)
    context.driver.find_element("xpath", "//div[@class='imgHolder']").click()
    context.driver.switch_to.window(context.driver.window_handles[1])

@when('click on "{size}"')
def select_size(context,size):
    time.sleep(2)
    context.driver.execute_script("window.scrollBy(0,400)", "")
    buttons = context.driver.find_elements("xpath", "//div[@class='size-swatch']")
    for i in range(len(buttons)):
        time.sleep(2)
        if buttons[i].is_enabled() and buttons[i].text==size:
            time.sleep(2)
            buttons[i].click()
            break



@when('click on add to bag')
def add_to_bag(context):

    time.sleep(2)
    context.driver.find_element("xpath","//div[@class='btn-gold']").click()

@when('click on go to bag and navigated')
def nav_bag(context):
    time.sleep(10)
    context.driver.find_element("xpath", "//span[text()='GO TO BAG']").click()


@when('click on proceed to shopping')
def proceed(context):
    time.sleep(2)
    context.driver.find_element("xpath", "//button[text()='Proceed to shipping']").click()



# from behave import *
# from selenium import webdriver
# import time
# @given('I launch browser')
# def lauch_browser(context):
#     # raise NotImplementedError(u'STEP: Given I launch browser')
#     opt = webdriver.ChromeOptions()
#     opt.add_argument("--disable-notifications")
#     # driver = webdriver.Chrome(.Edge_Driver_path)
#     context.driver = webdriver.Chrome(options=opt)
#     context.driver.implicitly_wait(50)
#
# @when('I open ajio')
# def open_ajio(context):
#     # raise NotImplementedError(u'STEP: When I open ajio')
#     context.driver.get("https://ajio.com/")
#     context.driver.maximize_window()
# #
#
# @when('click on sign in')
# def sign_in(context):
#     # raise NotImplementedError(u'STEP: When click on sign in')
#     context.driver.find_element("xpath", "//span[text()='Sign In / Join AJIO']").click()
#
# @when('Enter valid number and OTP')
# def enter_num(context):
#     # raise NotImplementedError(u'STEP: When Enter valid number and OTP')
#     context.driver.find_element("xpath", "//input[@name='username']").send_keys("9966250321")
#
#     context.driver.find_element("xpath","//input[@class='login-btn']").click()
#
# @when('click on login')
# def log_in(context):
#     # raise NotImplementedError(u'STEP: When click on login')
#     time.sleep(20)
#     context.driver.find_element("xpath", "//input[@class='login-form-inputs login-btn']").click()
#
#
# @when('click on search page and enter "{element}"')
# def step_impl(context,element):
#     # raise NotImplementedError(u'STEP: When click on search page and enter "kurti"')
#     context.driver.find_element_by_name("searchVal").send_keys(element)
#     time.sleep(2)
#     context.driver.find_element("xpath", "//button[@class='rilrtl-button']").click()
#     context.driver.switch_to.window(context.driver.window_handles[1])
# # @when('search element click and navigated')
# # def search_click(context):
# #     time.sleep(5)
# #     context.driver.find_element("xpath","//button[@class='rilrtl-button']").click()
#
# @when('click on product and navigated')
# def product(context):
#     time.sleep(2)
#     context.driver.find_element("xpath", "//div[@class='imgHolder']").click()
#     time.sleep(2)
#     context.driver.switch_to.window(context.driver.window_handles[1])
# #
# @when('click on "{size}"')
# def select_size(context,size):
#     time.sleep(2)
#     context.driver.execute_script("window.scrollBy(0,400)", "")
#     buttons = context.driver.find_elements("xpath", "//div[@class='size-swatch']")
#     for i in range(len(buttons)):
#         time.sleep(2)
#         if buttons[i].is_enabled() and buttons[i].text== size:
#             time.sleep(2)
#             buttons[i].click()
#             break
# #
#
#
# @when('click on add to bag')
# def add_to_bag(context):
#     # raise NotImplementedError(u'STEP: When click on add to bag')
#     time.sleep(2)
#     context.driver.find_element("xpath","//div[@class='btn-gold']").click()
#     #
#
# @when('click on go to bag and navigated')
# def nav_bag(context):
#     # raise NotImplementedError(u'STEP: When click on go to bag and navigated')
#     time.sleep(2)
#     context.driver.find_element("xpath", "//span[text()='GO TO BAG']").click()
#     #
#
# @when('click on proceed to shopping')
# def proceed(context):
#     time.sleep(2)
#     context.driver.find_element("xpath", "//button[text()='Proceed to shipping']").click()
#
#
#
