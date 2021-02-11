# 点击手动输入添加
from appium.webdriver.common.mobileby import MobileBy

from appiumPO_test.page.base_page import BasePage
from appiumPO_test.page.contactedit_page import ContactEditPage


class MemberInvitePage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    addmember_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    def addconect_manual(self):
        # self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.find_and_click(self.addmember_element)
        return ContactEditPage(self.driver)

    def get_toast(self):
        # mytoast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        toast_element = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        mytoast = self.find_and_get_text(toast_element)
        return mytoast
