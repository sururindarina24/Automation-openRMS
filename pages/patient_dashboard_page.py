from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class PatientDashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.patient_name_header = page.locator(".PersonName-givenName")
        self.find_patient_record_link = page.get_by_role("link", name="Find Patient Record")
        self.search_input = page.locator("#patient-search")
        self.no_results_message = page.locator("td.dataTables_empty")
        self.search_result = page.get_by_role("cell", name="100HXG")

    def verify_patient_creation(self, given_name):
        """Memvalidasi bahwa nama pasien muncul di header."""
        ###expect(self.patient_name_header).to_be_visible()
        expect(self.patient_name_header).to_have_text(given_name)

    def search_for_patient(self, full_name, found=True):
        """Mencari pasien dan memvalidasi hasilnya."""
        self.find_patient_record_link.click()
        self.search_input.fill(full_name)
        expect(self.search_result).to_be_visible()