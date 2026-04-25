# Traffic Law Enforcement System

A rule-based expert system for detecting and calculating traffic violations under the **Punjab Motor Vehicles Ordinance 1965**. Built with Python and Streamlit, it uses a forward-chaining inference engine over a structured knowledge base of 25+ traffic rules.

---

## Features

- **Forward-Chaining Inference Engine** — automatically evaluates all applicable rules against a given set of traffic facts
- **25+ Violation Rules** — covers speed, safety equipment, documentation, signal violations, DUI, and more
- **Fine Calculation** — computes base fines with repeat-offence penalty multipliers
- **Demerit Point System** — assigns licence demerit points per violation
- **Arrest / Detention Flagging** — identifies offences that mandate vehicle detention
- **Risk Meter** — visual compliance risk gauge based on accumulated demerit points
- **Knowledge Base Reference** — filterable ordinance reference table built into the UI
- **Dark Government Aesthetic** — professional dark-navy UI with Rajdhani and Share Tech Mono fonts

---

## Tech Stack

| Layer | Technology |
|---|---|
| UI Framework | [Streamlit](https://streamlit.io) |
| Language | Python 3.9+ |
| Inference | Custom forward-chaining engine |
| Knowledge Base | Python dict-based rule store with lambda conditions |
| Styling | Custom CSS (dark navy / government theme) |

---

## Getting Started

### Prerequisites

```
Python 3.9 or higher
pip
```

### Installation

```bash
# Clone the repository
https://github.com/MNS-developer/traffic-law-enforcement-system.git
cd traffic-law-enforcement-system

# Install dependencies
pip install streamlit

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

---

## Project Structure

```
traffic-law-enforcement-system/
├── app.py          # Main application — UI, knowledge base, inference engine
└── README.md
└── Traffic Law Enforcement System.png     #Screenshot
```

---

## Knowledge Base

Rules are defined as Python dictionaries with the following schema:

```python
"rule_id": {
    "section":   "S.74 MVO",           # Ordinance section reference
    "name":      "Overspeeding ...",   # Human-readable name
    "desc":      "...",                # Description shown in results
    "cond":      lambda f: ...,        # Condition evaluated against facts dict
    "base_fine": 5000,                 # Fine in PKR
    "severity":  "HIGH",              # CRITICAL | HIGH | MEDIUM | LOW
    "arrest":    False,               # Whether offence mandates detention
    "points":    3,                   # Demerit points
}
```

To add a new rule, simply add an entry to the `RULES` dict in `app.py`. No other changes are needed — the inference engine and UI pick it up automatically.

---

## Violation Categories

| Category | Examples |
|---|---|
| Speed | Overspeeding by zone, extreme overspeeding |
| Safety | No helmet, no seatbelt, passenger overloading |
| Documents | No licence, expired registration, no insurance |
| Traffic Signals | Red light, wrong-side driving |
| Vehicle Condition | No number plate, defective indicators, illegal tint |
| Conduct | Mobile phone use, DUI, underage driving |
| Goods Vehicles | Overloading beyond permissible weight |

---

## Legal Reference

All rules reference the **Punjab Motor Vehicles Ordinance 1965** and **Motor Vehicles Rules 1969**, applicable to Punjab, Pakistan. Fine amounts reflect current Punjab Safe Cities Authority / Traffic Police published schedules.

> **Disclaimer:** This system is for informational and educational purposes. It is not a substitute for official legal proceedings. Always consult the relevant traffic authority for official challan issuance.

---

## License

[MIT License](LICENSE) — free to use, modify, and distribute.
