from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class RegisterPatientPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.given_name_input = page.locator("input[name='givenName']")
        self.middle_name_input = page.locator("input[name='middleName']")
        self.family_name_input = page.locator("input[name='familyName']")
        self.next_button = page.locator("#next-button")
        self.gender_dropdown = page.locator("#gender-field")
        self.day_input = page.locator("#birthdateDay-field")
        self.month_select = page.locator("#birthdateMonth-field")
        self.year_input = page.locator("#birthdateYear-field")
        self.address_input = page.locator("#address1")
        self.city_input = page.locator("#cityVillage")
        self.state_input = page.locator("#stateProvince")
        self.country_input = page.locator("#country")
        self.zip_input = page.locator("#postalCode")
        self.phone_input = page.locator("input[name='phoneNumber']")
        self.relationship_dropdown = page.locator("#relationship_type")
        self.relationship_name = page.locator(".person-typeahead")
        self.confirm_button = page.locator("#submit")
        self.name_error_message = page.locator(".field-error")
        self.given_name_success = page.locator(".PersonName-givenName")
        self.confirm_empty_button = page.locator("#confirmation_label")
        self.duplicate_account = page.locator("#similarPatientsSelect .name").nth(0)


    def fill_patient_data(self, patient_data):
        """Mengisi semua data pasien dari sebuah dictionary."""
        self.given_name_input.fill(patient_data["given_name"])
        self.middle_name_input.fill(patient_data["middle_name"])
        self.family_name_input.fill(patient_data["family_name"])
        self.next_button.click()
        self.gender_dropdown.select_option(value="M")
        self.next_button.click()
        self.day_input.fill(patient_data["day"])
        self.month_select.select_option(label="January")
        self.year_input.fill(patient_data["year"])
        self.next_button.click()
        self.address_input.fill(patient_data["address"])
        self.city_input.fill(patient_data["city"])
        self.state_input.fill(patient_data["state"])
        self.country_input.fill(patient_data["country"])
        self.zip_input.fill(patient_data["zip"])
        self.next_button.click()
        self.phone_input.fill(patient_data["phone"])
        self.next_button.click()
        self.relationship_dropdown.select_option(label="Sibling")
        self.relationship_name.fill(patient_data["relation_name"])
        self.next_button.click()
        self.confirm_button.click()
        

    def submit_registration(self):
        """Menyimpan data pendaftaran pasien."""
        self.confirm_button.click()

    def check_name_validation_error(self, error_text="Required"):
        """Memeriksa pesan error validasi untuk field nama."""
        self.confirm_empty_button.click()

        first_error = self.page.locator(".field-error").first
        expect(first_error).to_be_visible()
        expect(first_error).to_have_text(error_text) 

    def check_create_account_success(self):
        """Memeriksa pesan sukses pembuatan akun."""
        expect(self.given_name_success).to_be_visible(timeout=5000)
        expect(self.given_name_success).to_have_text()

    def check_duplicate_user(self, patient_data_exist):
        self.given_name_input.fill(patient_data_exist["given_name"])
        self.middle_name_input.fill(patient_data_exist["middle_name"])
        self.family_name_input.fill(patient_data_exist["family_name"])
        self.next_button.click()
        self.gender_dropdown.select_option(value="M")
        self.next_button.click()
        self.day_input.fill(patient_data_exist["day"])
        self.month_select.select_option(label="January")
        self.year_input.fill(patient_data_exist["year"])
        self.next_button.click()
        self.address_input.fill(patient_data_exist["address"])
        self.city_input.fill(patient_data_exist["city"])
        self.state_input.fill(patient_data_exist["state"])
        self.country_input.fill(patient_data_exist["country"])
        self.zip_input.fill(patient_data_exist["zip"])
        self.next_button.click()
        self.phone_input.fill(patient_data_exist["phone"])
        self.next_button.click()
        self.relationship_dropdown.select_option(label="Sibling")
        self.relationship_name.fill(patient_data_exist["relation_name"])
        self.next_button.click()

    def verify_patient_name(self, given_name: str, family_name: str):
        """Memvalidasi nama depan dan nama keluarga pasien."""
        expect(self.duplicate_account).to_be_visible(timeout=5000)
        expect(self.duplicate_account).to_have_text(f"{given_name} {family_name}")