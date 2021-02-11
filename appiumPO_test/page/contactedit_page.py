# 添加成员信息
from appium.webdriver.common.mobileby import MobileBy
from appiumPO_test.page.base_page import BasePage


class ContactEditPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def edit_name(self, name):
        # self.driver.find_element_by_xpath\
        #     ("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys("eric")
        name_element = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
        self.find(name_element).send_keys(name)
        return self

    # def edit_gender(self):
    #     return self
    # 测试的企业微信版本只有姓名和电话输入框

    def edit_phone(self, phone):
        # self.driver.find_element_by_id("com.tencent.wework:id/fwi").send_keys("13088888888")
        self.find((MobileBy.ID, "com.tencent.wework:id/fwi")).send_keys(phone)

        return self

    def click_save(self):
        # self.driver.find_element_by_id("com.tencent.wework:id/aj_").click()
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/aj_"))
        from appiumPO_test.page.memberinvite_page import MemberInvitePage
        return MemberInvitePage(self.driver)
