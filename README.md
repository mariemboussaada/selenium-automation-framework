# 🧪 Selenium Automation Framework

![Tests](https://github.com/mariemboussaada/selenium-automation-framework/actions/workflows/test.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

End-to-end test automation framework for [SauceDemo](https://www.saucedemo.com) built with Python & Selenium.

---

## 📊 Live Test Report
🔗 [View Allure Report](https://mariemboussaada.github.io/selenium-automation-framework/)

---

## 🏗️ Project Structure
```
selenium-automation-framework/
├── pages/
│   ├── login_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── products_page.py
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_products.py
├── screenshots/        # Auto-generated on failure
├── reports/            # Allure results
├── conftest.py
├── requirements.txt
└── .github/
    └── workflows/
        └── selenium.yml
```

---

## ✅ Test Coverage

| Test | Description | Severity |
|------|-------------|----------|
| `test_login_valid` | Valid user login and redirect | 🔴 Critical |
| `test_login_invalid` | Invalid credentials error message | 🟡 Normal |
| `test_add_to_cart` | Add product and verify cart badge | 🔴 Critical |
| `test_checkout` | Complete checkout flow end-to-end | 🔴 Critical |
| `test_products_display` | Products page loads correctly | 🟡 Normal |

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10 | Programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test framework |
| Allure Report | Test reporting |
| GitHub Actions | CI/CD pipeline |
| Page Object Model | Architecture pattern |

---

## 🚀 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/mariemboussaada/selenium-automation-framework.git
cd selenium-automation-framework
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run tests
```bash
# With Allure report
pytest --alluredir=reports/allure-results -v

# With HTML report
pytest --html=reports/report.html --self-contained-html -v

# Specific browser
pytest --browser=firefox -v

# Specific test
pytest tests/test_login.py -v
```

### 4. View Allure report
```bash
allure serve reports/allure-results
```

---

## 🌐 CI/CD

Tests run automatically on every push to `main` via GitHub Actions.

- ✅ Headless Chrome on Ubuntu
- ✅ Allure report auto-generated
- ✅ Report published to GitHub Pages
- ✅ Screenshots on failure

---

## 📸 Screenshots

Auto-generated in `screenshots/` folder when a test fails :
```
screenshots/
└── test_checkout_20260316_143607.png
```

---

## 👩‍💻 Author

**Mariem Boussaada**
🔗 [LinkedIn](https://www.linkedin.com/in/mariem-boussaada-a24b45264/)
🔗 [GitHub](https://github.com/mariemboussaada)