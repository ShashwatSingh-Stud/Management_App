<![CDATA[<div align="center">

# 🏦 NeoBank — Bank Account Management System

### Secure · Simple · Swift

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

A lightweight bank account management application with **two interfaces** — a terminal‑based CLI and a sleek, dark‑themed **Streamlit web dashboard**. Create accounts, deposit & withdraw funds, view details, update profiles, and close accounts — all backed by a simple JSON file database.

---

</div>

## 📑 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the CLI](#running-the-cli)
  - [Running the Web Dashboard](#running-the-web-dashboard)
- [Usage Guide](#-usage-guide)
  - [Create Account](#-create-account)
  - [Deposit Money](#-deposit-money)
  - [Withdraw Money](#-withdraw-money)
  - [View Details](#-view-details)
  - [Update Profile](#-update-profile)
  - [Close Account](#-close-account)
- [Architecture](#-architecture)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [Author](#-author)

---

## ✨ Features

| Feature | CLI (`main.py`) | Web UI (`app.py`) |
|---|:---:|:---:|
| Create Account | ✅ | ✅ |
| Deposit Money | ✅ | ✅ |
| Withdraw Money | ✅ | ✅ |
| View Account Details | ✅ | ✅ |
| Update Profile (Name / Email / PIN) | ✅ | ✅ |
| Delete / Close Account | ✅ | ✅ |
| PIN‑based Authentication | ✅ | ✅ |
| Auto‑generated Account Numbers | ✅ | ✅ |
| Age Validation (min 12 years) | ✅ | ✅ |
| Dashboard Metrics (Total Accounts & Deposits) | — | ✅ |
| Dark Glassmorphic UI with Gradient Theme | — | ✅ |

---

## 🛠 Tech Stack

- **Language:** Python 3.8+
- **Web Framework:** [Streamlit](https://streamlit.io/) — for the interactive dashboard
- **Data Storage:** JSON file (`database.json`) — zero‑config, file‑based persistence
- **Fonts:** [Syne](https://fonts.google.com/specimen/Syne) & [DM Mono](https://fonts.google.com/specimen/DM+Mono) (loaded via Google Fonts in the web UI)

---

## 📂 Project Structure

```
Management App/
├── app.py            # Streamlit web dashboard (dark-themed UI)
├── main.py           # Terminal-based CLI application
├── database.json     # JSON file storing all user account data
└── README.md         # Project documentation
```

| File | Description |
|---|---|
| `app.py` | Full‑featured **Streamlit** web application with a premium dark UI, sidebar navigation, custom CSS styling, gradient backgrounds, and real‑time metrics. |
| `main.py` | Object‑oriented **CLI** version using a `Bank` class with methods for every operation, driven by a simple menu loop. |
| `database.json` | Flat JSON array storing user records — each record contains `name`, `age`, `email`, `AccountNo.`, `pin`, and `Balance`. |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8** or higher installed on your system
- **pip** (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/Management-App.git
   cd Management-App
   ```

2. **Install dependencies**

   ```bash
   pip install streamlit
   ```

   > The CLI (`main.py`) uses only the Python standard library — no extra packages needed.

### Running the CLI

```bash
python main.py
```

You will be presented with a numbered menu:

```
press 1 for Creating an account
press 2 for Depositing money
press 3 for Withdraw Money
press 4 for Details of an user
press 5 for updating users details
press 6 for deleting user
press 0 for exit
```

### Running the Web Dashboard

```bash
streamlit run app.py
```

The app will launch in your default browser at **http://localhost:8501**.

---

## 📖 Usage Guide

### ⊕ Create Account

Provide your **name**, **age**, **email**, and a **4‑digit PIN** (1000–9999). The system auto‑generates a unique alphanumeric account number. Minimum age requirement is **12 years**.

### ↑ Deposit Money

Authenticate with your **account number** and **PIN**, then enter the amount to deposit. Your updated balance is displayed instantly.

### ↓ Withdraw Money

Authenticate and enter the withdrawal amount. The system checks for **insufficient balance** and prevents overdrafts.

### ◈ View Details

Authenticate to view your complete profile — name, email, age, account number, and current balance.

### ✎ Update Profile

Change your **name**, **email**, or **PIN** after authentication. Leave fields blank to keep existing values unchanged.

### ⊗ Close Account

Permanently delete your account after authentication. Requires explicit confirmation. **This action is irreversible.**

---

## 🏗 Architecture

```
┌───────────────────────────────────────────────────┐
│                   User Interface                  │
│                                                   │
│   ┌─────────────────┐   ┌──────────────────────┐  │
│   │   CLI (main.py) │   │  Web UI (app.py)     │  │
│   │   Terminal Menu  │   │  Streamlit Dashboard │  │
│   └────────┬────────┘   └──────────┬───────────┘  │
│            │                       │              │
│            └───────────┬───────────┘              │
│                        │                          │
│              ┌─────────▼─────────┐                │
│              │   Bank Logic      │                │
│              │   (Python)        │                │
│              │                   │                │
│              │  • Account Gen    │                │
│              │  • PIN Auth       │                │
│              │  • CRUD Ops       │                │
│              └─────────┬─────────┘                │
│                        │                          │
│              ┌─────────▼─────────┐                │
│              │  database.json    │                │
│              │  (JSON File DB)   │                │
│              └───────────────────┘                │
└───────────────────────────────────────────────────┘
```

### Data Model

Each user record stored in `database.json` follows this schema:

```json
{
  "name": "string",
  "age": 12,
  "email": "user@example.com",
  "AccountNo.": "aB3d9Kz2",
  "pin": 1234,
  "Balance": 0
}
```

---

## 🖼 Screenshots

> **Web Dashboard** — Launch with `streamlit run app.py`

| Create Account | Deposit Funds | Account Details |
|:---:|:---:|:---:|
| Dark‑themed form with auto‑generated account badge | Gradient balance display after successful deposit | Full profile card with balance highlight |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** this repository
2. **Create** a feature branch — `git checkout -b feature/your-feature`
3. **Commit** your changes — `git commit -m "Add your feature"`
4. **Push** to the branch — `git push origin feature/your-feature`
5. **Open** a Pull Request

### Ideas for Improvement

- [ ] Add transaction history / ledger
- [ ] Implement password hashing for PINs
- [ ] Migrate from JSON to SQLite / PostgreSQL
- [ ] Add fund transfer between accounts
- [ ] Deploy the Streamlit app to Streamlit Cloud

---

## 👤 Author

**Deepak**

---

<div align="center">

Made with ❤️ using Python & Streamlit

</div>
]]>
