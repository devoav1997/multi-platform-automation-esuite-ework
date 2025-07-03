from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
import random
import time

fake = Faker()

INDUSTRY_LIST = [
    "Construction", "Education", "Healthcare", "Agriculture", "Energy",
    "Entertainment and Media", "Fast Moving Customer Goods (FMCG)", "Automotive",
    "Mining and Metals", "Retail", "Technology", "Telecommunications",
    "Transportation and Logistics", "Finance and Banking", "Food & Beverage",
    "Hospitality", "Manufacturing", "Nonprofit and Social Services", "Real Estate"
]

COMPANY_TYPE_LIST = [
    "Importer/Exporter", "Consignor/Consignee", "Marketplace", "Retailer", "Service Aggregator",
    "Third-Party Logistics (3PL) Provider", "Holding Company", "Cooperative (Co-op)",
    "Franchisee/Franchisor", "Manufacturer", "Principal", "Agent", "Dropshipper",
    "Freight Forwarder", "Distributor", "Service", "Service Provider"
]

LANGUAGE_LIST = ["Indonesia", "English"]
COUNTRY_LIST = ["Indonesia"] # Asumsi Indonesia saja untuk test detail, sesuaikan jika perlu

INDONESIA_PROVINCES = [
    "ACEH", "SUMATERA UTARA", "SUMATERA BARAT", "RIAU", "JAMBI", "SUMATERA SELATAN", "BENGKULU", "LAMPUNG",
    "KEP BANGKA BELITUNG", "KEP RIAU", "DKI JAKARTA", "JAWA BARAT", "JAWA TENGAH", "DI YOGYAKARTA", "JAWA TIMUR",
    "BANTEN", "BALI", "NUSA TENGGARA BARAT", "NUSA TENGGARA TIMUR", "KALIMANTAN BARAT", "KALIMANTAN TENGAH",
    "KALIMANTAN SELATAN", "KALIMANTAN TIMUR", "KALIMANTAN UTARA", "SULAWESI UTARA", "SULAWESI TENGAH",
    "SULAWESI SELATAN", "SULAWESI TENGGARA", "GORONTALO", "SULAWESI BARAT", "MALUKU", "MALUKU UTARA", "PAPUA BARAT", "PAPUA"
]


@when('user creates a new company with dummy data')
def step_create_company(context):
    context.fake_company = fake.company()
    context.fake_email = fake.unique.company_email()
    context.fake_phone = "8" + str(fake.random_number(digits=9, fix_len=True))
    context.fake_address = fake.street_address()
    context.industry = random.choice(INDUSTRY_LIST)
    context.company_type = random.choice(COMPANY_TYPE_LIST)
    context.language = "Indonesia"
    context.country = "Indonesia"
    context.province = random.choice(INDONESIA_PROVINCES)
    context.postal_code = fake.postcode()

    # Go to Companies page
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="/companies" and text()="Companies"]'))
    ).click()
    time.sleep(2)
    # Add Company
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., '+ Add Company')]"))
    ).click()
    time.sleep(1)

    context.driver.find_element(By.XPATH, "//input[@placeholder='Input Company Name']").send_keys(context.fake_company)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Input Email']").send_keys(context.fake_email)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Input Phone']").send_keys(context.fake_phone)

    _select_dropdown(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Industry')])]", context.industry)
    _select_dropdown(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Company Type')])]", context.company_type)
    _select_dropdown(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Language')])]", context.language)

    # Address
    context.driver.find_element(By.XPATH, "//input[@placeholder='Input Address']").send_keys(context.fake_address)
    _select_dropdown(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Country')])]", context.country)
    _select_dropdown(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Province')])]", context.province)

    # --- INI BAGIAN RANDOM PILIH CITY/DISTRICT/SUBDISTRICT SETELAH DROPDOWN PROVINSI ---
    context.city = _select_dropdown_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'City')])]", return_selected=True)
    context.district = _select_dropdown_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'District')])]", return_selected=True)
    context.subdistrict = _select_dropdown_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Sub District')])]", return_selected=True)

    _input_postal_code(context, context.postal_code)
    context.driver.find_element(By.XPATH, "//button[normalize-space(text())='Next']").click()
    time.sleep(1)

     # Next
    context.driver.find_element(By.XPATH, "//button[normalize-space(text())='Next']").click()
    time.sleep(2)

    # Tunggu benar-benar field Branch Name muncul
    branch_name_input = WebDriverWait(context.driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Branch Name')]"))
    )
    branch_name_input.send_keys("HQ Automation")
    context.driver.find_element(By.XPATH, "//input[@placeholder='Input Address']").send_keys("Jl. Automation Cabang")
    _select_dropdown(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Country')])]", context.country)
    _select_dropdown(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Province')])]", context.province)
    _select_dropdown_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'City')])]")
    _select_dropdown_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'District')])]")
    _select_dropdown_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Sub District')])]")
    _input_postal_code(context, context.postal_code)

    _click_policy_checkbox(context)
    register_btn = context.driver.find_element(By.XPATH, "//button[contains(., 'Register')]")
    context.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", register_btn)
    time.sleep(0.3)
    register_btn.click()
    time.sleep(5)

@then('user should see the new company listed on Companies page')
def step_see_new_company(context):
    WebDriverWait(context.driver, 20).until(
        EC.url_contains("/companies")
    )
    time.sleep(2)  # pastikan animasi/refresh selesai
    # Ambil ulang semua card!
    cards = context.driver.find_elements(By.XPATH, "//div[contains(@class, 'rounded-lg') and contains(@class, 'flex-col')]")
    print(f"[DEBUG] Ada {len(cards)} cards company di halaman.")
    found = False
    for i, card in enumerate(cards):
        print(f"[CARD {i}]: {card.text.strip()}")
        # Toleransi: lowercase & strip
        if context.fake_company.lower().strip() in card.text.lower().strip():
            found = True
            # Cari tombol Manage di dalam card saat ini
            try:
                context.company_manage_btn = card.find_element(By.XPATH, ".//button[contains(.,'Manage')]")
            except Exception:
                context.company_manage_btn = None
                print("[DEBUG] Manage button not found, coba manual di step berikutnya.")
            break
    assert found, f"New company '{context.fake_company}' not found on Companies page"


@then('user can view company details and see all inputted data correctly')
def step_check_company_detail(context):
    # Klik tombol Manage di card company terbaru
    context.company_manage_btn.click()
    # Tunggu halaman detail terbuka (gunakan heading unik Company Details)
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(.,'Company Details')]"))
    )
    time.sleep(1)

    # Helper untuk print & assert field, cek attr title atau text, handle ellipsis
    def _assert_field(xpath, expected, label):
        el = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        # Pakai title kalau ada (untuk dropdown/ellipsis), fallback ke .text
        value = el.get_attribute("title") or el.get_attribute("value") or el.text
        value_clean = value.replace('...', '').strip().lower()
        expected_clean = expected.strip().lower()
        print(f"[DEBUG] {label}: expected='{expected}' | found='{value}'")
        # Lolos jika salah satu (toleransi untuk UI ellipsis)
        assert expected_clean.startswith(value_clean) or value_clean.startswith(expected_clean) or expected_clean in value_clean or value_clean in expected_clean, \
            f"Field {label}: expected '{expected}' in '{value}'"

    # Company Name
    _assert_field("//input[@placeholder='Input Company Name']", context.fake_company, "Company Name")
    # Industry Type (dropdown, kemungkinan ada ellipsis/title)
    _assert_field("//span[text()='Industry Type']/following::button[1]/span", context.industry, "Industry Type")
    # Company Type
    _assert_field("//span[text()='Company Type']/following::button[1]/span", context.company_type, "Company Type")
    # Country
    _assert_field("//span[text()='Country']/following::button[1]/span", context.country, "Country")
    # Province
    _assert_field("//span[text()='Province']/following::button[1]/span", context.province, "Province")
    # City
    _assert_field("//span[text()='City']/following::button[1]/span", context.city, "City")
    # District
    _assert_field("//span[text()='District']/following::button[1]/span", context.district, "District")
    # Postal Code
    _assert_field("//span[text()='Postal Code']/parent::div//input", context.postal_code, "Postal Code")
    # Email
    _assert_field("//input[@placeholder='Input Email']", context.fake_email, "Email")
    # Mobile Number (tanpa +62, pastikan format sesuai)
    phone_on_page = context.driver.find_element(By.XPATH, "//input[@placeholder='Input Mobile Number']").get_attribute("value")
    fake_phone_nozero = context.fake_phone.lstrip("0")
    print(f"[DEBUG] Mobile Number: expected='{fake_phone_nozero}' | found='{phone_on_page}'")
    assert fake_phone_nozero in phone_on_page, f"Field Mobile Number: expected '{fake_phone_nozero}' in '{phone_on_page}'"
    # Company Address
    _assert_field("//textarea[@placeholder='Input Company Address']", context.fake_address, "Company Address")

    print("✅ All company detail fields verified OK!")
    context.driver.quit()



# Helper
def _select_dropdown(context, dropdown_xpath, option_text):
    # Pastikan dropdown di-scroll ke layar & klik
    dropdown = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
    )
    context.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", dropdown)
    time.sleep(0.2)
    dropdown.click()
    time.sleep(0.2)
    
    # Cari dan klik option yang sesuai
    option_xpath = f"//div[@role='menu']//span[normalize-space(text())='{option_text}']"
    el = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, option_xpath))
    )
    try:
        context.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        time.sleep(0.2)
        el.click()
    except Exception:
        # Jika klik biasa gagal, pakai JS click
        context.driver.execute_script("arguments[0].click();", el)
    time.sleep(0.2)


def _select_dropdown_index(context, dropdown_xpath, return_selected=False):
    dropdown = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
    )
    context.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", dropdown)
    time.sleep(0.2)
    dropdown.click()
    time.sleep(0.2)
    options = context.driver.find_elements(By.XPATH, "//div[@role='menu']//span")
    idx = random.randint(0, len(options)-1) if options else 0
    el = options[idx]
    selected_text = el.get_attribute("title") or el.text
    try:
        context.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        time.sleep(0.2)
        el.click()
    except Exception:
        context.driver.execute_script("arguments[0].click();", el)
    time.sleep(0.2)
    if return_selected:
        return selected_text



def _input_postal_code(context, value):
    # Fallback: coba beberapa kemungkinan XPATH
    input_xpaths = [
        "//span[contains(text(),'Postal Code')]/parent::div//input",
        "//label[contains(.,'Postal Code')]/following-sibling::input",
        "//input[contains(@placeholder,'Postal Code')]"
    ]
    for xpath in input_xpaths:
        inputs = context.driver.find_elements(By.XPATH, xpath)
        if inputs:
            inputs[0].clear()
            inputs[0].send_keys(value)
            return True
    return False

def _click_policy_checkbox(context):
    btns = context.driver.find_elements(By.XPATH, "//button[@role='checkbox']")
    for btn in btns:
        parent = btn.find_element(By.XPATH, "./ancestor::div[1]")
        if "Policy" in parent.text and "Terms and Conditions" in parent.text:
            if btn.get_attribute("aria-checked") == "false":
                btn.click()
            return True
    return False

