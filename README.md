# Selenium Automation Framework

Automatisation complète pour [SauceDemo](https://www.saucedemo.com) avec Python & Selenium.

## Fonctionnalités
- Login / Ajout au panier / Checkout
- Gestion des alertes et exceptions
- Captures d’écran en cas d’échec
- Multi-navigateurs (Chrome & Firefox)
- Rapport HTML complet
- CI/CD via GitHub Actions

## Lancer les tests
```bash
pip install -r requirements.txt
pytest --html=reports/report.html --self-contained-html
