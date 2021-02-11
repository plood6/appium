from appium import webdriver
from appiumPO_test.page.base_page import BasePage
from appiumPO_test.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "wework"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(15)
        else:
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
