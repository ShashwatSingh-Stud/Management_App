import json
import random
import string
from pathlib import Path

import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NeoBank",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

/* ── Reset & base ── */
html, body, [class*="css"] {
    font-family: 'DM Mono', monospace;
    background-color: #090c10;
    color: #e8eaf0;
}

/* ── Animated gradient background ── */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse 80% 60% at 10% 0%, #0d2340 0%, transparent 60%),
                radial-gradient(ellipse 60% 50% at 90% 100%, #0a1f36 0%, transparent 60%),
                #090c10;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1220 0%, #0d1829 100%) !important;
    border-right: 1px solid #1a2840;
}

/* ── Sidebar header ── */
.sidebar-brand {
    font-family: 'Syne', sans-serif;
    font-size: 1.9rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
}
.sidebar-tagline {
    font-size: 0.68rem;
    color: #4a6080;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 2rem;
}

/* ── Nav buttons in sidebar ── */
div[data-testid="stSidebarContent"] .stButton > button {
    width: 100%;
    text-align: left;
    background: transparent;
    border: 1px solid #1a2840;
    color: #8ba0c0;
    font-family: 'DM Mono', monospace;
    font-size: 0.82rem;
    letter-spacing: 0.06em;
    padding: 0.65rem 1rem;
    border-radius: 8px;
    margin-bottom: 0.4rem;
    transition: all 0.2s ease;
}
div[data-testid="stSidebarContent"] .stButton > button:hover {
    background: #0f2033;
    border-color: #38bdf8;
    color: #e0f0ff;
    box-shadow: 0 0 12px rgba(56,189,248,0.15);
}

/* ── Main page buttons ── */
[data-testid="stMain"] .stButton > button {
    background: linear-gradient(135deg, #1a78c2 0%, #2e4fd6 100%);
    color: #fff;
    font-family: 'DM Mono', monospace;
    font-size: 0.82rem;
    letter-spacing: 0.08em;
    border: none;
    border-radius: 8px;
    padding: 0.6rem 1.8rem;
    transition: all 0.25s ease;
    box-shadow: 0 4px 18px rgba(30,120,200,0.25);
}
[data-testid="stMain"] .stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 28px rgba(30,120,200,0.4);
}

/* ── Inputs ── */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input {
    background: #0d1829 !important;
    border: 1px solid #1e3050 !important;
    border-radius: 8px !important;
    color: #c8d8f0 !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.85rem !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stNumberInput"] input:focus {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 0 2px rgba(56,189,248,0.12) !important;
}
label {
    color: #6888a8 !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
}

/* ── Metric cards ── */
[data-testid="metric-container"] {
    background: #0d1829;
    border: 1px solid #1a2840;
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
}
[data-testid="metric-container"] [data-testid="stMetricLabel"] {
    color: #4a6080 !important;
    font-size: 0.72rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.8rem !important;
    color: #38bdf8 !important;
}

/* ── Success / Warning / Error alerts ── */
[data-testid="stAlert"] {
    border-radius: 10px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.82rem !important;
}

/* ── Dividers ── */
hr { border-color: #1a2840; }

/* ── Section heading ── */
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    margin-bottom: 0.2rem;
}
.section-sub {
    font-size: 0.72rem;
    color: #4a6080;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 1.8rem;
}

/* ── Card container ── */
.card {
    background: #0d1829;
    border: 1px solid #1a2840;
    border-radius: 14px;
    padding: 1.8rem;
    margin-bottom: 1.2rem;
}

/* ── Account badge ── */
.acc-badge {
    display: inline-block;
    background: linear-gradient(135deg, #0a2040 0%, #0f2a50 100%);
    border: 1px solid #1e4070;
    border-radius: 8px;
    padding: 0.4rem 1rem;
    font-family: 'DM Mono', monospace;
    font-size: 1.1rem;
    letter-spacing: 0.18em;
    color: #38bdf8;
    margin-top: 0.6rem;
    word-break: break-all;
}

/* ── Balance highlight ── */
.balance-big {
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* ── User detail table ── */
.detail-row {
    display: flex;
    justify-content: space-between;
    padding: 0.6rem 0;
    border-bottom: 1px solid #1a2840;
    font-size: 0.85rem;
}
.detail-key { color: #4a6080; letter-spacing: 0.08em; text-transform: uppercase; font-size: 0.72rem; }
.detail-val { color: #c8d8f0; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #090c10; }
::-webkit-scrollbar-thumb { background: #1a2840; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)


# ── Backend logic (unchanged from original) ───────────────────────────────────
DATABASE = "database.json"

def _load():
    if Path(DATABASE).exists():
        with open(DATABASE) as f:
            return json.loads(f.read())
    return []

def _save(data):
    with open(DATABASE, "w") as f:
        f.write(json.dumps(data, indent=2))

def _gen_acc():
    alpha = random.choices(string.ascii_letters, k=4)
    num   = random.choices(string.digits, k=4)
    acc   = alpha + num
    random.shuffle(acc)
    return "".join(acc)

def _find_user(data, accno, pin):
    return [u for u in data if u["AccountNo."] == accno and u["pin"] == pin]


# ── Session init ──────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "create"


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-brand">NeoBank</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-tagline">Secure · Simple · Swift</div>', unsafe_allow_html=True)

    pages = {
        "create":   "⊕  Create Account",
        "deposit":  "↑  Deposit Money",
        "withdraw": "↓  Withdraw Money",
        "details":  "◈  View Details",
        "update":   "✎  Update Profile",
        "delete":   "⊗  Close Account",
    }
    for key, label in pages.items():
        if st.button(label, key=f"nav_{key}"):
            st.session_state.page = key

    st.markdown("---")
    data = _load()
    st.metric("Total Accounts", len(data))
    total_bal = sum(u.get("Balance", 0) for u in data)
    st.metric("Total Deposits", f"₹{total_bal:,.0f}")


# ── Helper: auth form ─────────────────────────────────────────────────────────
def auth_form():
    col1, col2 = st.columns(2)
    with col1:
        accno = st.text_input("Account Number", placeholder="e.g. aB3d9Kz2")
    with col2:
        pin = st.number_input("PIN", min_value=0, max_value=9999, step=1,
                              format="%d", value=0)
    return accno.strip(), int(pin)


# ── Pages ─────────────────────────────────────────────────────────────────────
page = st.session_state.page

# ── CREATE ────────────────────────────────────────────────────────────────────
if page == "create":
    st.markdown('<div class="section-title">Open New Account</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Join NeoBank — takes 30 seconds</div>', unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            name  = st.text_input("Full Name", placeholder="Shashwat Sharma")
            email = st.text_input("Email Address", placeholder="you@example.com")
        with col2:
            age = st.number_input("Age", min_value=0, max_value=120, value=18)
            pin = st.number_input("Set 4-digit PIN", min_value=0, max_value=9999,
                                  step=1, format="%d", value=1234)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Create Account →"):
            if age < 12:
                st.error("❌ Minimum age to open an account is 12 years.")
            elif len(str(pin)) != 4 or pin < 1000:
                st.error("❌ PIN must be exactly 4 digits (1000–9999).")
            elif not name or not email:
                st.error("❌ Name and email cannot be empty.")
            else:
                data  = _load()
                accno = _gen_acc()
                data.append({
                    "name": name,
                    "age":  age,
                    "email": email,
                    "AccountNo.": accno,
                    "pin": pin,
                    "Balance": 0,
                })
                _save(data)
                st.success("✅ Account created successfully!")
                st.markdown(f"""
                <div class="card">
                    <div style="color:#4a6080;font-size:0.72rem;letter-spacing:.1em;text-transform:uppercase">
                        Your Account Number
                    </div>
                    <div class="acc-badge">{accno}</div>
                    <div style="margin-top:.8rem;color:#4a6080;font-size:0.75rem">
                        Save this number — you'll need it for all transactions.
                    </div>
                </div>
                """, unsafe_allow_html=True)

# ── DEPOSIT ───────────────────────────────────────────────────────────────────
elif page == "deposit":
    st.markdown('<div class="section-title">Deposit Funds</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Add money to your account</div>', unsafe_allow_html=True)

    accno, pin = auth_form()
    amount = st.number_input("Amount to Deposit (₹)", min_value=1, value=500, step=100)

    if st.button("Deposit →"):
        data  = _load()
        users = _find_user(data, accno, pin)
        if not users:
            st.error("❌ Invalid account number or PIN.")
        else:
            users[0]["Balance"] += amount
            _save(data)
            st.success(f"✅ ₹{amount:,.0f} deposited successfully!")
            st.markdown(f"""
            <div class="card">
                <div style="color:#4a6080;font-size:0.72rem;letter-spacing:.1em;text-transform:uppercase">Updated Balance</div>
                <div class="balance-big">₹{users[0]['Balance']:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)

# ── WITHDRAW ──────────────────────────────────────────────────────────────────
elif page == "withdraw":
    st.markdown('<div class="section-title">Withdraw Funds</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Transfer money out of your account</div>', unsafe_allow_html=True)

    accno, pin = auth_form()
    amount = st.number_input("Amount to Withdraw (₹)", min_value=1, value=100, step=50)

    if st.button("Withdraw →"):
        data  = _load()
        users = _find_user(data, accno, pin)
        if not users:
            st.error("❌ Invalid account number or PIN.")
        elif amount > users[0]["Balance"]:
            st.warning(f"⚠️ Insufficient balance. Available: ₹{users[0]['Balance']:,.0f}")
        else:
            users[0]["Balance"] -= amount
            _save(data)
            st.success(f"✅ ₹{amount:,.0f} withdrawn successfully!")
            st.markdown(f"""
            <div class="card">
                <div style="color:#4a6080;font-size:0.72rem;letter-spacing:.1em;text-transform:uppercase">Remaining Balance</div>
                <div class="balance-big">₹{users[0]['Balance']:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)

# ── DETAILS ───────────────────────────────────────────────────────────────────
elif page == "details":
    st.markdown('<div class="section-title">Account Details</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">View your profile & balance</div>', unsafe_allow_html=True)

    accno, pin = auth_form()

    if st.button("Fetch Details →"):
        data  = _load()
        users = _find_user(data, accno, pin)
        if not users:
            st.error("❌ No account found with these credentials.")
        else:
            u = users[0]
            st.markdown(f"""
            <div class="card">
                <div class="balance-big">₹{u['Balance']:,.0f}</div>
                <div style="color:#4a6080;font-size:0.72rem;letter-spacing:.1em;margin-bottom:1.4rem">CURRENT BALANCE</div>
                <div class="detail-row"><span class="detail-key">Name</span><span class="detail-val">{u['name']}</span></div>
                <div class="detail-row"><span class="detail-key">Email</span><span class="detail-val">{u['email']}</span></div>
                <div class="detail-row"><span class="detail-key">Age</span><span class="detail-val">{u['age']} yrs</span></div>
                <div class="detail-row"><span class="detail-key">Account No.</span><span class="detail-val">{u['AccountNo.']}</span></div>
            </div>
            """, unsafe_allow_html=True)

# ── UPDATE ────────────────────────────────────────────────────────────────────
elif page == "update":
    st.markdown('<div class="section-title">Update Profile</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Change name, email or PIN</div>', unsafe_allow_html=True)

    accno, pin = auth_form()
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        new_name  = st.text_input("New Name", placeholder="Leave blank to keep")
    with col2:
        new_email = st.text_input("New Email", placeholder="Leave blank to keep")
    with col3:
        new_pin   = st.number_input("New PIN (4-digit)", min_value=0, max_value=9999,
                                    step=1, format="%d", value=0)

    if st.button("Save Changes →"):
        data  = _load()
        users = _find_user(data, accno, pin)
        if not users:
            st.error("❌ Invalid account number or PIN.")
        else:
            u = users[0]
            if new_name.strip():
                u["name"] = new_name.strip()
            if new_email.strip():
                u["email"] = new_email.strip()
            if new_pin >= 1000:
                if len(str(new_pin)) != 4:
                    st.error("❌ New PIN must be exactly 4 digits.")
                    st.stop()
                u["pin"] = new_pin
            _save(data)
            st.success("✅ Profile updated successfully!")

# ── DELETE ────────────────────────────────────────────────────────────────────
elif page == "delete":
    st.markdown('<div class="section-title">Close Account</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">This action is permanent</div>', unsafe_allow_html=True)

    st.warning("⚠️ Closing your account will permanently delete all data and forfeit your remaining balance.")

    accno, pin = auth_form()
    confirm = st.checkbox("I understand this cannot be undone")

    if st.button("Close Account →"):
        if not confirm:
            st.error("❌ Please check the confirmation box first.")
        else:
            data  = _load()
            users = _find_user(data, accno, pin)
            if not users:
                st.error("❌ Invalid account number or PIN.")
            else:
                data.remove(users[0])
                _save(data)
                st.success("✅ Account closed. We're sorry to see you go.")