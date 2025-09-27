from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://demo.openmrs.org/openmrs/login.htm"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.location_session = page.locator("#Inpatient-Ward") # Locator yang lebih spesifik
        self.login_button = page.locator("#loginButton")
        self.error_message = page.locator("#error-message")
        self.empty_location_message = page.locator("#sessionLocationError")


    def navigate(self):
        """Membuka halaman login."""
        self.page.goto(self.URL)

    def login(self, username, password, location_text="Inpatient Ward"):
        """Melakukan proses login lengkap."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.page.get_by_text(location_text).click()
        self.login_button.click()
    
    def login_with_empty_fields(self, location_text="Inpatient Ward"):
        """Mencoba login dengan field kosong."""
        self.page.get_by_text(location_text).click()
        self.login_button.click()
    
    def login_with_empty_location(self, username, password):
        """Mencoba login dengan field kosong."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def check_error_message(self, expected_text):
        """Memvalidasi pesan error yang muncul."""
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text(expected_text)
    
    def check_empty_message(self, expected_text):
        """validasi error message empty field"""
        expect(self.empty_location_message).to_be_visible()
        expect(self.empty_location_message).to_have_text(expected_text)