# CSRD Climate Implementation
## ESRS E1 Climate Reporting for Swedish Steel Industry

End-to-end implementation of Corporate Sustainability Reporting Directive (CSRD) climate reporting using GHG Protocol, Python, and Power BI. Demonstrates practical ESG data management and sustainability reporting competency.

---

## Project Overview

This project showcases a complete **ESRS E1 Climate Change** reporting implementation for **Norrland Stål AB**, a fictional Swedish steel manufacturer. It covers:

- **GHG Protocol Scope 1-3** emissions accounting
- **ESRS E1** alignment and disclosure requirements
- **Synthetic data generation** with industry-realistic benchmarks
- **Data quality management** per ESRS standards
- **Automated reporting** ready for Power BI visualization

**Use Case:** Portfolio project demonstrating CSRD/ESG implementation expertise for consulting roles in sustainability reporting, climate analytics, and corporate ESG management.

---

## Current Status

| Component | Status | Description |
|-----------|--------|-------------|
| **Python Data Generator** | ✓ Complete | Generates 24 months of realistic GHG emissions data |
| **Data Documentation** | ✓ Complete | Full data dictionary with emission factors and references |
| **Methodology Documentation** | ✓ Complete | GHG Protocol + ESRS E1 methodology guide |
| **Synthetic Dataset** | ✓ Generated | Excel file with 4 sheets (778k tCO2e over 24 months) |
| **Power BI Dashboard** | In Progress | Visualization and KPI tracking (coming soon) |
| **GitHub Repository** | ✓ Live | [github.com/ekblomvictor/CSRD-Climate-Implementation](https://github.com/ekblomvictor/CSRD-Climate-Implementation) |

---

## Project Structure

```
CSRD-Climate-Implementation/
│
├── data/
│   ├── README.md                        # Data dictionary & emission factors
│   └── norrland_stal_emissions.xlsx     # Generated dataset (not in Git)
│
├── scripts/
│   └── generate_mock_data.py            # Python data generator
│
├── docs/
│   └── methodology.md                   # GHG Protocol methodology
│
├── powerbi/
│   └── (Power BI files - coming soon)
│
├── .gitignore                           # Excludes .xlsx and .pbix files
└── README.md                            # This file
```

---

## Key Features

### 1. Realistic Emissions Data
- **24 months** of monthly emissions data (2023-2024)
- **Scope 1:** Blast furnace operations (18,000-22,000 tCO2e/month)
- **Scope 2:** Electricity and district heating (~350 tCO2e/month, Swedish low-carbon grid)
- **Scope 3:** Value chain emissions covering 4 material categories (8,000-15,000 tCO2e/month)
- **Seasonal variation:** Production and emissions fluctuate realistically

### 2. ESRS E1 Compliance
- **Data quality classification:** Measured, Calculated, Estimated per ESRS requirements
- **Scope 2 dual reporting:** Both location-based and market-based methods
- **Emissions intensity:** tCO2e per tonne of steel produced
- **Materiality assessment:** 4 of 15 Scope 3 categories included (>95% coverage)

### 3. GHG Protocol Foundation
- **Organizational boundary:** Operational control approach
- **Scope 1-3 definitions:** Complete implementation with source breakdowns
- **Emission factors:** Sourced from IPCC, IEA, Swedish Energy Agency, WorldSteel
- **Calculation transparency:** Documented formulas and assumptions

### 4. Swedish Industry Context
- **Steel manufacturing:** Blast furnace route (NACE C24.10)
- **Low-carbon electricity:** Swedish grid (~13 g CO2e/kWh)
- **Nordic benchmarks:** Emissions intensity competitive with Swedish industry average
- **EU ETS coverage:** ~90% of Scope 1 emissions

---

## Getting Started

### Prerequisites
- **Python 3.8+** (tested with Python 3.14.2)
- **Libraries:** pandas, numpy, openpyxl
- **Optional:** Power BI Desktop (for visualization)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ekblomvictor/CSRD-Climate-Implementation.git
   cd CSRD-Climate-Implementation
   ```

2. **Install Python dependencies**
   ```bash
   pip install pandas numpy openpyxl
   ```

3. **Generate emissions data**
   ```bash
   python scripts/generate_mock_data.py
   ```

   **Output:**
   - `data/norrland_stal_emissions.xlsx` with 4 sheets:
     - **Emissions_Data:** Monthly time series (24 rows × 40+ columns)
     - **Company_Info:** Company profile metadata
     - **Annual_Summary:** Yearly aggregated metrics
     - **Data_Quality:** Measured/Calculated/Estimated breakdown

4. **Review documentation**
   - Data dictionary: `data/README.md`
   - Methodology guide: `docs/methodology.md`

---

## Data Summary

**Company:** Norrland Stål AB (Luleå, Sweden)
**Industry:** Steel Manufacturing (NACE C24.10)
**Reporting Period:** January 2023 - December 2024

### Emissions Overview (24 months)

| Scope | Total Emissions | % of Total | Data Quality |
|-------|----------------|------------|--------------|
| **Scope 1** | 457,497 tCO2e | 58.8% | 70% measured |
| **Scope 2** | 8,796 tCO2e | 1.1% | 90% measured |
| **Scope 3** | 311,825 tCO2e | 40.1% | 15% measured |
| **Total** | **778,118 tCO2e** | **100%** | **48.2% measured** |

**Production:** 933,609 tonnes steel
**Emissions Intensity:** 0.834 tCO2e per tonne steel

### Scope 3 Breakdown (Included Categories)

| Category | Description | % of Scope 3 |
|----------|-------------|--------------|
| **Cat 1** | Purchased goods (ore, coal, limestone) | ~65% |
| **Cat 4** | Upstream transportation | ~20% |
| **Cat 9** | Downstream transportation | ~10% |
| **Cat 12** | End-of-life treatment | ~5% |

---

## Methodology Highlights

### Emission Factors Used

**Scope 1:**
- Blast furnace: 0.48 tCO2e/tonne steel (Swedish industry benchmark)
- Diesel: 2.68 kg CO2e/liter (IPCC 2006)

**Scope 2:**
- Swedish electricity grid: 13 g CO2e/kWh (location-based)
- Renewable contracts: 8 g CO2e/kWh (market-based)
- District heating: 15 g CO2e/kWh (bio-CHP)

**Scope 3:**
- Iron ore: 0.05 tCO2e/tonne (Ecoinvent 3.9)
- Coking coal: 0.15 tCO2e/tonne (IEA Coal 2023)
- Rail freight: 0.022 kg CO2e/tkm (EN 16258:2012)
- Road freight: 0.062 kg CO2e/tkm (GLEC Framework)

See `docs/methodology.md` for complete methodology documentation.

---

## Technical Stack

- **Python 3.14:** Data generation and processing
- **pandas:** Time series data manipulation
- **numpy:** Stochastic data modeling
- **openpyxl:** Excel export with multi-sheet formatting
- **Power BI:** Visualization and dashboard (in progress)
- **Git/GitHub:** Version control and portfolio hosting

---

## Use Cases & Learning Objectives

This project demonstrates competency in:

1. **CSRD/ESRS Implementation:** Practical application of EU sustainability reporting standards
2. **GHG Protocol Expertise:** Scope 1-3 accounting per Corporate Standard
3. **ESG Data Management:** Data quality, emission factors, calculation methodologies
4. **Python for ESG:** Automated data generation and reporting pipelines
5. **Industry Knowledge:** Steel manufacturing emissions benchmarks and mitigation strategies
6. **Stakeholder Communication:** Technical documentation for assurance and compliance

**Target Roles:**
- ESG Consultant / Sustainability Analyst
- Climate Reporting Specialist
- CSRD Implementation Manager
- Carbon Accounting Analyst
- Corporate Sustainability Reporting

---

## ESRS E1 Disclosure Coverage

| Requirement | Status | Notes |
|-------------|--------|-------|
| E1-6: Gross Scopes 1, 2, 3 emissions | ✓ Complete | All scopes reported in tCO2e |
| E1-6: Location & market-based Scope 2 | ✓ Complete | Both methods provided |
| E1-6: Emissions intensity | ✓ Complete | Per tonne steel produced |
| E1-6: Data quality breakdown | ✓ Complete | Measured/Calculated/Estimated |
| E1-5: Energy consumption | ✓ Complete | Electricity and heating reported |
| E1-4: GHG reduction targets | Partial | Target: <0.70 tCO2e/t by 2030 |
| E1-1: Transition plan | In Progress | To be developed (2025) |

---

## Next Steps

### Power BI Dashboard (In Progress)
- [ ] Import Excel data to Power BI
- [ ] Create emissions trend visualizations
- [ ] Build Scope 1-3 waterfall charts
- [ ] Add data quality KPI cards
- [ ] Implement emissions intensity tracker
- [ ] Design ESRS E1 disclosure report page

### Enhancements
- [ ] Add scenario modeling (e.g., hydrogen-based steelmaking)
- [ ] Include EU ETS carbon pricing simulation
- [ ] Expand Scope 3 to all 15 categories
- [ ] Add supplier engagement data quality improvements
- [ ] Create automated assurance audit trail

---

## References

### Standards & Frameworks
1. **GHG Protocol Corporate Standard** (2015) - WRI/WBCSD
2. **GHG Protocol Scope 3 Standard** (2011) - WRI/WBCSD
3. **ESRS E1 Climate Change** (2023) - EFRAG
4. **ISO 14064-1:2018** - Greenhouse gas accounting
5. **CSRD Directive (EU) 2022/2464** - European Commission

### Emission Factor Sources
6. **IPCC Guidelines** (2006, 2019 Refinement)
7. **Swedish Energy Agency** - Miljövärdering av el och värme (2024)
8. **Ecoinvent 3.9** - LCA database
9. **IEA Coal 2023** - International Energy Agency
10. **WorldSteel LCA** (2023) - Steel industry life cycle assessment

---

## Contact & License

**Author:** Victor Ekblom
**Email:** ekblomvictor@gmail.com
**GitHub:** [github.com/ekblomvictor](https://github.com/ekblomvictor)
**LinkedIn:** [linkedin.com/in/victor-ekblom](https://linkedin.com/in/victor-ekblom)

**License:** MIT License (for code and documentation)

**Note:** This project uses synthetic data for demonstration purposes. All emission factors and methodologies reflect real-world industry practices suitable for portfolio and training use cases.

---

## Acknowledgments

- **Swedish Steel Industry Association** for emissions benchmarking data
- **EFRAG** for ESRS E1 technical guidance
- **GHG Protocol** for corporate accounting standards
- **Anthropic Claude** for technical implementation support

---

**Last Updated:** January 2024
**Project Status:** Active Development
**Version:** 1.0
