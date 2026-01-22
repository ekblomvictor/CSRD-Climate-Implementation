# GHG Accounting Methodology
## CSRD Climate Implementation - Norrland Stål AB

---

## 1. Overview

This document outlines the greenhouse gas (GHG) accounting methodology used by Norrland Stål AB for climate reporting under the Corporate Sustainability Reporting Directive (CSRD) and European Sustainability Reporting Standard E1 (ESRS E1).

**Reporting Period:** January 2023 - December 2024
**Reporting Frameworks:**
- GHG Protocol Corporate Accounting and Reporting Standard
- GHG Protocol Corporate Value Chain (Scope 3) Standard
- ESRS E1 Climate Change
- ISO 14064-1:2018

---

## 2. GHG Protocol Foundation

### 2.1 The Three Scopes

The GHG Protocol classifies emissions into three scopes based on operational control:

#### **Scope 1: Direct GHG Emissions**
Emissions from sources that are owned or controlled by the company.

**Included Sources:**
- **Blast furnace operations:** CO₂ emissions from reduction of iron ore using coke (carbon-based fuel)
- **Auxiliary combustion:** On-site fuel combustion for heating, drying, and auxiliary processes
- **Mobile sources:** Company-owned vehicles and mobile equipment
- **Process emissions:** Chemical reactions in steelmaking (non-combustion)

**Formula:**
```
Scope 1 = Σ (Activity Data × Emission Factor)

Where:
- Activity Data = Fuel consumption (liters, m³, kg) or process output (tonnes)
- Emission Factor = kg CO₂e per unit activity (from IPCC, national databases)
```

**Key Characteristics:**
- Direct control over emission sources
- High data quality possible (70% measured via CEMS)
- Subject to EU Emissions Trading System (EU ETS)

---

#### **Scope 2: Indirect Energy-Related Emissions**
Emissions from the generation of purchased electricity, heat, steam, and cooling.

**Included Sources:**
- **Purchased electricity:** Grid electricity for electric arc furnaces, rolling mills, auxiliary equipment
- **District heating:** Purchased heat for facility heating and process steam

**Two Accounting Methods (both reported):**

1. **Location-Based Method**
   - Uses average emission factor for the regional grid
   - Reflects physical electricity consumption
   - Formula: `Electricity (kWh) × Grid Average EF (kg CO₂e/kWh)`

2. **Market-Based Method**
   - Uses emission factor from specific supplier contracts
   - Reflects contractual instruments (renewable energy certificates)
   - Formula: `Electricity (kWh) × Supplier-Specific EF (kg CO₂e/kWh)`

**Swedish Context:**
- Sweden has one of the lowest grid emission factors globally (~13 g CO₂e/kWh)
- High share of hydro (~45%) and nuclear (~30%) power
- Renewable energy certificates (Guarantees of Origin) common

**Key Characteristics:**
- Indirect emissions but relatively easy to measure
- High data quality (90% measured via utility meters)
- Choice of renewable energy impacts market-based accounting

---

#### **Scope 3: Other Indirect Emissions**
All other indirect emissions occurring in the company's value chain (upstream and downstream).

**Materiality Assessment Results:**

| Category | Description | Materiality | Included |
|----------|-------------|-------------|----------|
| **1. Purchased Goods & Services** | Raw materials (ore, coal, limestone) | High (~65% of Scope 3) | ✓ Yes |
| **2. Capital Goods** | Machinery, equipment | Low | ✗ No |
| **3. Fuel & Energy-Related** | Upstream emissions from energy | Low | ✗ No |
| **4. Upstream Transportation** | Inbound logistics | Medium (~20% of Scope 3) | ✓ Yes |
| **5. Waste Generated** | Waste disposal | Low | ✗ No |
| **6. Business Travel** | Employee travel | Negligible | ✗ No |
| **7. Employee Commuting** | Staff commuting | Negligible | ✗ No |
| **8. Upstream Leased Assets** | Not applicable | N/A | ✗ No |
| **9. Downstream Transportation** | Outbound logistics | Medium (~10% of Scope 3) | ✓ Yes |
| **10. Processing of Sold Products** | Further processing by customers | Low | ✗ No |
| **11. Use of Sold Products** | Steel used in products | Not applicable | ✗ No |
| **12. End-of-Life Treatment** | Recycling, disposal | Low (~5% of Scope 3) | ✓ Yes |
| **13. Downstream Leased Assets** | Not applicable | N/A | ✗ No |
| **14. Franchises** | Not applicable | N/A | ✗ No |
| **15. Investments** | Not material | Low | ✗ No |

**Key Characteristics:**
- Largest emissions (typically 60-70% of total for steel)
- Lowest data quality (60% estimated due to supplier data gaps)
- Improvement priority: supplier engagement for primary data

---

## 3. Organizational Boundaries

### 3.1 Consolidation Approach

**Selected Approach:** Operational Control

**Definition:** Norrland Stål AB accounts for 100% of GHG emissions from operations over which it has operational control.

**Rationale:**
- Aligns with financial reporting boundaries
- Clear decision-making authority over emission sources
- Consistent with EU ETS obligations

**Included Facilities:**
- Luleå Steel Plant (primary production facility)
- On-site warehousing and logistics
- Administrative buildings on-site

**Excluded:**
- Joint ventures where operational control is shared
- Off-site supplier facilities (reported in Scope 3)

---

## 4. Operational Boundaries

### 4.1 Included Emission Sources by Scope

**Scope 1 Sources:**
```
Blast Furnace Operations
├── Iron ore reduction (coke consumption)
├── Hot blast stoves (coke oven gas)
├── Auxiliary fuel combustion (natural gas, diesel)
└── Company vehicle fleet (diesel, gasoline)
```

**Scope 2 Sources:**
```
Purchased Energy
├── Electricity (grid connection, ~27 GWh/month)
├── District heating (Luleå Energi, biofuel-based)
└── Steam (purchased from co-generation facility)
```

**Scope 3 Sources:**
```
Category 1: Purchased Goods
├── Iron ore (1.6 tonnes per tonne steel)
├── Coking coal (0.4 tonnes per tonne steel)
└── Limestone and additives (0.2 tonnes per tonne steel)

Category 4: Upstream Transport
├── Rail freight (iron ore from Kiruna)
├── Ship freight (coal imports)
└── Road freight (additives)

Category 9: Downstream Transport
└── Customer deliveries (road/rail, average 300 km)

Category 12: End-of-Life
└── Steel recycling and disposal (credit for recycled content)
```

### 4.2 Exclusions and Rationale

| Exclusion | Rationale |
|-----------|-----------|
| Categories 2, 3, 5-8, 10-11, 13-15 | Below 5% materiality threshold (assessed 2023) |
| Fugitive emissions (refrigerants) | Negligible (<0.1% of Scope 1) |
| Biogenic CO₂ from biomass | Reported separately per GHG Protocol |
| Indirect land use change | Not applicable to steel manufacturing |

---

## 5. Emission Factors and Data Sources

### 5.1 Scope 1 Emission Factors

| Source | Emission Factor | Unit | Reference | Update Frequency |
|--------|----------------|------|-----------|------------------|
| Blast furnace (integrated route) | 0.48 | tCO2e/tonne steel | Swedish Steel Industry, 2023 | Annual |
| Diesel fuel | 2.68 | kg CO2e/liter | IPCC 2006, Vol. 2 | Static |
| Natural gas | 0.184 | kg CO2e/kWh | Swedish Energy Agency | Annual |
| Coke (metallurgical) | 3.17 | kg CO2e/kg | ISO 14404-1:2013 | Static |

**Notes:**
- Blast furnace factor is plant-specific (measured via CEMS and mass balance)
- Reflects Swedish industry benchmarks (lower than global average due to efficiency)

### 5.2 Scope 2 Emission Factors

| Source | Location-Based | Market-Based | Unit | Reference |
|--------|----------------|--------------|------|-----------|
| Swedish electricity grid (SE3 zone) | 13 | - | g CO2e/kWh | Swedish Energy Agency, 2024 |
| Renewable electricity (GOs) | - | 8 | g CO2e/kWh | Supplier certificate, 2024 |
| District heating (Luleå) | 15 | - | g CO2e/kWh | Luleå Energi, 2024 |

**Notes:**
- Location-based: Nordic residual mix (after GO exports)
- Market-based: 70% renewable certificates, 30% residual mix
- District heating: Bio-CHP plant (biomass co-generation)

### 5.3 Scope 3 Emission Factors

#### Category 1: Purchased Goods

| Material | Emission Factor | Unit | Reference | Data Quality |
|----------|----------------|------|-----------|--------------|
| Iron ore (70% Fe content) | 0.05 | tCO2e/tonne | Ecoinvent 3.9 | Database average |
| Coking coal | 0.15 | tCO2e/tonne | IEA Coal 2023 | Global average |
| Limestone (CaCO₃) | 0.02 | tCO2e/tonne | USGS Minerals, 2023 | Process average |
| Scrap steel | 0.30 | tCO2e/tonne | WorldSteel LCA | Industry average |

**Data Quality Improvement Plan:**
- Target: Replace 40% of database factors with supplier-specific data by 2025
- Engagement: Send supplier questionnaires per PACT Framework

#### Category 4 & 9: Transportation

| Mode | Emission Factor | Unit | Reference |
|------|----------------|------|-----------|
| Rail freight (electric) | 0.022 | kg CO2e/tkm | EN 16258:2012 |
| Rail freight (diesel) | 0.045 | kg CO2e/tkm | EN 16258:2012 |
| Ship freight (bulk carrier) | 0.011 | kg CO2e/tkm | IMO Fourth GHG Study |
| Road freight (HDV >20t) | 0.062 | kg CO2e/tkm | GLEC Framework v3 |

**Assumptions:**
- Average transport distances: Ore (450 km), Coal (800 km), Customer (300 km)
- Modal split: Rail (60%), Road (30%), Ship (10%)

#### Category 12: End-of-Life

| Process | Emission Factor | Unit | Reference |
|---------|----------------|------|-----------|
| Steel recycling (scrap processing) | 0.02 | tCO2e/tonne | WorldSteel, 2023 |
| Landfill disposal (steel waste) | 0.01 | tCO2e/tonne | IPCC Waste Guidelines |

**Notes:**
- Assumes 95% of steel is eventually recycled (circular economy)
- No emissions avoided credit applied (conservative approach)

---

## 6. Calculation Methodology

### 6.1 General Formula

```
GHG Emissions = Σ (Activity Data × Emission Factor × GWP)

Where:
- Activity Data = Quantified activity (fuel, electricity, materials, transport)
- Emission Factor = Emission per unit activity (kg CO₂e/unit)
- GWP = Global Warming Potential (100-year, IPCC AR6)
```

### 6.2 Scope-Specific Calculations

**Scope 1 - Blast Furnace Example:**
```
Monthly Production = 40,000 tonnes steel
Emission Factor = 0.48 tCO2e/tonne steel
Scope 1 Blast Furnace = 40,000 × 0.48 = 19,200 tCO2e
```

**Scope 2 - Electricity Example (Location-Based):**
```
Monthly Electricity Consumption = 27,000,000 kWh
Grid Emission Factor = 0.000013 tCO2e/kWh (13 g/kWh)
Scope 2 Location-Based = 27,000,000 × 0.000013 = 351 tCO2e
```

**Scope 3 - Category 1 Example (Iron Ore):**
```
Steel Production = 40,000 tonnes
Iron Ore Requirement = 40,000 × 1.6 = 64,000 tonnes
Emission Factor = 0.05 tCO2e/tonne ore
Cat 1 Iron Ore = 64,000 × 0.05 = 3,200 tCO2e
```

**Scope 3 - Category 4 Example (Upstream Transport):**
```
Iron Ore Transported = 64,000 tonnes
Transport Distance = 450 km (Kiruna to Luleå)
Mode = Rail (80% electric, 20% diesel)

Transport Intensity = 64,000 tonnes × 450 km = 28,800,000 tkm

Electric Rail: 28,800,000 × 0.80 × 0.000022 = 507 tCO2e
Diesel Rail: 28,800,000 × 0.20 × 0.000045 = 259 tCO2e
Cat 4 Total = 507 + 259 = 766 tCO2e
```

### 6.3 Emissions Intensity

```
Emissions Intensity = Total GHG Emissions / Production Output

Example (monthly):
Total Emissions = 30,000 tCO2e
Production = 40,000 tonnes steel
Intensity = 30,000 / 40,000 = 0.75 tCO2e per tonne steel
```

**Industry Benchmark:**
- Global average (blast furnace): 1.8-2.0 tCO2e/tonne steel
- Sweden (efficient plants): 0.7-0.9 tCO2e/tonne steel
- Norrland Stål target: <0.75 tCO2e/tonne by 2025

---

## 7. Data Quality and Uncertainty

### 7.1 Data Quality Hierarchy (ESRS E1)

Per ESRS E1, emissions data is classified by measurement approach:

| Quality Level | Definition | Uncertainty Range | Target Share |
|---------------|------------|-------------------|--------------|
| **Measured** | Direct instrumentation (CEMS, meters, scales) | ±5% | >70% (Scope 1, 2) |
| **Calculated** | Activity data × standard emission factors | ±10-20% | 20-30% |
| **Estimated** | Proxies, spend-based, industry averages | ±50-100% | <10% (minimize) |

### 7.2 Current Data Quality by Scope

```
Scope 1: 70% Measured + 25% Calculated + 5% Estimated
Scope 2: 90% Measured + 10% Calculated + 0% Estimated
Scope 3: 15% Measured + 25% Calculated + 60% Estimated
```

**Overall Score:** 47% measured (weighted by emissions volume)

### 7.3 Uncertainty Quantification

| Scope | Estimated Uncertainty | Confidence Level |
|-------|----------------------|------------------|
| Scope 1 | ±8% | High (CEMS verified) |
| Scope 2 | ±5% | Very High (metered) |
| Scope 3 | ±60% | Low (supplier data gaps) |
| **Total** | ±35% | Medium |

**Improvement Actions:**
1. Engage top 10 suppliers for primary data (covers 80% of Scope 3 Cat 1)
2. Request carrier-specific emission factors for transport
3. Annual recalibration of CEMS per ISO 14181

---

## 8. ESRS E1 Climate Change Alignment

### 8.1 Disclosure Requirements Coverage

| ESRS E1 Requirement | Status | Documentation Location |
|---------------------|--------|------------------------|
| **E1-1:** Transition Plan | ⚠ In Progress | Separate document (2025) |
| **E1-2:** Policies on Climate Mitigation | ✓ Complete | Sustainability Policy |
| **E1-3:** Actions and Resources | ⚠ Partial | Investment plan (2024) |
| **E1-4:** Targets | ✓ Complete | Target: <0.70 tCO2e/t by 2030 |
| **E1-5:** Energy Consumption | ✓ Complete | Scope 2 data |
| **E1-6:** GHG Emissions | ✓ Complete | This methodology + data |
| **E1-7:** GHG Removals | ✗ Not Applicable | No removal activities |
| **E1-8:** Internal Carbon Pricing | ⚠ Planned | Implementation 2025 |
| **E1-9:** Anticipated Financial Effects | ⚠ Partial | Risk assessment ongoing |

### 8.2 ESRS E1-6 Specific Requirements

**✓ Gross Scope 1, 2, 3 Emissions:** Reported in tonnes CO₂e
**✓ Location-Based and Market-Based Scope 2:** Both methods provided
**✓ Emissions Intensity:** tCO₂e per tonne steel produced
**⚠ Emissions by Country:** Single-country operations (Sweden only)
**⚠ Regulated Emissions (EU ETS):** ~90% of Scope 1 under EU ETS
**⚠ Change in Inventory:** First reporting period (no comparison)

---

## 9. Base Year and Recalculation

### 9.1 Base Year Selection

**Base Year:** 2023 (first full year of comprehensive data collection)

**Criteria:**
- Reliable data availability across all scopes
- Representative operational performance
- No major structural changes

### 9.2 Recalculation Policy

Emissions will be recalculated if:
- **Structural changes:** Acquisitions, divestments, mergers (>5% of base year emissions)
- **Methodology improvements:** Material change to emission factors or calculation methods
- **Errors discovered:** Calculation errors exceeding 5% of base year emissions

**Significance Threshold:** ±5% of base year emissions per GHG Protocol

---

## 10. Verification and Assurance

### 10.1 Current Status

**2023-2024:** Internal verification by ESG team
**2025 onwards:** Limited external assurance per CSRD requirements

### 10.2 Assurance Scope (Planned)

| Scope | Assurance Level | Standard |
|-------|----------------|----------|
| Scope 1 | Limited | ISO 14064-3 |
| Scope 2 | Limited | ISO 14064-3 |
| Scope 3 (Cat 1, 4, 9, 12) | Limited | ISO 14064-3 |
| Other Scope 3 | None | - |

**Assurance Provider:** To be selected (Big 4 accounting firm or specialized ESG assurer)

---

## 11. Limitations and Continuous Improvement

### 11.1 Known Limitations

1. **Scope 3 Data Gaps:** 60% of Scope 3 relies on secondary data (databases, industry averages)
2. **Allocation Methods:** Some multi-output processes use economic allocation (not physical)
3. **Biogenic Carbon:** Biomass emissions in district heating not fully quantified
4. **Temporal Mismatch:** Some Scope 3 emission factors lag activity data by 1-2 years

### 11.2 Improvement Roadmap

**2024:**
- ✓ Establish GHG inventory and reporting system
- ⚠ Conduct materiality assessment for all 15 Scope 3 categories
- ⚠ Implement monthly data collection processes

**2025:**
- ☐ Engage top 10 suppliers for primary emissions data (Scope 3 Cat 1)
- ☐ Obtain limited external assurance per CSRD
- ☐ Refine emission factors based on supplier engagement
- ☐ Implement internal carbon pricing (shadow price: 100 EUR/tCO2e)

**2026-2030:**
- ☐ Achieve 50% measured data in Scope 3 Cat 1
- ☐ Expand Scope 3 coverage to all material categories
- ☐ Transition to reasonable assurance (from limited)
- ☐ Align with Science-Based Targets initiative (SBTi)

---

## 12. References

### Primary Standards
1. **GHG Protocol Corporate Standard** (Revised Edition, 2015) - World Resources Institute / World Business Council for Sustainable Development
2. **GHG Protocol Scope 3 Standard** (2011) - WRI/WBCSD
3. **ESRS E1 Climate Change** (July 2023) - European Financial Reporting Advisory Group (EFRAG)
4. **ISO 14064-1:2018** - Greenhouse gases — Specification with guidance at the organization level

### Emission Factor Sources
5. **IPCC Guidelines for National GHG Inventories** (2006, 2019 Refinement)
6. **Swedish Energy Agency** - Miljövärdering av el och värme (2024)
7. **Ecoinvent v3.9** - Life Cycle Inventory Database (2023)
8. **IEA Coal 2023** - International Energy Agency
9. **WorldSteel Life Cycle Assessment** (2023) - World Steel Association
10. **EN 16258:2012** - Methodology for calculation and declaration of energy consumption and GHG emissions of transport services
11. **GLEC Framework v3** - Global Logistics Emissions Council (2023)
12. **IMO Fourth GHG Study** - International Maritime Organization (2020)

### Industry Benchmarks
13. **Swedish Steel Industry Association** - Emissions Benchmarking Report (2023)
14. **European Steel Association (EUROFER)** - Low Carbon Roadmap 2050
15. **ISSB IFRS S2** - Climate-related Disclosures (2023) - International Sustainability Standards Board

### Data Quality
16. **GHG Protocol Scope 3 Evaluator** - Uncertainty quantification tool
17. **PACT Framework** - Partnership for Carbon Transparency (Scope 3 data exchange)
18. **ISO 14181** - Quality assurance of continuous emissions monitoring systems

---

## Appendix A: Glossary

| Term | Definition |
|------|------------|
| **tCO₂e** | Tonnes of carbon dioxide equivalent (includes all GHGs using GWP) |
| **GWP** | Global Warming Potential (100-year horizon, IPCC AR6) |
| **CEMS** | Continuous Emissions Monitoring System |
| **EF** | Emission Factor |
| **tkm** | Tonne-kilometers (mass × distance for transport) |
| **GOs** | Guarantees of Origin (renewable energy certificates) |
| **EU ETS** | European Union Emissions Trading System |
| **ESRS** | European Sustainability Reporting Standards |
| **CSRD** | Corporate Sustainability Reporting Directive |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | January 2024 | Victor Ekblom | Initial methodology documentation |

**Next Review Date:** January 2025
**Approval Status:** Approved by ESG Steering Committee

---
