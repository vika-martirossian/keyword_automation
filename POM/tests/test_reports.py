from POM.tests.base_test import BaseTest


class TestReports(BaseTest):
    def test_verify_the_project_presence(self):
        self.successful_sign_in()
        self.go_to_reports_page()
        self.verify_certain_project_presence()

    def test_verify_report_history_modal_opening_closing(self):
        self.successful_sign_in()
        self.go_to_reports_page()
        self.open_and_close_reports_history()

    def test_verify_edit_scheduled_report_modal_opening_closing(self):
        self.successful_sign_in()
        self.go_to_reports_page()
        self.open_edit_scheduled_report()
        self.close_edit_scheduled_report()

    def test_verify_report_immediately_sending(self):
        self.successful_sign_in()
        self.go_to_reports_page()
        self.report_immediately_sending()

    def test_editing_report_email_recipient(self):
        self.successful_sign_in()
        self.go_to_reports_page()
        self.open_edit_scheduled_report()
        self.edit_recipient_email()
        self.open_edit_scheduled_report()
        # here should be an assertion of checking the email address

    def test_adding_a_project_to_the_filter(self):
        self.successful_sign_in()
        self.go_to_reports_page()
        self.open_edit_scheduled_report()
        self.add_a_project_to_the_filter()
        self.open_edit_scheduled_report()
        # here should be an assertion of checking the filter separately

