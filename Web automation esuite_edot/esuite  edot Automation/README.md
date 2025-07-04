# 🧪 esuite.edot.id Pytest BDD Test

## 🚀 Behave (BDD) + Selenium WebDriver Automation for esuite.edot.id

Proyek ini adalah **automation testing** untuk [esuite.edot.id](https://esuite.edot.id) dengan:

* **Behave** (Gherkin/BDD)
* **Selenium WebDriver** untuk automation browser (Chrome)
* **Faker** untuk dummy data
* **Tanpa Page Object Pattern** (semua di `steps/`)

---

## 🗂️ Struktur Folder

```
ESUITE_EDOT_BDD/
├── features/
│   ├── steps/
│   │   ├── step_create_company.py         # Step: create company 
│   │   ├── step_verify_company.py         # Step: verifikasi detail company (cek data benar di detail)
│   │   ├── step_oidc.py                   # Step: OIDC login (positive & negative)
│   ├── create_company.feature             # Feature: skenario create company
│   ├── oidc_login.feature                 # Feature: skenario login OIDC
│   └── verify_company_detail.feature      # Feature: verifikasi detail company yang sudah dibuat
├── venv/                                  # Python virtualenv
├── requirements.txt                       # Daftar dependensi
├── .gitignore
└── README.md
```

---

## ⚙️ Cara Menjalankan Automation

### 1. **Clone repositori**

```bash
git clone https://github.com/devoav1997/multi-platform-automation-esuite-ework.git
cd ESUITE_EDOT_BDD
```

### 2. Setup & Persiapan

Sebelum menjalankan test, **lakukan setup virtual environment** dan install semua dependency berikut:

```bash
# Pastikan sudah di folder project
deactivate  # Kalau venv masih aktif
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. **Jalankan Semua Test**

```bash
behave
```

### 4. **Jalankan Hanya Create Company**

```bash
behave features/create_company.feature
```

### 5. **Jalankan Hanya OIDC Login**

```bash
behave features/oidc_login.feature
```

### 6. **Jalankan Verify Company Detail**

```bash
behave features/verify_company_detail.feature
```

---

## ✅ Skenario yang Diuji

### 1. **Login OIDC (Positive & Negative)**

* **Login valid:**

  * Username & password benar, redirect ke dashboard.
* **Login negative:**

  * Username benar, password salah → muncul error.
  * Username salah, password benar → muncul error.
  * Username/password kosong → muncul error.

### 2. **Create Company**

* Navigasi menu "Companies" setelah login
* Klik "+ Add Company"
* Isi form perusahaan dengan data random (Faker)
* Dropdown otomatis menyesuaikan country:

  * **Indonesia:** province, city, district, sub-district, postal code (input, bukan dropdown)
  * **Malaysia:** state, city, location, postal code (dropdown)
  * **Philippines:** region, province, city, barangay, postal code (input)
* Cek dan isi **checkbox Policy & Terms**
* Klik tombol Register
* Validasi perusahaan yang baru dibuat muncul di daftar Companies

### 3. **Verify Company Detail**

* **Tujuan:**
  Memastikan seluruh data perusahaan yang telah diinput muncul **lengkap & benar** di halaman detail.
* **Langkah utama:**

  * Klik tombol "Manage" pada company yang baru dibuat
  * Pastikan seluruh field (company name, industry type, company type, country, province, city, district, subdistrict, postal code, email, phone, address) **sesuai** dengan data saat pembuatan
  * Handle jika data terpotong/ellipsis (misal: `Entertainment and Me...` tetap lolos asalkan mengandung expected value)
* **Contoh Gherkin:**

  ```gherkin
  Scenario: Confirm that the inputted company data is displayed correctly
    Given user is logged in to esuite
    When user creates a new company with dummy data
    Then user should see the new company listed on Companies page
    And user can view company details and see all inputted data correctly
  ```

### 4. **Validasi Error Otomatis**

* Jika terjadi error/validasi form (misal field required belum diisi), automation akan print pesan error yang muncul (jika ada) ke terminal.

---

## 📝 Contoh Menjalankan Satu Skenario (Verify Company Detail)

```bash
behave features/verify_company_detail.feature
```

* **Step ini:**

  * Otomatis login ke aplikasi
  * Tambah company baru dengan data acak
  * Submit form
  * Verifikasi nama company muncul di list
  * Buka detail company dan cek seluruh field **match** dengan data inputan

---

## 📦 Requirements

* Python 3.10+
* Google Chrome
* ChromeDriver (auto-install dengan webdriver-manager)
* Behave
* Selenium
* Faker

**Contoh isi minimum `requirements.txt`:**

```
selenium
behave
webdriver-manager
faker
```

---

## 📚 Tools yang Digunakan

* **Behave** – Framework BDD (Given-When-Then)
* **Selenium WebDriver** – Otomasi browser
* **webdriver-manager** – Auto-download driver Chrome
* **Faker** – Generate data dummy/random
* **Python** – Bahasa scripting utama

