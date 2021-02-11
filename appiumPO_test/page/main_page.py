# 首页-点击通讯录
from appium.webdriver.common.mobileby import MobileBy

from appiumPO_test.page.addresslist_page import AddressListPage
from appiumPO_test.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def click_addresslist(self):
        # self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        self.find(self.addresslist_element).click()
        return AddressListPage(self.driver)
