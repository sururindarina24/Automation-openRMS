import pytest
from playwright.sync_api import Page
import random
import string

# Import page object yang dibutuhkan untuk tes ini
from pages.home_page import HomePage
from pages.register_patient_page import RegisterPatientPage
from pages.patient_dashboard_page import PatientDashboardPage

# Data unik untuk pasien baru, spesifik untuk file ini
random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
patient_data_exist = {
    "given_name": "Jane",
    "middle_name": "Doe",
    "family_name": "Smith",
    "day": "20",
    "year": "1985",
    "address": "Jl. Gatot Subroto No. 2",
    "city": "Jakarta",
    "state": "DKI Jakarta",
    "country": "Indonesia",
    "zip": "12345",
    "phone": "081234567890",
    "relation_name": "John"
}
patient_data = {
    "given_name": "kita",
    "middle_name": "akan",
    "family_name": "membuat",
    "day": "20",
    "year": "1985",
    "address": "Jl. Gatot Subroto No. 2",
    "city": "Jakarta",
    "state": "DKI Jakarta",
    "country": "Indonesia",
    "zip": "12345",
    "phone": "081234567890",
    "relation_name": "John"
}


# Tes yang berhubungan dengan registrasi pasien
def test_add_new_patient(login_setup: Page):
    """Skenario 4: Menambah pasien baru dengan data valid."""
    page = login_setup
    home_page = HomePage(page)
    register_page = RegisterPatientPage(page)
    patient_dashboard = PatientDashboardPage(page)
    
    home_page.navigate_to_register_patient()
    register_page.fill_patient_data(patient_data)
    patient_dashboard.verify_patient_creation(patient_data["given_name"])

def test_add_new_patient_exist(login_setup: Page):
    """Skenario 5: Menambah pasien baru dengan data exist."""
    page = login_setup
    home_page = HomePage(page)
    register_page = RegisterPatientPage(page)
    patient_dashboard = PatientDashboardPage(page)
    
    home_page.navigate_to_register_patient()
    register_page.check_duplicate_user(patient_data_exist)
    register_page.verify_patient_name(
        patient_data_exist["given_name"], 
        patient_data_exist["family_name"]
    )

def test_add_patient_without_name(login_setup: Page):
    """Skenario 5: Menambahkan pasien tanpa mengisi nama."""
    page = login_setup
    home_page = HomePage(page)
    register_page = RegisterPatientPage(page)
    
    home_page.navigate_to_register_patient()
    register_page.check_name_validation_error(error_text="Required")

def test_search_created_patient(login_setup: Page):
    """Skenario 6: Mencari pasien yang baru saja dibuat."""
    # Catatan: Tes ini lebih baik jika digabungkan atau dijalankan setelah test_add_new_patient,
    # Namun untuk independensi, kita bisa membuat pasien baru lagi di sini.
    # Untuk contoh ini, kita asumsikan test_add_new_patient sudah membuat data yang bisa dicari.
    page = login_setup
    patient_dashboard = PatientDashboardPage(page)
    # Gunakan nama pasien dari data yang dibuat di atas
    patient_dashboard.search_for_patient("Jane Smith")
