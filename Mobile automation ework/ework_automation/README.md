Tentu, berikut contoh **README.md** yang cocok untuk project automation mobile menggunakan **pytest + Appium + Python**.
Bisa kamu copy langsung, nanti tinggal ganti detail app dan test jika mau.

---

````markdown
# Ework Mobile Automation Testing

Automation testing untuk aplikasi **Ework** berbasis Android menggunakan **pytest** dan **Appium**.

---

## 📦 Prerequisites

Pastikan kamu sudah install berikut di Mac:

- **Python 3.9+** (direkomendasikan, tes kamu pakai 3.13 juga boleh)
- **Java JDK** (untuk Appium & Android Emulator)
- **Node.js & NPM** (untuk Appium)
- **Android Studio & Android Emulator**
- **Appium server**

---

## 🛠️ Setup Environment

1. **Clone repo**

    ```sh
    git clone <url-repo-ini>
    cd ework_automation
    ```

2. **Buat dan aktifkan virtualenv**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**

    ```sh
    pip install -r requirements.txt
    ```

    **Contoh `requirements.txt`:**
    ```
    pytest
    Appium-Python-Client
    selenium
    ```

4. **Install & Start Appium Server**

    - Install Appium via npm:
      ```sh
      npm install -g appium
      ```
    - Jalankan Appium server:
      ```sh
      appium
      ```
    - Default listen: `http://localhost:4723`

5. **Siapkan Emulator & APK**

    - Pastikan emulator aktif dan ready (misal: `emulator-5554`).
    - Pastikan file APK sudah ada, misal: `/Users/devo/Downloads/ework 1.20.5.apk`.

---

## 🚀 Cara Menjalankan Test

1. **Aktifkan virtualenv** (jika belum):
    ```sh
    source venv/bin/activate
    ```

2. **Pastikan Appium server sudah jalan**  
   Cek di terminal:
   ```sh
   appium
````

3. **Jalankan test dengan pytest**

   ```sh
   pytest steps/test_login_steps.py -v
   ```

   Atau untuk semua test:

   ```sh
   pytest -v
   ```

---

## ⚙️ Struktur Project

```
EWORK_AUTOMATION/
│
├── features/
│   ├── create_customer.feature
│   └── login.feature
│
├── pages/
│   ├── customer_page.py
│   └── login_page.py
│
├── steps/
│   ├── test_create_customer_steps.py
│   └── test_login_steps.py
│
├── venv/
├── conftest.py
├── requirements.txt
└── README.md

```

---

## ⚡ Troubleshooting

* **Emulator tidak terdeteksi**
  Pastikan sudah jalan (`adb devices` cek muncul device/emulator).

* **Appium server error**
  Pastikan port 4723 tidak dipakai app lain, dan versi Appium sesuai kebutuhan Android.

* **NoSuchElementException**
  Periksa selector element di kode test, bisa juga tambahkan explicit wait.

* **APK tidak terbuka**
  Pastikan path APK benar, app compatible dengan emulator.

---

## 📚 Referensi

* [Appium Python Client](https://github.com/appium/python-client)
* [Pytest Documentation](https://docs.pytest.org/)
* [Appium Documentation](https://appium.io/docs/en/about-appium/intro/)

