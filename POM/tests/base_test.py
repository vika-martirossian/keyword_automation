import pytest
from testing_data.test_data import valid_login
from testing_data.test_data import valid_password


@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def successful_sign_in(self):
        self.signin.enter_email_address(valid_login)
        self.signin.enter_password(valid_password)
        self.signin.click_on_login_btn()

    def go_to_reports_page(self):
        self.reports.navigate_to_reports_page()

    def verify_certain_project_presence(self):
        self.reports.check_the_project_presence()

    def open_and_close_reports_history(self):
        self.reports.hover_over_the_project()
        self.reports.open_report_history()
        self.reports.close_report_history()

    def open_edit_scheduled_report(self):
        self.reports.hover_over_the_project()
        self.reports.open_edit_report_modal()

    def close_edit_scheduled_report(self):
        self.reports.close_edit_report_modal()

    def report_immediately_sending(self):
        self.reports.hover_over_the_project()
        self.reports.send_report_immediately()

    def edit_recipient_email(self):
        self.editreport.edit_recipient_email()

    def add_a_project_to_the_filter(self):
        self.add_a_project_to_the_filter()
