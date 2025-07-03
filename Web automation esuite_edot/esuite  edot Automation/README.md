Tentu, berikut **README.md** yang sudah **diperbaiki** dan lebih jelas (step-by-step) untuk menjalankan automation **create company** di project-mu, plus penjelasan ringkas tentang tiap skenario:

---

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
│   │   ├── step_create_company.py     # Step definition: create company (positive, negative, dan error form)
│   │   └── step_oidc.py               # Step definition: OIDC login (positive & negative)
│   ├── create_company.feature         # Feature file: skenario create company
│   └── oidc_login.feature             # Feature file: skenario login OIDC
├── venv/                              # Python virtualenv
├── requirements.txt                   # Daftar dependensi
├── .gitignore
└── README.md
```

---

## ⚙️ Cara Menjalankan Automation

### 1. **Clone repositori**

```bash
git clone <url-repo-kamu>
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
* Dropdown akan otomatis menyesuaikan country:

  * **Indonesia:** province, city, district, sub-district, postal code (input, bukan dropdown)
  * **Malaysia:** state, city, location, postal code (dropdown)
  * **Philippines:** region, province, city, barangay, postal code (input)
* Cek dan isi **checkbox Policy & Terms** (custom, role=checkbox)
* Klik tombol Register
* Validasi bahwa perusahaan yang baru dibuat muncul di daftar Companies

### 3. **Validasi Error Otomatis**

* Jika terjadi error/validasi form (misal field required belum diisi), automation akan print pesan error yang muncul (jika ada) ke terminal.

---

## 📝 Contoh Menjalankan Satu Skenario (Create Company)

```bash
behave features/create_company.feature
```

* **Step ini:**

  * Otomatis login ke aplikasi
  * Navigasi ke menu "Companies"
  * Tambah company baru dengan data acak
  * Isi seluruh field sesuai negara (Indonesia/Malaysia/Philippines)
  * Submit form
  * Verifikasi nama company muncul di list
  * Jika form error, otomatis print pesan error yang muncul

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

