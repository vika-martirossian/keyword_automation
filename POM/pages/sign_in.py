from selenium.webdriver.common.by import By

from POM.lib.helpers import Helpers


class SignIn(Helpers):
    email_field = (By.XPATH, "//*[@type='email']")
    password_field = (By.XPATH, "//*[@type='password']")
    login_btn = (By.ID, "kw-button-288")

    def enter_email_address(self, email):
        self.find_and_send_keys(self.email_field, email)

    def enter_password(self, password):
        self.find_and_send_keys(self.password_field, password)

    def click_on_login_btn(self, expected_page_url="https://app-qa1.keyword.me/dashboard"):
        self.find_and_click(self.login_btn)
        current_page_url = self.get_page_url()
        assert current_page_url == expected_page_url
