import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from POM.lib.helpers import Helpers
from POM.lib.assertions import assert_that

driver = webdriver.Chrome()


class Reports(Helpers):
    profile_btn = (By.XPATH, "//*[@class='button-profile']")
    reports_btn = (By.XPATH, "//*[@href='/reports']")
    automation_project = (By.XPATH, "(//*[@data-tooltip='automation/dont delete'])[1]")
    report_history_btn = (By.XPATH, "(//*[@class='kw kw-history'])[18]")
    delivery_date = (By.XPATH, "//*[@data-tooltip='Delivery Date']")
    edit_report_btn = (By.XPATH, "(//*[@class='kw kw-edit-3'])[18]")
    send_report_btn = (By.XPATH, "(//*[@class='kw kw-send'])[18]")
    edit_scheduled_report_title = (By.XPATH, "//*[@class='report-form__title']")
    close_btn = (By.XPATH, "//*[@class='kw kw-x']")
    sent_a_moment_ago = (By.XPATH, "//*[@data-tooltip='Sent A moment ago']")
    success_toast = (By.XPATH, "//*[@class='toast toast-success']")

    def navigate_to_reports_page(self):
        self.find_and_click(self.profile_btn)
        self.find_and_click(self.reports_btn)

    def check_the_project_presence(self, expected_report_name="automation/dont delete"):
        actual_report = self.find(self.automation_project, get_text=True)
        assert_that(actual_report, expected_report_name)

    def hover_over_the_project(self):
        elem = self.find(self.automation_project)
        self.focus_on_element(elem)

    def open_report_history(self, expected_table_column="Delivery Date"):
        self.find_and_click(self.report_history_btn)
        time.sleep(3)
        actual_table_column = self.find(self.delivery_date, get_text=True)
        assert_that(actual_table_column, expected_table_column)

    def close_report_history(self):
        self.find_and_click(self.close_btn)
        self.wait_for_invisibility(self.delivery_date)

    def open_edit_report_modal(self, expected_modal_title=" Edit Scheduled Report "):
        self.find_and_click(self.edit_report_btn)
        modal_title = self.find(self.edit_scheduled_report_title, get_text=True)
        assert_that(modal_title, expected_modal_title)

    def close_edit_report_modal(self):
        self.find_and_click(self.close_btn)
        self.wait_for_invisibility(self.edit_scheduled_report_title)

    def send_report_immediately(self):
        elem = self.find(self.automation_project)
        self.focus_on_element(elem)
        self.find_and_click(self.send_report_btn)
        assert self.assert_element_present(self.success_toast)
        self.find_and_click(self.report_history_btn)
        assert self.assert_element_present(self.sent_a_moment_ago)
