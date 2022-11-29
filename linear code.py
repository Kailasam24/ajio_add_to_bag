from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
file_path=r'C:\Users\91996\Downloads\chromedriver_win32\chromedriver.exe'
# file_path=r'C:\Users\91996\Downloads\edgedriver_win32\msedgedriver.exe'
# file_path=r"C:\Users\91996\Downloads\geckodriver-v0.32.0-win-aarch64\geckodriver.exe"
opt=webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
driver=webdriver.Chrome(executable_path=file_path,options=opt)
driver.implicitly_wait(30)
driver.get('https://www.ajio.com/')
driver.maximize_window()
titles=driver.get('https://www.ajio.com/')
print()
# sign up
# driver.find_element("xpath","//span[text()='Sign In / Join AJIO']").click()
# # driver.find_element("xpath","//input[@name='username']").send_keys("9966250321")
# # driver.find_element("xpath","//input[@class='login-btn']").click()
# # time.sleep(30)
# # driver.find_element("xpath","//input[@class='login-form-inputs login-btn']").click()
# # ##search
driver.find_element_by_name("searchVal").send_keys("heelsgfdsag543")
driver.find_element_by_name("searchVal").send_keys(Keys.ENTER)
time.sleep(2)
sorry=driver.find_element("xpath","//div[@class='no-search-result']//div").text
time.sleep(2)
if sorry=="Sorry! We couldn't find any matching items for":
    driver.quit()
    print("test case failed")
else:

    driver.find_element("xpath","//div[@class='imgHolder']").click()
    # #window handles
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    # color=driver.find_element("xpath","//p[@class='prod-color']")
    # if color=='Khaki':
    #     color.click()
    # else:
    #     pass


    ####size selection
    size='7'
    buttons=driver.find_elements("xpath","//div[@class='size-variant-block']//div")
    for i in range(0,len(buttons)):
        if buttons[i].is_enabled() and buttons[i].text==size:
            time.sleep(2)
            buttons[i].click()
            break
    else:
        driver.quit()
        print('size not available')
        ## size is unavailabl
    driver.execute_script("window.scrollBy(0,400)","")
    driver.find_element("xpath","//div[@class='btn-gold']").click()
        # driver.find_element("xpath","//span[text()='Please select a size']")
    time.sleep(5)
    driver.find_element("xpath","//span[text()='GO TO BAG']").click()
    time.sleep(2)
    driver.find_element("xpath","//button[text()='Proceed to shipping']").click()
    # driver.quit()
    # # #
    #
    # # #
    # # # # def test_ajio_1(self):
    # # # #     bag = Ajio()
    # # # #     bag.select_signin_button()
    # # # #     bag.enter_number("9966250321")
    # # # #     bag.search("short")
    # # # #     bag.product()
    # # # #     bag.color_select("blue")
    # # # #     bag.size_select("M")
    # # # #     bag.go_to_bag()
    # # # #     bag.add_to_bag()
    # # # #     bag.proceed_shopping()
    # #
    # #
    # #
    # #
    #     # def color_select(self, color):
    #     #     colors = self.driver.find_elements(*lo_obj['color_select_click']).text
    #     #     try:
    #     #         for i in range(len(colors)):
    #     #             time.sleep(2)
    #     #             if colors[i].text==color:
    #     #                 colors[i].click()
    #     #                 time.sleep(2)
    #     #                 break
    #     #         else:
    #     #             pass
    # #
    # #
    # #
