from appiumPO_test.page.base_page import BasePage
from appiumPO_test.page.memberinvite_page import MemberInvitePage


class AddressListPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def add_member(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("添加成员").instance(0));').click()
        self.find_by_scroll_and_click("添加成员")
        return MemberInvitePage(self.driver)
