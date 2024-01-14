import time

from selenium.webdriver.common.by import By

from POM.lib.helpers import Helpers
from POM.lib.assertions import assert_that


class EditScheduledReport(Helpers):
    recipient_email = (By.XPATH, "(//*[@type='text'])[4]")
    project_filter = (By.XPATH, "//*[@class='select-projects-button-text']")
    travel_project = (By.XPATH, "(//*[@data-tooltip='(H) Travel with Booking Test'])[3]")
    frequency_drop_down = (By.XPATH, "//*[@class='form-control dropdown-toggle']")
    select_days_drop_down = (By.XPATH, "(//*[@id='kw-button-450'])[7]")
    pdf_radio_btn = (By.XPATH, "(//*[@class='radio-button__content'])[1]")
    pdf_label = (By.XPATH, "(//*[@class='radio-button__label'])[1]")
    csv_radio_btn = (By.XPATH, "(//*[@class='radio-button__content'])[2]")
    csv_label = (By.XPATH, "(//*[@class='radio-button__label'])[2]")
    save_btn = (By.XPATH, "(//*[@class='kw-button kw-btn-primary'])[2]")

    def edit_recipient_email(self, edited_email="automation1@mailinator.com"):
        self.find(self.recipient_email).clear()
        self.find_and_send_keys(self.recipient_email, edited_email)
        # here should be an assertion of checking the email address

    def add_a_project_to_the_filter(self, exp_projects="automation/dont delete, (H) Travel with Booking Test"):
        self.find_and_click(self.project_filter)
        self.find_and_click(self.travel_project)
        actual_projects = self.find(self.project_filter, get_text=True)
        assert_that(actual_projects, exp_projects)

