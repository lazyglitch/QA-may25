from base_page import BasePage
from playwright.sync_api import expect


class ExamplePage(BasePage):

    def should_have_valid_header(self):
        header = self.page.locator("h1")
        expect(header).to_be_visible()
        expect(header).to_contain_text("Example")

    def should_have_more_information_link(self):
        link = self.page.get_by_text("More information")
        expect(link).to_be_visible()

    def click_more_information_link(self):
        self.page.get_by_text("More information").click()

    def should_have_correct_url_after_click(self):
        expect(self.page).to_have_url("https://www.iana.org/help/example-domains")
