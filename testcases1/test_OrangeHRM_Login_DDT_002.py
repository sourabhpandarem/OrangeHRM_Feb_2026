import pytest
import allure
import openpyxl

from Utilities.XLUtils import XLUtils_class
from Utilities.logger import Logger_Class
from pageObjects.Loginpage import Login_page_class
from Utilities.readconfig import ReadConfig
@pytest.mark.usefixtures("driver_setup")
class  Test_OrangeHRM_Login_DDT_002:
    driver = None
    login_url = ReadConfig.get_login_url()
    log = Logger_Class.get_loggen()
    excel_file = ".\\Test_Data\\OrangeHRM_Test_Data.xlsx"
    sheet = "Sheet1"

    def test_orange_hrm_login_ddt_003(self):
        self.log.info("Starting Test: Verify OrangeHRM Login Functionality")
        row_count = XLUtils_class.get_row_count(self.excel_file, self.sheet)
        self.log.info(f"Total Rows in Excel: {row_count}")
        result = []
        for i in range(2, row_count + 1):
            username = XLUtils_class.read_data(self.excel_file, self.sheet, i, 2)
            password = XLUtils_class.read_data(self.excel_file, self.sheet, i, 3)
            expected_result = XLUtils_class.read_data(self.excel_file, self.sheet, i, 4)
            self.log.info(f"Test Data: Username={username}, Password={password}, Expected Result={expected_result}")
            self.log.info("Navigating to OrangeHRM Login Page")
            self.driver.get(self.login_url)
            self.log.info("OrangeHRM Login Page Loaded")
            lp = Login_page_class(self.driver)
            lp.Enter_Username(username)
            lp.Enter_Password(password)
            lp.Click_Login()
            if lp.verify_login() == "Login Successful":
                self.log.info(f"Login Successful for Username={username}")
                self.driver.save_screenshot(f"screenshots\\test_orange_hrm_login_ddt_003_pass_{username}.png")
                allure.attach.file(f"screenshots\\test_orange_hrm_login_ddt_003_pass_{username}.png", name=f"test_orange_hrm_login_ddt_003_pass_{username}", attachment_type=allure.attachment_type.PNG)
                lp.Click_Menu()
                lp.Click_Logout()

                actual_result = "Login Successful"
            else:
                self.log.error(f"Login Failed for Username={username}")
                self.driver.save_screenshot(f"screenshots\\test_orange_hrm_login_ddt_003_fail_{username}.png")
                allure.attach.file(f"screenshots\\test_orange_hrm_login_ddt_003_fail_{username}.png", name=f"test_orange_hrm_login_ddt_003_fail_{username}", attachment_type=allure.attachment_type.PNG)
                result.append("Fail")
                actual_result = "Login Failed"
            if actual_result == expected_result:
                self.log.info(f"Test Passed for Username={username}")
                test_status = "Pass"
                result.append("Pass")
            else:
                self.log.error(f"Test Failed for Username={username}")
                test_status = "Fail"
                result.append("Fail")
            XLUtils_class.write_data(self.excel_file, self.sheet, i, 6, test_status)
        self.log.info(f"Test Results: {result}")
        assert "Fail" not in result
        self.log.info("test_orange_hrm_login_ddt_003 test Completed")
        self.log.info("=============================================================")






#pytest -v -n=auto --html=Html_Reports\OrangeHRM_Login.html --alluredir=Allure_Reports --browser chrome