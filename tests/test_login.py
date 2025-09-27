import pytest
from playwright.sync_api import Page
import random
import string

# Import semua page object yang dibutuhkan
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.register_patient_page import RegisterPatientPage
from pages.patient_dashboard_page import PatientDashboardPage

# --- Konfigurasi Awal ---
USERNAME = "admin"
PASSWORD = "Admin123"

# =========== KUMPULAN TEST CASE =================

def test_positive_login(page: Page):
    """Skenario 1: Login dengan kredensial yang valid."""
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)
    
    home_page.verify_login_success(USERNAME)

def test_negative_login_wrong_password(page: Page):
    """Skenario 2: Login dengan password yang salah."""
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login(USERNAME, "PasswordSalah")
    
    login_page.check_error_message("Invalid username/password. Please try again.")

def test_negative_login_empty_fields(page: Page):
    """Skenario 3: Login dengan field kosong."""
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login_with_empty_fields()

    login_page.check_error_message("Invalid username/password. Please try again.")

def test_negative_login_empty_location(page: Page):
    """Skenario 4: Login dengan lokasi kosong"""
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login_with_empty_location("Admin", "Admin123")

    login_page.check_empty_message("You must choose a location!")