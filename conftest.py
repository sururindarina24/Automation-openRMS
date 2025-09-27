import pytest
from playwright.sync_api import Page

# Import page object yang dibutuhkan untuk fixture
from pages.login_page import LoginPage

# --- Konfigurasi Awal ---
USERNAME = "admin"
PASSWORD = "Admin123"

@pytest.fixture(scope="function")
def login_setup(page: Page):
    """Fixture untuk melakukan login sebelum tes yang membutuhkan."""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)
    return page