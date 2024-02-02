from selenium.webdriver.common.by import By

from POM.lib.helpers import Helpers
from POM.lib.assertions import assert_that


class EditScheduledReport(Helpers):
    recipient_email = (By.XPATH, "(//*[@type='text'])[4]")
    recipient_email_tb = (By.XPATH, "(//*[@data-v-8c628df4])[12]")
    project_filter = (By.XPATH, "//*[@class='select-projects-button-text']")
    travel_project = (By.XPATH, "(//*[@data-tooltip='(H) Travel with Booking Test'])[3]")
    frequency_drop_down = (By.XPATH, "//*[@class='btn-content']")
    frequency_select = (By.XPATH, "//*[@class='secret']")
    select_days_drop_down = (By.XPATH, "(//*[@id='kw-button-450'])[7]")
    pdf_radio_btn = (By.XPATH, "(//*[@class='radio-button__content'])[1]")
    pdf_label = (By.XPATH, "(//*[@class='radio-button__label'])[1]")
    csv_radio_btn = (By.XPATH, "(//*[@class='radio-button__content'])[2]")
    csv_label = (By.XPATH, "(//*[@class='radio-button__label'])[2]")
    save_btn = (By.XPATH, "(//*[@class='kw-button kw-btn-primary'])[2]")
    default_frequency = ""
    actual_freq = ""

    def edit_recipient_email(self):
        addition = self.generate_random_string(5)
        edited_email = f"automation{addition}@mailinator.com"
        actual_email = self.find(self.recipient_email_tb, get_text=True)
        self.find(self.recipient_email).clear()
        self.find_and_send_keys(self.recipient_email, edited_email)
        self.find_and_click(self.save_btn)
        assert_that(actual_email, edited_email)

    def get_default_recipient_email(self, default_email="automation@mailinator.com"):
        self.find(self.recipient_email).clear()
        self.find_and_send_keys(self.recipient_email, default_email)

    def add_a_project_to_the_filter(self, exp_projects="automation/dont delete, (H) Travel with Booking Test"):
        self.find_and_click(self.project_filter)
        self.find_and_click(self.travel_project)
        actual_projects = self.find(self.project_filter, get_text=True)
        assert_that(actual_projects, exp_projects)

    def change_scheduled_frequency(self):
        self.find_and_click(self.frequency_drop_down)
        default_frequency = self.find(self.frequency_drop_down, get_text=True)
        freq_select = self.find(self.frequency_select)
        selected_option = self.select_item(freq_select, value=2)
        self.find_and_click(selected_option)
        actual_freq = self.find(self.frequency_drop_down, get_text=True)
        self.find_and_click(self.save_btn)
