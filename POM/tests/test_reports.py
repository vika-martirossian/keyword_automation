from POM.tests.base_test import BaseTest


class TestReports(BaseTest):
    def test_verify_the_project_presence(self):
        self.successful_sign_in()
        self.go_to_reports_page()
        self.verify_certain_project_presence()

    def test_verify_report_history_modal_opening_closing(self):
        self.open_and_close_reports_history()

    def test_verify_edit_scheduled_report_modal_opening_closing(self):
        self.open_and_close_edit_scheduled_report()

    def test_verify_report_immediately_sending(self):
        self.report_immediately_sending()

