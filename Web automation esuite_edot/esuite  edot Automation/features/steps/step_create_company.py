from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import random
import time
from selenium.webdriver.common.action_chains import ActionChains

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

COUNTRY_LIST = ["Philippines", "Malaysia", "Indonesia"]

INDONESIA_PROVINCES = [
    "ACEH", "SUMATERA UTARA", "SUMATERA BARAT", "RIAU", "JAMBI", "SUMATERA SELATAN", "BENGKULU", "LAMPUNG",
    "KEP BANGKA BELITUNG", "KEP RIAU", "DKI JAKARTA", "JAWA BARAT", "JAWA TENGAH", "DI YOGYAKARTA", "JAWA TIMUR",
    "BANTEN", "BALI", "NUSA TENGGARA BARAT", "NUSA TENGGARA TIMUR", "KALIMANTAN BARAT", "KALIMANTAN TENGAH",
    "KALIMANTAN SELATAN", "KALIMANTAN TIMUR", "KALIMANTAN UTARA", "SULAWESI UTARA", "SULAWESI TENGAH",
    "SULAWESI SELATAN", "SULAWESI TENGGARA", "GORONTALO", "SULAWESI BARAT", "MALUKU", "MALUKU UTARA", "PAPUA BARAT", "PAPUA"
]
MALAYSIA_STATES = [
    "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", "Pahang", "Perak", "Perlis", "Pulau Pinang",
    "Sabah", "Sarawak", "Selangor", "Terengganu", "Wilayah Persekutuan Kuala Lumpur",
    "Wilayah Persekutuan Putrajaya", "Wilayah Persekutuan Labuan"
]
PHILIPPINES_REGIONS = [
    "Region I (Ilocos Region)", "Region II (Cagayan Valley)", "Region III (Central Luzon)",
    "Region IV-A (Calabarzon)", "Region V (Bicol Region)", "Region VI (Western Visayas)",
    "Region VII (Central Visayas)", "Region VIII (Eastern Visayas)", "Region IX (Zamboanga Peninsula)",
    "Region X (Northern Mindanao)", "Region XI (Davao Region)", "Region XII (Soccsksargen)",
    "National Capital Region (NCR)", "Cordillera Administrative Region (CAR)",
    "Region XIII (Caraga)", "Mimaropa Region", "Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)"
]




@given('user is logged in to esuite')
def step_login(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    context.driver.get("https://esuite.edot.id")
    context.driver.implicitly_wait(5)
    # Klik "Use Email or Username"
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Use Email or Username')]"))
    ).click()
    # Input username/email
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Input Email or Username']"))
    ).send_keys("it.qa@edot.id")
    context.driver.find_element(By.XPATH, "//button[contains(., 'Log In')]").click()
    # Input password
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
    ).send_keys("it.QA2025")
    context.driver.find_element(By.XPATH, "//button[contains(., 'Log In')]").click()
    # Tunggu dashboard/homepage
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Welcome Back')]"))
    )
    time.sleep(2)

@when('user navigates to Companies page')
def step_navigate_companies(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="/companies" and text()="Companies"]'))
    ).click()
    time.sleep(2)

@when('user clicks Add Company')
def step_click_add_company(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., '+ Add Company')]"))
    ).click()
    time.sleep(2)
    
def robust_select_dropdown_option(context, dropdown_xpath, option_text):
    # Klik dropdown
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
    ).click()
    # Cari dan klik option sesuai text
    option_xpath = f"//div[@role='menu']//span[normalize-space(text())='{option_text}']"
    try:
        el = WebDriverWait(context.driver, 8).until(
            EC.visibility_of_element_located((By.XPATH, option_xpath))
        )
        try:
            el.click()
        except Exception:
            # Gunakan cara lain jika normal click gagal
            try:
                ActionChains(context.driver).move_to_element(el).click().perform()
            except Exception:
                context.driver.execute_script("arguments[0].click();", el)
    except Exception:
        raise Exception(f"Dropdown option '{option_text}' not found: {dropdown_xpath}")
    time.sleep(0.2)


@when('user fills company registration form with dummy data')
def step_fill_company_form(context):
    context.fake_company = fake.company()
    fake_email = fake.unique.company_email()
    fake_phone = "8" + str(fake.random_number(digits=9, fix_len=True))
    fake_address = fake.street_address()

    # Company Name, Email, Phone
    context.driver.find_element(By.XPATH, "//input[@placeholder='Input Company Name']").send_keys(context.fake_company)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Input Email']").send_keys(fake_email)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Input Phone']").send_keys(fake_phone)

    # INDUSTRY TYPE
    industry = random.choice(INDUSTRY_LIST)
    robust_select_dropdown_option(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Industry')])]", industry)

    # COMPANY TYPE
    company_type = random.choice(COMPANY_TYPE_LIST)
    robust_select_dropdown_option(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Company Type')])]", company_type)

    # LANGUAGE
    language = random.choice(LANGUAGE_LIST)
    robust_select_dropdown_option(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Language')] or span[contains(text(),'Choose Language')])]", language)

    # STREET ADDRESS (Company)
    try:
        context.driver.find_element(
            By.XPATH, "//span[contains(.,'Street Address')]/ancestor::div[contains(@class,'flex') or contains(@class,'mb')][1]//input[@placeholder='Input Address']"
        ).send_keys(fake_address)
    except Exception:
    # Fallback to first "Input Address" input
        address_inputs = context.driver.find_elements(By.XPATH, "//input[@placeholder='Input Address']")
        if address_inputs:
            address_inputs[0].send_keys(fake_address)
        else:
            raise Exception("Street Address field not found!")

    # COUNTRY
    robust_select_dropdown_option(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Country')])]", "Indonesia")


       # Province, City, District, Sub District, Postal Code
    for label in ['Province', 'City', 'District', 'Sub District', 'Postal Code']:
        found = False
        # --- Coba dropdown combobox (button dengan role='combobox') ---
        try:
            dropdown_xpath = f"//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'{label}')])]"
            dropdown = context.driver.find_element(By.XPATH, dropdown_xpath)
            dropdown.click()
            # Untuk Postal Code: jika tidak ada opsi, klik pertama
            if label == "Postal Code":
                try:
                    # Coba klik opsi yang visible (bisa pakai faker atau random atau klik saja yang pertama)
                    WebDriverWait(context.driver, 4).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "//div[@role='menu']//span[1]")
                        )
                    ).click()
                except Exception:
                    pass
            else:
                WebDriverWait(context.driver, 4).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//div[@role='menu']//span[1]")
                    )
                ).click()
            found = True
        except Exception:
            pass
        # --- Coba input text manual jika bukan dropdown ---
        if not found:
            try:
                input_xpath = f"//label[contains(.,'{label}')]/following-sibling::input | //span[contains(text(),'{label}')]/parent::label/following-sibling::div//input"
                input_box = context.driver.find_element(By.XPATH, input_xpath)
                # Value random dengan Faker untuk Postal Code atau label lain
                if label == "Postal Code":
                    value = fake.postcode()
                else:
                    value = fake.word().upper()
                input_box.clear()
                input_box.send_keys(value)
            except Exception:
                print(f"[WARNING] Field {label} tidak ditemukan!")
        time.sleep(0.3)


    # Next
    context.driver.find_element(By.XPATH, "//button[normalize-space(text())='Next']").click()
    time.sleep(2)


@when('user goes to next company form and fill required fields')
def step_fill_legal_bank(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Next']"))
    ).click()
    time.sleep(2)
    
def robust_select_dropdown_by_index(context, dropdown_xpath, index=0):
    # Klik dropdown
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
    ).click()
    # Tunggu option muncul
    option_xpath = f"//div[@role='menu']//span"
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, option_xpath))
    )
    options = context.driver.find_elements(By.XPATH, option_xpath)
    # Pakai random index (jika available lebih dari 1)
    if options:
        idx = random.randint(0, len(options)-1) if len(options) > 1 else 0
        options[idx].click()
        time.sleep(0.2)
    else:
        raise Exception("No options found in dropdown!")


def input_postal_code_if_input(context, code=""):
    """
    Try to find input for postal code, if exists, fill it.
    """
    # Cari input di bawah label Postal Code
    input_xpaths = [
        "//span[contains(text(),'Postal Code')]/parent::div//input",
        "//label[contains(.,'Postal Code')]/following-sibling::input",
        "//input[contains(@placeholder,'Postal Code')]",
        "//input[@type='text' and (contains(@name, 'postal') or contains(@id, 'postal'))]",
    ]
    for xpath in input_xpaths:
        inputs = context.driver.find_elements(By.XPATH, xpath)
        if inputs:
            inputs[0].clear()
            if not code:
                from faker import Faker
                code = Faker().postcode()
            inputs[0].send_keys(code)
            print("[INFO] Postal Code field detected as input, filled with:", code)
            return True
    return False

# Klik checkbox (custom, radix, role=checkbox)
def click_policy_checkbox(context):
    # Cari tombol yang berperan sebagai checkbox
    checkbox_buttons = context.driver.find_elements(By.XPATH, "//button[@role='checkbox']")
    for btn in checkbox_buttons:
        # Pastikan ini untuk Policy & Terms, cek label di dekatnya
        parent = btn.find_element(By.XPATH, "./ancestor::div[1]")
        if "Policy" in parent.text and "Terms and Conditions" in parent.text:
            # Klik kalau belum dicentang
            aria_checked = btn.get_attribute("aria-checked")
            if aria_checked == "false":
                btn.click()
                print("[INFO] Policy checkbox clicked")
            return True
    print("[WARNING] Policy checkbox not found!")
    return False


@when('user completes branch creation form with dummy data')
def step_fill_branch_form(context):
    branch_name = "HQ Automation"
    context.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Branch Name')]").clear()
    context.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Branch Name')]").send_keys(branch_name)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Input Address']").send_keys("Jl. Automation Cabang")

    # --- Pilih Country random ---
    country = random.choice(COUNTRY_LIST)
    robust_select_dropdown_option(
        context,
        "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Country')])]",
        country
    )

    if country == "Philippines":
        region = random.choice(PHILIPPINES_REGIONS)
        robust_select_dropdown_option(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Region')])]", region)
        robust_select_dropdown_by_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Province')])]")
        robust_select_dropdown_by_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'City')])]")
        robust_select_dropdown_by_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Barangay')])]")
        # POSTAL CODE: Input bukan dropdown!
        if not input_postal_code_if_input(context):
            print("[WARNING] Postal Code input not found! Skipped.")
    elif country == "Malaysia":
        state = random.choice(MALAYSIA_STATES)
        robust_select_dropdown_option(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'State')])]", state)
        robust_select_dropdown_by_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'City')])]")
        robust_select_dropdown_by_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Location')])]")
        robust_select_dropdown_by_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Postal Code')])]")
    elif country == "Indonesia":
        province = random.choice(INDONESIA_PROVINCES)
        robust_select_dropdown_option(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Province')])]", province)
        robust_select_dropdown_by_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'City')])]")
        robust_select_dropdown_by_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'District')])]")
        robust_select_dropdown_by_index(context, "//button[@role='combobox' and @aria-haspopup='menu' and (span[contains(text(),'Sub District')])]")
        # POSTAL CODE: Input bukan dropdown!
        if not input_postal_code_if_input(context):
            print("[WARNING] Postal Code input not found! Skipped.")

    # Checkbox Policy
    click_policy_checkbox(context)

    register_btn = context.driver.find_element(By.XPATH, "//button[contains(., 'Register')]")
    
    # --- [Tambahkan scroll ke tombol Register]
    context.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", register_btn)
    time.sleep(0.5)  # opsional: beri waktu sebentar setelah scroll

    register_btn.click()
    time.sleep(4)

@then('user should see new company on Companies page')
def step_see_new_company(context):
    WebDriverWait(context.driver, 20).until(
        EC.url_contains("/companies")
    )
    found = False
    # Cari semua card company
    cards = context.driver.find_elements(
        By.XPATH,
        "//div[contains(@class, 'rounded-lg') and contains(@class, 'bg-card') and contains(@class, 'flex-col')]"
    )
    for card in cards:
        # Cari nama company di dalam card
        name_els = card.find_elements(
            By.XPATH, ".//div[contains(@class,'text-lg') and contains(@class,'font-bold')]"
        )
        for name_el in name_els:
            if context.fake_company in name_el.text:
                found = True
                break
        if found:
            break
    assert found, f"New company '{context.fake_company}' not found on Companies page"

