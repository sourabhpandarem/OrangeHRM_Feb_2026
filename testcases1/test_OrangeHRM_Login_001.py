import time

import allure

# import time
# import sys
# sys.path.append("os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))")


import pytest

from Utilities.logger import Logger_class
from Utilities.readconfig import ReadConfig
from pageObjects.Loginpage import Login_page_class



@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_001:
    driver = None
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    login_url = ReadConfig.get_login_url()
    logger = Logger_class.get_loggen()

    @allure.title("Verify OrangeHRM Login Page URL")
    @allure.description("This test verifies the URL of the OrangeHRM login page.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("Navigate to OrangeHRM Login Page")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", name="OrangeHRM Login Page")
    @allure.issue("https://github.com/allure-framework/allure-python/issues/123", name="Issue 123")
    @allure.testcase("https://github.com/allure-framework/allure-python/issues/123", name="Test Case 123")
    @allure.feature("OrangeHRM Login")
    @allure.story("Verify Login Page URL")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_verify_url_001(self):
        self.logger.info("Verify OrangeHRM Login Page URL")
        self.driver.get(self.login_url)
      #  sel.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  (when we use config file that time we remove this part )

        if self.driver.title == "OrangeHRM":
            self.logger.info("OrangeHRM Login Page URL Verified")
            self.driver.save_screenshot("screenshots\\test_verify_url_pass.png")
            self.logger.info("Screenshot taken saved successfully")
            allure.attach.file("screenshots\\test_verify_url_pass.png", name="test_verify_url_pass", attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.logger.error("OrangeHRM Login Page URL Not Verified")
            self.logger.info("OrangeHRM Login Page URL Not Verified")
            self.driver.save_screenshot("screenshots\\test_verify_url_fail.png")
            allure.attach.file("screenshots\\test_verify_url_fail.png", name="test_verify_url_fail", attachment_type=allure.attachment_type.PNG)
            assert False
        self.logger.info("test_verify_url_001 is passed ,completed")
        self.logger.info("===OrangeHRM Login Test Completed===")


    @allure.title("Verify OrangeHRM Login")
    @allure.description("This test verifies the login functionality of the OrangeHRM application.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("Enter Username and Password")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", name="OrangeHRM Login Page")
    @allure.issue("https://github.com/allure-framework/allure-python/issues/123", name="Issue 123")
    @allure.testcase("https://github.com/allure-framework/allure-python/issues/123", name="Test Case 123")
    @allure.step("Click Login Button")
    @allure.feature("OrangeHRM Login")
    @allure.story("Verify Login Functionality")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_OrangeHRM_Login_002(self):
        self.logger.info("Verify OrangeHRM Login")
        self.driver.get(self.login_url)
        #self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        lp = Login_page_class(self.driver)
        lp.Enter_Username(self.username)
        lp.Enter_Password(self.password)
        lp.Click_Login()

        if lp.verify_login() == "Login Successful":
            self.logger.info("Login Successful")
            self.driver.save_screenshot("screenshots\\test_OrangeHRM_Login_002_pass.png")
            self.logger.info("Screenshot taken saved successfully")
            allure.attach.file("screenshots\\test_OrangeHRM_Login_002_pass.png", name="test_OrangeHRM_Login_002_pass", attachment_type=allure.attachment_type.PNG)
            lp.Click_Menu()
            lp.Click_Logout()
            assert True
        else:
            self.driver.save_screenshot("screenshots\\test_OrangeHRM_Login_002_fail.png")
            self.logger.error("Login Failed")
            self.logger.info("Login Failed")
            allure.attach.file("screenshots\\test_OrangeHRM_Login_002_fail.png", name="test_OrangeHRM_Login_002_fail", attachment_type=allure.attachment_type.PNG)
            assert False
        self.logger.info("test_OrangeHRM_Login_002 is passed ,completed")
        self.logger.info("===OrangeHRM Login Test Completed===")

#pytest -v -n=auto --html=Html_Reports\OrangeHRM_Login.html --alluredir=Allure_Reports --browser chrome