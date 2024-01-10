from selenium.webdriver.common.by import By

from POM.lib.helpers import Helpers
from POM.lib.assertions import assert_that
from testing_data.test_data import base_url


class Reports(Helpers):
    automation_project = (By.XPATH, "(//*[@data-tooltip='automation/dont delete'])[1]//child::span")
    report_history_btn = (By.XPATH, "(//*[@class='kw kw-history'])[18]")
    delivery_date = (By.XPATH, "//*[@data-tooltip='Delivery Date']")
    edit_report_btn = (By.XPATH, "(//*[@class='kw kw-edit-3'])[18]")
    send_report_btn = (By.XPATH, "(//*[@class='kw kw-send'])[18]")
    edit_scheduled_report_title = (By.XPATH, "//*[@class='report-form__title']")
    close_btn = (By.XPATH, "//*[@class='kw kw-x']")
    sent_a_moment_ago = (By.XPATH, "//*[@data-tooltip='Sent A moment ago']")
    success_toast = (By.XPATH, "//*[@class='toast toast-success']")

    def navigate_to_reports_page(self):
        self.navigate_to_url(base_url=base_url, path="/reports")

    def check_the_project_presence(self, expected_report_name="automation/dont delete"):
        actual_report = self.find(self.automation_project, get_text=True)
        assert_that(actual_report, expected_report_name)

    def open_report_history(self, expected_table_column="Delivery Date"):
        self.find_and_click(self.report_history_btn)
        actual_table_column = self.find(self.delivery_date, get_text=True)
        assert_that(actual_table_column, expected_table_column)

    def close_report_history(self):
        self.find_and_click(self.close_btn)
        assert len(self.find_all(self.delivery_date)) == 0

    def open_edit_report_modal(self, expected_modal_title=" Edit Scheduled Report "):
        self.find_and_click(self.edit_report_btn)
        modal_title = self.find(self.edit_scheduled_report_title, get_text=True)
        assert_that(modal_title, expected_modal_title)

    def close_edit_report_modal(self):
        self.find_and_click(self.close_btn)
        assert len(self.find_all(self.edit_scheduled_report_title)) == 0

    def send_report_immediately(self):
        self.find_and_click(self.send_report_btn)
        assert self.assert_element_present(self.success_toast)
        self.find_and_click(self.report_history_btn)
        assert self.assert_element_present(self.sent_a_moment_ago)

