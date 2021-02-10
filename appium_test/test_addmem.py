from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_addmem(self):
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys("Tom")
        # 测试的企业微信版本没有性别选项
        self.driver.find_element_by_id("com.tencent.wework:id/fwi").send_keys("18888888888")
        self.driver.find_element_by_id("com.tencent.wework:id/aj_").click()
        mytoast = self.driver.find_element_by_xpath("//*[@text='添加成功']").text
        mytoast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        assert "添加成功" == mytoast
