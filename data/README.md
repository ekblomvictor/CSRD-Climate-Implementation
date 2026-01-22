# Climate Data Documentation
## Norrland Stål AB - ESRS E1 Climate Reporting

---

## Company Profile

**Company Name:** Norrland Stål AB
**Industry:** Steel Manufacturing (NACE Code C24.10)
**Location:** Luleå, Sweden
**Reporting Period:** January 2023 - December 2024 (24 months)
**Production Capacity:** 500,000 tonnes steel per year
**Primary Process:** Blast furnace-based steel production

---

## Data Dictionary

### General Information Columns

| Column | Description | Unit | Data Type |
|--------|-------------|------|-----------|
| `Date` | Reporting month in YYYY-MM format | - | String |
| `Year` | Reporting year | - | Integer |
| `Month` | Month number (1-12) | - | Integer |
| `Month_Name` | Month name in English | - | String |
| `Production_Tonnes` | Steel production volume | tonnes | Float |

### Scope 1 Emissions (Direct GHG Emissions)

| Column | Description | Unit | Data Type |
|--------|-------------|------|-----------|
| `Scope1_Total_tCO2e` | Total direct emissions | tCO2e | Float |
| `Scope1_Blast_Furnace` | Emissions from blast furnace operations | tCO2e | Float |
| `Scope1_Auxiliary` | Emissions from auxiliary combustion (heating, transport) | tCO2e | Float |
| `Scope1_Measured` | Directly measured emissions (CEMS) | tCO2e | Float |
| `Scope1_Calculated` | Calculated emissions (fuel consumption × EF) | tCO2e | Float |
| `Scope1_Estimated` | Estimated emissions (proxies, assumptions) | tCO2e | Float |

**Sources:**
- Blast furnace: Continuous Emissions Monitoring Systems (CEMS)
- Auxiliary: Fuel logs and default emission factors

### Scope 2 Emissions (Indirect Energy-Related Emissions)

| Column | Description | Unit | Data Type |
|--------|-------------|------|-----------|
| `Scope2_Total_tCO2e` | Total indirect energy emissions (location-based) | tCO2e | Float |
| `Scope2_Electricity_kWh` | Total electricity consumption | kWh | Float |
| `Scope2_Location_Based` | Emissions using grid average emission factor | tCO2e | Float |
| `Scope2_Market_Based` | Emissions using supplier-specific emission factor | tCO2e | Float |
| `Scope2_Heating` | District heating emissions | tCO2e | Float |
| `Scope2_Measured` | Metered electricity/heat consumption | tCO2e | Float |
| `Scope2_Calculated` | Calculated using emission factors | tCO2e | Float |
| `Scope2_Estimated` | Estimated consumption (not used for Scope 2) | tCO2e | Float |

**Sources:**
- Electricity: Utility bills with hourly metering
- District heating: Monthly invoices from Luleå Energi

### Scope 3 Emissions (Other Indirect Emissions)

| Column | Description | Unit | Data Type |
|--------|-------------|------|-----------|
| `Scope3_Total_tCO2e` | Total value chain emissions | tCO2e | Float |
| `Scope3_Cat1_Purchased_Goods` | Category 1: Purchased goods and services (iron ore, coal, limestone) | tCO2e | Float |
| `Scope3_Cat4_Upstream_Transport` | Category 4: Upstream transportation and distribution | tCO2e | Float |
| `Scope3_Cat9_Downstream_Transport` | Category 9: Downstream transportation and distribution | tCO2e | Float |
| `Scope3_Cat12_End_of_Life` | Category 12: End-of-life treatment of sold products | tCO2e | Float |
| `Scope3_Measured` | Supplier-provided emissions data | tCO2e | Float |
| `Scope3_Calculated` | Spend-based or activity-based calculations | tCO2e | Float |
| `Scope3_Estimated` | Industry averages and proxy data | tCO2e | Float |

**Coverage:**
- Currently includes 4 of 15 GHG Protocol categories
- Categories 2, 3, 5, 6, 7, 8, 10, 11, 13, 14, 15 excluded as not material (<5% total emissions)

### Aggregated Metrics

| Column | Description | Unit | Data Type |
|--------|-------------|------|-----------|
| `Total_Emissions_tCO2e` | Sum of Scope 1 + Scope 2 + Scope 3 | tCO2e | Float |
| `Emissions_Intensity_tCO2e_per_tonne` | Emissions per tonne of steel produced | tCO2e/tonne | Float |
| `Data_Quality_Score` | Percentage of emissions that are directly measured | % | Float |
| `Reporting_Standard` | Applicable reporting frameworks | - | String |

---

## Emission Factors

### Scope 1: Direct Emissions

| Source | Emission Factor | Unit | Reference |
|--------|----------------|------|-----------|
| Blast furnace (integrated steel) | 0.48 | tCO2e/tonne steel | Swedish Steel Industry Association, 2023 |
| Diesel (auxiliary vehicles) | 2.68 | kg CO2e/liter | IPCC 2006 Guidelines, Volume 2 |
| Natural gas (heating) | 0.184 | kg CO2e/kWh | Swedish Energy Agency, 2024 |

### Scope 2: Indirect Energy Emissions

| Source | Location-Based EF | Market-Based EF | Unit | Reference |
|--------|------------------|----------------|------|-----------|
| Swedish electricity grid | 13 | - | g CO2e/kWh | Swedish Energy Agency, 2024 |
| Renewable electricity (GOs) | - | 8 | g CO2e/kWh | Supplier-specific data |
| District heating (Luleå) | 15 | - | g CO2e/kWh | Luleå Energi, 2024 |

**Notes:**
- Sweden has one of the lowest grid emission factors in Europe due to hydro and nuclear power
- Market-based factor assumes 70% renewable energy certificates (Guarantees of Origin)

### Scope 3: Value Chain Emissions

| Category | Material/Activity | Emission Factor | Unit | Reference |
|----------|-------------------|----------------|------|-----------|
| Cat 1 | Iron ore | 0.05 | tCO2e/tonne | Ecoinvent 3.9, 2023 |
| Cat 1 | Coking coal | 0.15 | tCO2e/tonne | IEA Coal 2023 |
| Cat 1 | Limestone | 0.02 | tCO2e/tonne | USGS, 2023 |
| Cat 4 | Rail freight | 0.022 | kg CO2e/tkm | EN 16258:2012 |
| Cat 4 | Ship freight | 0.011 | kg CO2e/tkm | IMO Fourth GHG Study, 2020 |
| Cat 9 | Road freight (downstream) | 0.062 | kg CO2e/tkm | GLEC Framework, 2023 |
| Cat 12 | Steel recycling | 0.02 | tCO2e/tonne | WorldSteel Association, 2023 |

---

## Data Quality Levels (ESRS E1)

According to ESRS E1 requirements, emissions data is classified by measurement quality:

### Quality Level Definitions

| Level | Definition | Examples |
|-------|------------|----------|
| **Measured** | Direct measurement using calibrated instruments | CEMS, utility meters, scales |
| **Calculated** | Activity data × standard emission factors | Fuel consumption × IPCC EF |
| **Estimated** | Based on proxies, industry averages, or assumptions | Spend-based methods, extrapolations |

### Current Data Quality Distribution

| Scope | Measured | Calculated | Estimated | Total |
|-------|----------|------------|-----------|-------|
| **Scope 1** | 70% | 25% | 5% | 100% |
| **Scope 2** | 90% | 10% | 0% | 100% |
| **Scope 3** | 15% | 25% | 60% | 100% |

**Overall Data Quality Score:** ~47% measured (weighted by emissions volume)

### Quality Improvement Plan

1. **Scope 3 Category 1:** Engage suppliers for primary data (target: 40% measured by 2025)
2. **Scope 3 Category 4:** Request carrier-specific emissions data
3. **Scope 1 Auxiliary:** Install additional metering on diesel tanks

---

## Methodology Notes

### Organizational Boundaries
- **Approach:** Operational control
- **Included:** All facilities where Norrland Stål AB has operational control
- **Excluded:** Joint ventures where control is shared (if any)

### Temporal Boundaries
- **Reporting Period:** Calendar year (January-December)
- **Data Frequency:** Monthly aggregation
- **Vintage:** Emission factors updated annually

### Operational Boundaries

**Scope 1 - Included:**
- Blast furnace operations (iron reduction)
- On-site fuel combustion (heating, generators)
- Company-owned vehicle fleet

**Scope 2 - Included:**
- Purchased electricity for production
- Purchased district heating
- Both location-based and market-based methods reported

**Scope 3 - Included (material categories only):**
- Category 1: Raw material extraction and processing
- Category 4: Inbound logistics
- Category 9: Outbound logistics
- Category 12: End-of-life treatment

**Scope 3 - Excluded (immaterial <5%):**
- Categories 2, 3, 5, 6, 7, 8, 10, 11, 13, 14, 15

### Uncertainties and Limitations

1. **Scope 3 Estimation:** 60% of Scope 3 based on industry averages due to limited supplier data
2. **Seasonal Variation:** Production and emissions vary ±8% due to maintenance schedules
3. **Emission Factor Age:** Some Scope 3 factors are 1-2 years old pending updates
4. **Excluded Categories:** Materiality assessment conducted in 2023, to be reviewed in 2025

---

## ESRS E1 Alignment

This dataset supports the following ESRS E1 disclosure requirements:

| Requirement | Status | Data Coverage |
|-------------|--------|---------------|
| **E1-6:** Gross Scopes 1, 2, 3 and Total GHG emissions | ✓ Complete | All scopes reported |
| **E1-6:** GHG intensity per net revenue | ⚠ Partial | Revenue data not included |
| **E1-6:** GHG intensity per production output | ✓ Complete | tCO2e per tonne steel |
| **E1-6:** Scope 2 location and market-based | ✓ Complete | Both methods provided |
| **E1-6:** Percentage of emissions from regulated schemes | ⚠ Partial | EU ETS data not included |
| **E1-6:** Changes in inventory methodology | N/A | First reporting year |

---

## Contact & Data Governance

**Data Owner:** ESG Reporting Team, Norrland Stål AB
**Last Updated:** January 2024
**Review Frequency:** Quarterly
**Assurance:** Internal review (external assurance planned for 2025)

**Data Usage:**
- This is synthetic data for demonstration purposes
- Emission factors and methodologies reflect real industry practices
- Suitable for Power BI portfolio projects and CSRD implementation training

---

## References

1. GHG Protocol Corporate Accounting and Reporting Standard (Revised Edition, 2015)
2. GHG Protocol Corporate Value Chain (Scope 3) Accounting and Reporting Standard (2011)
3. ESRS E1 Climate Change (European Sustainability Reporting Standard, 2023)
4. IPCC Guidelines for National Greenhouse Gas Inventories (2006, 2019 Refinement)
5. Swedish Energy Agency - Miljövärdering av el och värme (2024)
6. WorldSteel Association - Life Cycle Assessment Methodology Report (2023)
7. IEA - Iron and Steel Technology Roadmap (2023)

---

**Document Version:** 1.0
**Date:** January 2024
**Author:** Victor Ekblom
