from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


class Login_page_class:
    text_username_xpath = "//input[@placeholder='Username']"
    text_password_xpath = "//input[@placeholder='Password']"
    btn_login_xpath = "//button[@type='submit']"
    click_menu_xpath = "//p[@class='oxd-userdropdown-name']"
    click_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)



    def Enter_Username(self,username):
        time.sleep(5)
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_username_xpath)))
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(username)

    def Enter_Password(self,password):

        self.wait.until((expected_conditions.visibility_of_element_located((By.XPATH, self.text_password_xpath))))
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def Click_Login(self):
        time.sleep(5)
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.btn_login_xpath)))
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def Click_Menu(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.click_menu_xpath)))
        self.driver.find_element(By.XPATH, self.click_menu_xpath).click()

    def Click_Logout(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.click_logout_xpath)))
        self.driver.find_element(By.XPATH, self.click_logout_xpath).click()

    def verify_login(self):
        try:
            time.sleep(10)
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.click_menu_xpath)))
            self.driver.find_element(By.XPATH, self.click_menu_xpath)
            return "Login Successful"
        except:
            return "Login Failed"
        