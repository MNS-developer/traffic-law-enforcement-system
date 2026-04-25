import streamlit as st
import time
from datetime import datetime

st.set_page_config(
    page_title="Punjab Traffic Law Enforcement System",
    page_icon="🚔",
    layout="wide"
)

# ─────────────────────────────────────────────────────────────────
# DARK THEME CSS  –  official / government  +  dark navy aesthetic
# ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&family=Barlow:wght@300;400;500;600&display=swap');

/* ── base ── */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #080d18 !important;
    color: #c9d6e3 !important;
    font-family: 'Barlow', sans-serif;
}
[data-testid="stSidebar"] { display: none; }
[data-testid="stHeader"]  { background: transparent !important; }

.block-container { padding: 1.5rem 2rem 3rem !important; max-width: 1280px !important; }

/* scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0d1526; }
::-webkit-scrollbar-thumb { background: #f59e0b; border-radius: 3px; }

/* ── header banner ── */
.hdr-wrap {
    background: linear-gradient(135deg, #0d1e3d 0%, #0a1628 60%, #0d1526 100%);
    border: 1px solid #1e3a5f;
    border-radius: 16px;
    padding: 2.4rem 2.8rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hdr-wrap::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 240px; height: 240px;
    background: radial-gradient(circle, rgba(245,158,11,0.12) 0%, transparent 70%);
    border-radius: 50%;
}
.hdr-wrap::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, #f59e0b, #ef4444, #f59e0b, transparent);
}
.hdr-seal { font-size: 3.5rem; }
.hdr-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 2.4rem;
    font-weight: 700;
    color: #f8f4ec;
    letter-spacing: 1px;
    line-height: 1.1;
}
.hdr-subtitle {
    font-size: 0.85rem;
    color: #64748b;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 0.4rem;
}
.hdr-badge {
    background: rgba(245,158,11,0.15);
    border: 1px solid #f59e0b;
    color: #f59e0b;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    padding: 3px 10px;
    border-radius: 4px;
    letter-spacing: 2px;
    display: inline-block;
    margin-top: 0.6rem;
}
.hdr-meta {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.72rem;
    color: #475569;
    text-align: right;
}

/* ── section cards ── */
.sec-card {
    background: #0d1829;
    border: 1px solid #1a2e4a;
    border-radius: 12px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.4rem;
    position: relative;
}
.sec-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 4px; height: 100%;
    background: linear-gradient(180deg, #f59e0b, #b45309);
    border-radius: 12px 0 0 12px;
}
.sec-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: #f59e0b;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 1.2rem;
    padding-bottom: 0.7rem;
    border-bottom: 1px solid #1e3a5f;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* ── selectbox / number_input theming ── */
.stSelectbox > div > div, .stNumberInput > div > div > input {
    background: #0a1628 !important;
    border: 1px solid #1e3a5f !important;
    color: #c9d6e3 !important;
    border-radius: 8px !important;
}
.stSelectbox label, .stNumberInput label { color: #8ea5bf !important; font-size: 0.85rem !important; }

/* ── analyze button ── */
.stButton > button {
    background: linear-gradient(135deg, #b45309, #f59e0b) !important;
    color: #0a0e1a !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1.25rem !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.7rem 2rem !important;
    text-transform: uppercase !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 20px rgba(245,158,11,0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(245,158,11,0.5) !important;
}

/* ── result tables ── */
.viol-table { width:100%; border-collapse:collapse; margin: 1rem 0; }
.viol-table th {
    background: #0d1e3d;
    color: #f59e0b;
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.85rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 12px 14px;
    border-bottom: 2px solid #f59e0b;
    text-align: left;
}
.viol-table td { padding: 11px 14px; border-bottom: 1px solid #1a2e4a; font-size: 0.9rem; }
.sev-critical { background: rgba(239,68,68,0.12) !important; }
.sev-high     { background: rgba(245,158,11,0.10) !important; }
.sev-medium   { background: rgba(234,179,8,0.08) !important; }
.sev-low      { background: rgba(34,197,94,0.06) !important; }
.badge-critical { display:inline-block; background:#ef4444; color:#fff; font-size:0.65rem; padding:2px 7px; border-radius:3px; font-family:'Share Tech Mono',monospace; letter-spacing:1px; }
.badge-high     { display:inline-block; background:#f59e0b; color:#000; font-size:0.65rem; padding:2px 7px; border-radius:3px; font-family:'Share Tech Mono',monospace; letter-spacing:1px; }
.badge-medium   { display:inline-block; background:#eab308; color:#000; font-size:0.65rem; padding:2px 7px; border-radius:3px; font-family:'Share Tech Mono',monospace; letter-spacing:1px; }
.badge-low      { display:inline-block; background:#22c55e; color:#000; font-size:0.65rem; padding:2px 7px; border-radius:3px; font-family:'Share Tech Mono',monospace; letter-spacing:1px; }

/* ── fine card ── */
.fine-card {
    background: linear-gradient(135deg, #1a0a00 0%, #2d1200 50%, #1a0a00 100%);
    border: 2px solid #f59e0b;
    border-radius: 16px;
    padding: 2.4rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin: 1.5rem 0;
}
.fine-card::before {
    content: '';
    position: absolute;
    top: -40px; left: 50%;
    transform: translateX(-50%);
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(245,158,11,0.15) 0%, transparent 70%);
}
.fine-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.8rem;
    color: #78350f;
    letter-spacing: 4px;
    text-transform: uppercase;
}
.fine-amount {
    font-family: 'Rajdhani', sans-serif;
    font-size: 4rem;
    font-weight: 700;
    color: #f59e0b;
    line-height: 1.1;
    text-shadow: 0 0 30px rgba(245,158,11,0.5);
}
.fine-currency {
    font-family: 'Share Tech Mono', monospace;
    font-size: 1rem;
    color: #b45309;
    margin-right: 0.4rem;
    vertical-align: super;
}
.fine-meta { color: #92400e; font-size: 0.9rem; margin-top: 0.8rem; }

/* ── status badges ── */
.status-clear {
    background: rgba(34,197,94,0.1);
    border: 1px solid #22c55e;
    color: #86efac;
    border-radius: 12px;
    padding: 1.6rem;
    text-align: center;
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.5rem;
    font-weight: 600;
}

/* ── info panel ── */
.info-row {
    display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.4rem;
}
.info-chip {
    background: #0d1829;
    border: 1px solid #1a2e4a;
    border-radius: 8px;
    padding: 0.7rem 1rem;
    flex: 1; min-width: 150px;
    font-size: 0.8rem;
}
.info-chip .ic-label { color: #475569; font-size: 0.7rem; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 3px; }
.info-chip .ic-val   { color: #e2e8f0; font-family: 'Share Tech Mono', monospace; }

/* ── risk meter ── */
.risk-bar-wrap { margin: 1.2rem 0; }
.risk-bar-bg   { background: #0a1628; border-radius: 6px; height: 10px; overflow: hidden; border: 1px solid #1e3a5f; }
.risk-bar-fill { height: 100%; border-radius: 6px; transition: width 1s ease; }
.risk-label    { font-family: 'Rajdhani', sans-serif; font-size: 1rem; font-weight: 600; margin-bottom: 5px; }

/* ── breakdown expander ── */
.breakdown-row { display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid #0f1f35; font-size:0.85rem; }
.breakdown-row:last-child { border-bottom: none; }
.breakdown-total { display:flex; justify-content:space-between; padding:12px 0 0; font-family:'Rajdhani',sans-serif; font-size:1.1rem; font-weight:700; color:#f59e0b; border-top: 2px solid #f59e0b; margin-top:8px; }

/* ── streamlit fixes ── */
.stExpander { background: #0d1829 !important; border: 1px solid #1a2e4a !important; border-radius: 10px !important; }
[data-testid="stExpanderToggleIcon"] { color: #f59e0b !important; }
.streamlit-expanderHeader { font-family: 'Barlow', sans-serif !important; color: #94a3b8 !important; }
.stSpinner > div { border-top-color: #f59e0b !important; }

/* ── kb table ── */
.kb-table { width:100%; border-collapse:collapse; font-size:0.82rem; margin-top:0.8rem; }
.kb-table th { background:#0d1e3d; color:#f59e0b; padding:9px 12px; text-align:left; font-family:'Rajdhani',sans-serif; letter-spacing:1.5px; text-transform:uppercase; border-bottom:1px solid #f59e0b; }
.kb-table td { padding:8px 12px; border-bottom:1px solid #111e32; color:#94a3b8; }
.kb-table tr:hover td { background:#0a1628; color:#c9d6e3; }

/* ── footer ── */
.footer { text-align:center; color:#1e3a5f; font-size:0.75rem; margin-top:2.5rem; font-family:'Share Tech Mono',monospace; letter-spacing:1px; }

/* columns label */
div[data-testid="column"] label { color: #8ea5bf !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# KNOWLEDGE BASE  –  Punjab Motor Vehicles Ordinance 1965 + updates
# ─────────────────────────────────────────────────────────────────

RULES = {
    # ── SPEED VIOLATIONS ──
    "overspeed_school": {
        "section": "S.74 MVO",
        "name": "Overspeeding in School Zone",
        "desc": "Speed exceeds 30 km/h limit in school zone",
        "cond": lambda f: f["speed"] > f["limit"] and f["area"] == "School Zone",
        "base_fine": 10000, "severity": "CRITICAL",
        "arrest": False, "points": 4
    },
    "overspeed_residential": {
        "section": "S.74 MVO",
        "name": "Overspeeding in Residential Area",
        "desc": "Speed exceeds prescribed limit in residential zone",
        "cond": lambda f: f["speed"] > f["limit"] and f["area"] == "Residential",
        "base_fine": 5000, "severity": "HIGH",
        "arrest": False, "points": 3
    },
    "overspeed_city": {
        "section": "S.74 MVO",
        "name": "Overspeeding in City Area",
        "desc": "Speed exceeds 60 km/h in city limits",
        "cond": lambda f: f["speed"] > f["limit"] and f["area"] in ["City", "Rural"],
        "base_fine": 3000, "severity": "MEDIUM",
        "arrest": False, "points": 2
    },
    "overspeed_highway": {
        "section": "S.74 MVO",
        "name": "Overspeeding on Highway",
        "desc": "Speed exceeds 100 km/h on highway",
        "cond": lambda f: f["speed"] > f["limit"] and f["area"] == "Highway",
        "base_fine": 4000, "severity": "MEDIUM",
        "arrest": False, "points": 2
    },
    "extreme_overspeed": {
        "section": "S.74-A MVO",
        "name": "Extreme Overspeeding (>40 km/h over limit)",
        "desc": "Reckless speed posing imminent danger to public",
        "cond": lambda f: (f["speed"] - f["limit"]) > 40,
        "base_fine": 20000, "severity": "CRITICAL",
        "arrest": True, "points": 6
    },
    # ── SAFETY ──
    "no_helmet": {
        "section": "S.98-A MVO",
        "name": "Riding Without Helmet",
        "desc": "Two-wheeler rider or pillion without approved helmet",
        "cond": lambda f: f["vehicle"] in ["Motorcycle", "Scooter"] and f["helmet"] == "No",
        "base_fine": 5000, "severity": "HIGH",
        "arrest": False, "points": 3
    },
    "no_seatbelt_driver": {
        "section": "S.98 MVO",
        "name": "Driver Not Wearing Seatbelt",
        "desc": "Driver of four-wheeler not wearing seatbelt",
        "cond": lambda f: f["vehicle"] in ["Car", "Jeep", "Van", "Taxi"] and f["seatbelt"] == "No",
        "base_fine": 5000, "severity": "HIGH",
        "arrest": False, "points": 3
    },
    "overloading": {
        "section": "S.85 MVO",
        "name": "Vehicle Overloading",
        "desc": "Passengers exceed registered seating capacity",
        "cond": lambda f: f["overloading"] == "Yes",
        "base_fine": 10000, "severity": "HIGH",
        "arrest": False, "points": 3
    },
    # ── DOCUMENTS ──
    "no_license": {
        "section": "S.10 MVO",
        "name": "No Valid Driving License",
        "desc": "Driving without a valid license",
        "cond": lambda f: f["license"] == "No",
        "base_fine": 30000, "severity": "CRITICAL",
        "arrest": True, "points": 8
    },
    "expired_license": {
        "section": "S.10 MVO",
        "name": "Expired Driving License",
        "desc": "Driving on an expired license",
        "cond": lambda f: f["license"] == "Expired",
        "base_fine": 15000, "severity": "HIGH",
        "arrest": False, "points": 5
    },
    "no_registration": {
        "section": "S.26 MVO",
        "name": "No / Fake Vehicle Registration",
        "desc": "Vehicle without valid registration certificate",
        "cond": lambda f: f["registration"] in ["No", "Fake"],
        "base_fine": 50000, "severity": "CRITICAL",
        "arrest": True, "points": 10
    },
    "no_insurance": {
        "section": "S.95 MVO",
        "name": "No Third-Party Insurance",
        "desc": "Vehicle not covered by mandatory third-party insurance",
        "cond": lambda f: f["insurance"] == "No",
        "base_fine": 10000, "severity": "HIGH",
        "arrest": False, "points": 4
    },
    "no_fitness": {
        "section": "S.35 MVO",
        "name": "No Fitness / Road-Worthiness Certificate",
        "desc": "Commercial vehicle without valid fitness certificate",
        "cond": lambda f: f["vehicle"] in ["Truck", "Bus"] and f["fitness"] == "No",
        "base_fine": 20000, "severity": "HIGH",
        "arrest": False, "points": 4
    },
    # ── TRAFFIC RULES ──
    "red_light": {
        "section": "S.61 MVO",
        "name": "Jumping Red Light",
        "desc": "Passed through or failed to stop at red traffic signal",
        "cond": lambda f: f["signal"] == "Red",
        "base_fine": 10000, "severity": "HIGH",
        "arrest": False, "points": 4
    },
    "wrong_side": {
        "section": "S.59 MVO",
        "name": "Wrong Side / One-Way Violation",
        "desc": "Driving on wrong side of road or entering one-way street",
        "cond": lambda f: f["wrong_side"] == "Yes",
        "base_fine": 15000, "severity": "CRITICAL",
        "arrest": False, "points": 5
    },
    "mobile_phone": {
        "section": "S.98-B MVO",
        "name": "Using Mobile Phone While Driving",
        "desc": "Holding and operating mobile device while vehicle in motion",
        "cond": lambda f: f["mobile"] == "Yes",
        "base_fine": 5000, "severity": "HIGH",
        "arrest": False, "points": 3
    },
    "no_horn": {
        "section": "S.68 MVO",
        "name": "Illegal Use of Pressure Horn",
        "desc": "Using prohibited air/pressure horn",
        "cond": lambda f: f["pressure_horn"] == "Yes",
        "base_fine": 3000, "severity": "MEDIUM",
        "arrest": False, "points": 1
    },
    "no_indicator": {
        "section": "S.60 MVO",
        "name": "Defective / No Turn Indicators",
        "desc": "Vehicle with non-functional turn signal lights",
        "cond": lambda f: f["indicators"] == "No",
        "base_fine": 2000, "severity": "LOW",
        "arrest": False, "points": 1
    },
    "tinted_glass": {
        "section": "S.108 MVO",
        "name": "Illegal Tinted Windows",
        "desc": "Window tint darker than legally permitted (70% VLT minimum)",
        "cond": lambda f: f["tinted"] == "Yes",
        "base_fine": 5000, "severity": "MEDIUM",
        "arrest": False, "points": 2
    },
    "drunk_driving": {
        "section": "S.126-A MVO + PPC 279",
        "name": "Driving Under Influence (DUI)",
        "desc": "Driver impaired by alcohol or controlled substances",
        "cond": lambda f: f["dui"] == "Yes",
        "base_fine": 50000, "severity": "CRITICAL",
        "arrest": True, "points": 12
    },
    "lane_discipline": {
        "section": "S.63 MVO",
        "name": "Lane Violation",
        "desc": "Changing lanes without signal or improper lane usage",
        "cond": lambda f: f["lane_violation"] == "Yes",
        "base_fine": 3000, "severity": "LOW",
        "arrest": False, "points": 1
    },
    "no_parking": {
        "section": "S.78 MVO",
        "name": "Illegal Parking",
        "desc": "Parking in prohibited zone, blocking traffic or emergency access",
        "cond": lambda f: f["illegal_parking"] == "Yes",
        "base_fine": 3000, "severity": "MEDIUM",
        "arrest": False, "points": 2
    },
    "underage_driving": {
        "section": "S.8 MVO",
        "name": "Underage Driving",
        "desc": "Driver below 18 years of age (16 for motorcycle learner)",
        "cond": lambda f: f["underage"] == "Yes",
        "base_fine": 20000, "severity": "CRITICAL",
        "arrest": True, "points": 8
    },
    "no_number_plate": {
        "section": "S.31 MVO",
        "name": "Tampered / Missing Number Plate",
        "desc": "Vehicle without standard number plate or with altered plates",
        "cond": lambda f: f["number_plate"] in ["Missing", "Tampered"],
        "base_fine": 10000, "severity": "HIGH",
        "arrest": True, "points": 5
    },
    "overloading_goods": {
        "section": "S.85 MVO",
        "name": "Goods Overloading",
        "desc": "Goods vehicle loaded beyond permissible weight limit",
        "cond": lambda f: f["vehicle"] == "Truck" and f["goods_overload"] == "Yes",
        "base_fine": 25000, "severity": "CRITICAL",
        "arrest": False, "points": 5
    },
}

SEV_ORDER = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
SEV_COLOR = {"CRITICAL": "#ef4444", "HIGH": "#f59e0b", "MEDIUM": "#eab308", "LOW": "#22c55e"}
SEV_BADGE = {
    "CRITICAL": '<span class="badge-critical">CRITICAL</span>',
    "HIGH":     '<span class="badge-high">HIGH</span>',
    "MEDIUM":   '<span class="badge-medium">MEDIUM</span>',
    "LOW":      '<span class="badge-low">LOW</span>',
}

def check_violations(facts):
    violations = []
    for key, rule in RULES.items():
        try:
            if rule["cond"](facts):
                violations.append({**rule, "id": key})
        except Exception:
            pass
    violations.sort(key=lambda x: SEV_ORDER[x["severity"]], reverse=True)
    return violations

# ─────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────
defaults = dict(analyzed=False, violations=[], total=0, repeat_add=0, facts={}, arrest=False, points=0)
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ─────────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────────
now = datetime.now()
st.markdown(f"""
<div class="hdr-wrap">
  <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1rem;">
    <div style="display:flex; align-items:center; gap:1.4rem;">
      <div class="hdr-seal">🚔</div>
      <div>
        <div class="hdr-title">Traffic Law Enforcement System</div>
        <div class="hdr-subtitle">Government of Punjab — Motor Vehicles Ordinance 1965</div>
        <div class="hdr-badge">Rule-Based Expert System</div>
      </div>
    </div>
    <div class="hdr-meta">
      SESSION ID: TLE-{now.strftime('%Y%m%d-%H%M')}<br>
      DATE: {now.strftime('%d %b %Y')}<br>
      JURISDICTION: PUNJAB, PAKISTAN
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# INPUTS
# ─────────────────────────────────────────────────────────────────
col_left, col_right = st.columns([3, 2])

with col_left:

    # ── Vehicle & Speed ──
    st.markdown('<div class="sec-card"><div class="sec-title">🚗 Vehicle & Speed</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        vehicle   = st.selectbox("Vehicle Type", ["Car", "Motorcycle", "Scooter", "Jeep", "Van", "Taxi", "Truck", "Bus"])
        speed     = st.number_input("Current Speed (km/h)", 0, 300, 60, step=5)
    with c2:
        area      = st.selectbox("Area Type", ["City", "Residential", "School Zone", "Highway", "Rural"])
        LIMITS    = {"Residential": 40, "School Zone": 30, "Highway": 100, "City": 60, "Rural": 80}
        limit     = st.number_input("Speed Limit (km/h)", 20, 180, LIMITS[area], step=5)
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Safety Equipment ──
    st.markdown('<div class="sec-card"><div class="sec-title">🦺 Safety Equipment</div>', unsafe_allow_html=True)
    c3, c4, c5 = st.columns(3)
    with c3:
        helmet    = st.selectbox("Helmet", ["Yes", "No"]) if vehicle in ["Motorcycle", "Scooter"] else "N/A"
    with c4:
        seatbelt  = st.selectbox("Seatbelt", ["Yes", "No"]) if vehicle in ["Car","Jeep","Van","Taxi","Bus"] else "N/A"
    with c5:
        overloading = st.selectbox("Passenger Overloading", ["No", "Yes"])
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Documents ──
    st.markdown('<div class="sec-card"><div class="sec-title">📋 Documents & Registration</div>', unsafe_allow_html=True)
    c6, c7, c8 = st.columns(3)
    with c6:
        license_     = st.selectbox("Driving License", ["Valid", "No", "Expired"])
    with c7:
        registration = st.selectbox("Registration", ["Valid", "No", "Fake"])
    with c8:
        insurance    = st.selectbox("Insurance", ["Valid", "No"])
    c9, c10 = st.columns(2)
    with c9:
        fitness = st.selectbox("Fitness Certificate", ["Valid", "No"]) if vehicle in ["Truck", "Bus"] else "Valid"
    with c10:
        number_plate = st.selectbox("Number Plate", ["OK", "Missing", "Tampered"])
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Traffic Violations ──
    st.markdown('<div class="sec-card"><div class="sec-title">🚦 Traffic Violations</div>', unsafe_allow_html=True)
    c11, c12 = st.columns(2)
    with c11:
        signal        = st.selectbox("Traffic Signal Status", ["Green", "Yellow", "Red", "None"])
        wrong_side    = st.selectbox("Wrong Side Driving", ["No", "Yes"])
        mobile        = st.selectbox("Mobile Phone While Driving", ["No", "Yes"])
    with c12:
        pressure_horn = st.selectbox("Using Pressure Horn", ["No", "Yes"])
        indicators    = st.selectbox("Turn Indicators Functional", ["Yes", "No"])
        lane_violation= st.selectbox("Lane Violation", ["No", "Yes"])
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Additional Offences ──
    st.markdown('<div class="sec-card"><div class="sec-title">⚠️ Additional Offences</div>', unsafe_allow_html=True)
    c13, c14, c15 = st.columns(3)
    with c13:
        tinted       = st.selectbox("Illegal Tinted Windows", ["No", "Yes"])
        dui          = st.selectbox("DUI / Under Influence", ["No", "Yes"])
    with c14:
        illegal_parking = st.selectbox("Illegal Parking", ["No", "Yes"])
        underage        = st.selectbox("Underage Driver (<18)", ["No", "Yes"])
    with c15:
        goods_overload  = st.selectbox("Goods Overloading", ["No", "Yes"]) if vehicle == "Truck" else "No"
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # ── Driver Info ──
    st.markdown('<div class="sec-card"><div class="sec-title">👤 Driver Profile</div>', unsafe_allow_html=True)
    driver_name   = st.text_input("Driver Name", placeholder="Full name")
    cnic          = st.text_input("CNIC", placeholder="XXXXX-XXXXXXX-X")
    vehicle_reg   = st.text_input("Vehicle Reg. No.", placeholder="LEA-1234")
    previous      = st.number_input("Previous Violations", 0, 50, 0, help="Adds PKR 5,000 penalty per prior offence")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Knowledge Base Reference ──
    st.markdown('<div class="sec-card"><div class="sec-title">📚 Ordinance Reference</div>', unsafe_allow_html=True)
    sel_sev = st.selectbox("Filter by severity", ["ALL", "CRITICAL", "HIGH", "MEDIUM", "LOW"])
    rows = ""
    for r in RULES.values():
        if sel_sev != "ALL" and r["severity"] != sel_sev:
            continue
        rows += f'<tr><td>{r["section"]}</td><td>{r["name"]}</td><td style="color:{SEV_COLOR[r["severity"]]}">{r["severity"]}</td><td>PKR {r["base_fine"]:,}</td></tr>'
    st.markdown(f"""
    <div style="max-height:320px; overflow-y:auto;">
    <table class="kb-table">
      <tr><th>Section</th><th>Offence</th><th>Sev.</th><th>Base Fine</th></tr>
      {rows}
    </table></div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# ANALYZE BUTTON
# ─────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
if st.button("⚖️  ANALYZE VIOLATIONS", type="primary", use_container_width=True):
    with st.spinner("Running forward-chaining inference engine…"):
        time.sleep(1.0)
        facts = {
            "vehicle": vehicle, "speed": speed, "area": area, "limit": limit,
            "helmet": helmet, "seatbelt": seatbelt, "overloading": overloading,
            "license": license_, "registration": registration, "insurance": insurance,
            "fitness": fitness, "number_plate": number_plate,
            "signal": signal, "wrong_side": wrong_side, "mobile": mobile,
            "pressure_horn": pressure_horn, "indicators": indicators,
            "lane_violation": lane_violation, "tinted": tinted, "dui": dui,
            "illegal_parking": illegal_parking, "underage": underage,
            "goods_overload": goods_overload,
        }
        viols       = check_violations(facts)
        repeat_add  = previous * 5000
        base_sum    = sum(v["base_fine"] for v in viols)
        total_fine  = base_sum + repeat_add
        arrest      = any(v["arrest"] for v in viols)
        points      = sum(v["points"] for v in viols)

        st.session_state.analyzed   = True
        st.session_state.violations = viols
        st.session_state.total      = total_fine
        st.session_state.repeat_add = repeat_add
        st.session_state.base_sum   = base_sum
        st.session_state.arrest     = arrest
        st.session_state.points     = points
        st.session_state.previous   = previous
        st.session_state.driver     = driver_name or "Unknown"
        st.session_state.cnic_val   = cnic or "N/A"
        st.session_state.vreg       = vehicle_reg or "N/A"
        st.session_state.speed_val  = speed
        st.session_state.limit_val  = limit

# ─────────────────────────────────────────────────────────────────
# RESULTS
# ─────────────────────────────────────────────────────────────────
st.markdown('<hr style="border-color:#1a2e4a; margin:2rem 0;">', unsafe_allow_html=True)
st.markdown('<div class="sec-title" style="font-family:Rajdhani,sans-serif; font-size:1.4rem; font-weight:700; color:#f59e0b; letter-spacing:2px; text-transform:uppercase; margin-bottom:1.2rem;">📊 Analysis Result</div>', unsafe_allow_html=True)

if not st.session_state.analyzed:
    st.markdown('<div style="background:#0d1829; border:1px dashed #1e3a5f; border-radius:10px; padding:2rem; text-align:center; color:#334155; font-family:Share Tech Mono,monospace; letter-spacing:2px;">AWAITING INPUT — FILL THE FORM ABOVE AND CLICK ANALYZE</div>', unsafe_allow_html=True)
else:
    # ── driver summary chips ──
    st.markdown(f"""
    <div class="info-row">
      <div class="info-chip"><div class="ic-label">Driver</div><div class="ic-val">{st.session_state.driver}</div></div>
      <div class="info-chip"><div class="ic-label">CNIC</div><div class="ic-val">{st.session_state.cnic_val}</div></div>
      <div class="info-chip"><div class="ic-label">Vehicle Reg.</div><div class="ic-val">{st.session_state.vreg}</div></div>
      <div class="info-chip"><div class="ic-label">Speed</div><div class="ic-val">{st.session_state.speed_val} / {st.session_state.limit_val} km/h</div></div>
      <div class="info-chip"><div class="ic-label">Demerit Points</div><div class="ic-val" style="color:#f59e0b">{st.session_state.points} pts</div></div>
      <div class="info-chip"><div class="ic-label">Arrest Risk</div><div class="ic-val" style="color:{'#ef4444' if st.session_state.arrest else '#22c55e'}">{'⚠ DETAIN' if st.session_state.arrest else '✓ NO'}</div></div>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.violations:
        st.markdown('<div class="status-clear">✅ &nbsp; No Violations Detected — Driver is Compliant</div>', unsafe_allow_html=True)
    else:
        n = len(st.session_state.violations)
        st.markdown(f"**{n} violation(s) detected** under Punjab Motor Vehicles Ordinance 1965")

        # ── Risk Meter ──
        risk_pct = min(100, (st.session_state.points / 30) * 100)
        risk_color = "#ef4444" if risk_pct >= 70 else "#f59e0b" if risk_pct >= 40 else "#eab308"
        risk_label = "CRITICAL RISK" if risk_pct >= 70 else "HIGH RISK" if risk_pct >= 40 else "MODERATE RISK"
        st.markdown(f"""
        <div class="risk-bar-wrap">
          <div class="risk-label" style="color:{risk_color}">🔴 Compliance Risk: {risk_label} ({st.session_state.points} demerit pts)</div>
          <div class="risk-bar-bg"><div class="risk-bar-fill" style="width:{risk_pct}%; background:linear-gradient(90deg,{risk_color}88,{risk_color});"></div></div>
        </div>""", unsafe_allow_html=True)

        # ── Violations Table ──
        rows_html = ""
        for i, v in enumerate(st.session_state.violations, 1):
            cls = f"sev-{v['severity'].lower()}"
            arrest_tag = '<span style="color:#ef4444; font-size:0.7rem; font-family:Share Tech Mono,monospace;">⚠ ARREST</span>' if v["arrest"] else ""
            rows_html += f"""<tr class="{cls}">
              <td style="color:#475569; font-family:Share Tech Mono,monospace; font-size:0.78rem;">{i:02d}</td>
              <td style="font-size:0.75rem; color:#64748b;">{v['section']}</td>
              <td>{v['name']}<br><span style="font-size:0.76rem; color:#475569;">{v['desc']}</span></td>
              <td>{SEV_BADGE[v['severity']]} {arrest_tag}</td>
              <td style="color:#f8f4ec; font-family:Share Tech Mono,monospace; text-align:right;">PKR {v['base_fine']:,}</td>
              <td style="color:#64748b; font-family:Share Tech Mono,monospace; text-align:center;">{v['points']}</td>
            </tr>"""

        st.markdown(f"""
        <table class="viol-table">
          <tr><th>#</th><th>Section</th><th>Offence</th><th>Severity</th><th style="text-align:right;">Base Fine</th><th style="text-align:center;">Points</th></tr>
          {rows_html}
        </table>""", unsafe_allow_html=True)

        # ── Fine Card ──
        st.markdown(f"""
        <div class="fine-card">
          <div class="fine-label">Total Penalty Imposed</div>
          <div class="fine-amount"><span class="fine-currency">PKR</span>{st.session_state.total:,}</div>
          <div class="fine-meta">
            {n} violation fine(s) + {st.session_state.previous} repeat offence penalty(ies)
            {'&nbsp;&nbsp;|&nbsp;&nbsp;⚠️ <span style="color:#ef4444; font-weight:700;">VEHICLE TO BE DETAINED</span>' if st.session_state.arrest else ''}
          </div>
        </div>""", unsafe_allow_html=True)

        # ── Transparent Breakdown ──
        with st.expander("🔍 View Transparent Calculation Breakdown"):
            brows = ""
            for v in st.session_state.violations:
                brows += f'<div class="breakdown-row"><span>{v["name"]}</span><span style="font-family:Share Tech Mono,monospace; color:#c9d6e3;">PKR {v["base_fine"]:,}</span></div>'
            if st.session_state.repeat_add > 0:
                brows += f'<div class="breakdown-row"><span>Repeat offence penalty ({st.session_state.previous} × PKR 5,000)</span><span style="font-family:Share Tech Mono,monospace; color:#ef4444;">+ PKR {st.session_state.repeat_add:,}</span></div>'
            st.markdown(f"""
            <div style="background:#060d1a; padding:1.2rem 1.4rem; border-radius:8px; border:1px solid #1a2e4a;">
              {brows}
              <div class="breakdown-total"><span>TOTAL FINE</span><span>PKR {st.session_state.total:,}</span></div>
            </div>""", unsafe_allow_html=True)

        # ── Legal Notice ──
        st.markdown(f"""
        <div style="background:#0d0a00; border:1px solid #78350f; border-left:4px solid #f59e0b; border-radius:8px; padding:1.2rem 1.4rem; margin-top:1rem; font-size:0.82rem; color:#78350f; line-height:1.7;">
          <strong style="color:#f59e0b;">⚖️ LEGAL NOTICE:</strong> This challan is issued under the Punjab Motor Vehicles Ordinance 1965 and Motor Vehicles Rules 1969.
          The accused may contest this challan before the Motor Vehicles Examiner / Magistrate within <strong>30 days</strong> of issuance.
          Non-payment within the prescribed period may lead to vehicle impoundment and/or enhanced penalties under Section 130 MVO.
          {'<br><strong style="color:#ef4444;">🚨 VEHICLE DETAINED:</strong> One or more offences mandate vehicle detention pending further proceedings.' if st.session_state.arrest else ''}
        </div>""", unsafe_allow_html=True)

# Footer removed — add your own branding here if needed
