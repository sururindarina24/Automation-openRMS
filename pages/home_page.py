from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.logged_in_message = page.locator("h4")
        self.register_patient_link = page.get_by_role("link", name="Register a patient")
        self.find_patient_link = page.get_by_role("link", name="Find Patient Record")
        self.logout_link = page.get_by_role("link", name="Logout")

    def verify_login_success(self, username):
        """Memastikan login berhasil dengan memeriksa pesan selamat datang."""
        expect(self.logged_in_message).to_contain_text(f"Logged in as Super User ({username})")

    def navigate_to_register_patient(self):
        """Klik link untuk mendaftarkan pasien."""
        self.register_patient_link.click()

    def navigate_to_find_patient(self):
        """Klik link untuk mencari pasien."""
        self.find_patient_link.click()

    def logout(self):
        """Melakukan logout dari sistem."""
        self.logout_link.click()