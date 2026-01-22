"""
CSRD Climate Data Generator for Norrland Stål AB
================================================
Generates synthetic GHG emissions data aligned with:
- GHG Protocol (Scope 1, 2, 3)
- ESRS E1 Climate Change requirements
- Swedish steel industry benchmarks

Author: Victor Ekblom
Date: 2024
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Set random seed for reproducibility
np.random.seed(42)


def generate_emissions_data():
    """Generate 24 months of realistic emissions data for Swedish steel company"""

    # Company profile
    company_info = {
        'company_name': 'Norrland Stål AB',
        'industry': 'Steel Manufacturing (NACE C24.10)',
        'location': 'Luleå, Sweden',
        'reporting_period': '2023-2024',
        'production_capacity': '500,000 tonnes steel/year'
    }

    # Generate monthly dates
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=30*i) for i in range(24)]

    # Initialize data lists
    data = []

    for i, date in enumerate(dates):
        month = date.month

        # Seasonal factors (winter = higher energy use)
        seasonal_factor = 1.0 + 0.15 * np.cos(2 * np.pi * (month - 1) / 12)

        # Production volume (tonnes steel/month, with realistic variation)
        base_production = 41667  # ~500k tonnes/year
        production = base_production * (0.95 + np.random.uniform(-0.08, 0.08)) * seasonal_factor

        # =====================================
        # SCOPE 1: Direct emissions (tCO2e)
        # =====================================
        # Blast furnace operations: ~0.5 tCO2/tonne steel (Swedish benchmark)
        scope1_base = 20000  # tCO2e/month baseline
        scope1_blast_furnace = production * 0.48 * (0.98 + np.random.uniform(-0.05, 0.05))
        scope1_auxiliary = 800 + np.random.uniform(-100, 100)  # Auxiliary combustion
        scope1_total = scope1_blast_furnace + scope1_auxiliary

        # =====================================
        # SCOPE 2: Indirect emissions (tCO2e)
        # =====================================
        # Swedish electricity grid: ~13 g CO2/kWh (highly renewable)
        electricity_kwh = production * 650  # kWh per tonne steel
        scope2_location = electricity_kwh * 0.000013  # Location-based (grid average)
        scope2_market = electricity_kwh * 0.000008    # Market-based (renewable contracts)

        # District heating (Swedish low-carbon heat)
        heating_mwh = 2500 + np.random.uniform(-300, 300)
        scope2_heating = heating_mwh * 0.015  # tCO2e (biofuel-based district heating)

        scope2_total = scope2_location + scope2_heating

        # =====================================
        # SCOPE 3: Value chain emissions (tCO2e)
        # =====================================
        # Category 1: Purchased goods (iron ore, coal, limestone)
        iron_ore_tonnes = production * 1.6
        scope3_cat1_ore = iron_ore_tonnes * 0.05  # 0.05 tCO2e per tonne ore

        coal_tonnes = production * 0.4
        scope3_cat1_coal = coal_tonnes * 0.15  # 0.15 tCO2e per tonne coal

        limestone_tonnes = production * 0.2
        scope3_cat1_limestone = limestone_tonnes * 0.02

        scope3_cat1 = scope3_cat1_ore + scope3_cat1_coal + scope3_cat1_limestone

        # Category 4: Upstream transportation
        transport_tkm = (iron_ore_tonnes + coal_tonnes) * 500  # tonne-kilometers
        scope3_cat4 = transport_tkm * 0.00012  # 0.12 kg CO2e per tkm (rail/ship)

        # Category 9: Downstream transportation
        scope3_cat9 = production * 0.05  # Distribution to customers

        # Category 12: End-of-life treatment
        scope3_cat12 = production * 0.02  # Steel recycling/disposal

        scope3_total = scope3_cat1 + scope3_cat4 + scope3_cat9 + scope3_cat12

        # =====================================
        # Data Quality Assessment (ESRS E1)
        # =====================================
        # Scope 1: 70% measured, 25% calculated, 5% estimated
        scope1_measured = scope1_total * 0.70
        scope1_calculated = scope1_total * 0.25
        scope1_estimated = scope1_total * 0.05

        # Scope 2: 90% measured, 10% calculated
        scope2_measured = scope2_total * 0.90
        scope2_calculated = scope2_total * 0.10
        scope2_estimated = 0

        # Scope 3: 15% measured, 25% calculated, 60% estimated
        scope3_measured = scope3_total * 0.15
        scope3_calculated = scope3_total * 0.25
        scope3_estimated = scope3_total * 0.60

        # Total emissions
        total_emissions = scope1_total + scope2_total + scope3_total

        # Emissions intensity
        intensity = total_emissions / production  # tCO2e per tonne steel

        # Append row
        data.append({
            'Date': date.strftime('%Y-%m'),
            'Year': date.year,
            'Month': date.month,
            'Month_Name': date.strftime('%B'),

            # Production
            'Production_Tonnes': round(production, 2),

            # Scope 1
            'Scope1_Total_tCO2e': round(scope1_total, 2),
            'Scope1_Blast_Furnace': round(scope1_blast_furnace, 2),
            'Scope1_Auxiliary': round(scope1_auxiliary, 2),
            'Scope1_Measured': round(scope1_measured, 2),
            'Scope1_Calculated': round(scope1_calculated, 2),
            'Scope1_Estimated': round(scope1_estimated, 2),

            # Scope 2
            'Scope2_Total_tCO2e': round(scope2_total, 2),
            'Scope2_Electricity_kWh': round(electricity_kwh, 0),
            'Scope2_Location_Based': round(scope2_location, 2),
            'Scope2_Market_Based': round(scope2_market, 2),
            'Scope2_Heating': round(scope2_heating, 2),
            'Scope2_Measured': round(scope2_measured, 2),
            'Scope2_Calculated': round(scope2_calculated, 2),
            'Scope2_Estimated': round(scope2_estimated, 2),

            # Scope 3
            'Scope3_Total_tCO2e': round(scope3_total, 2),
            'Scope3_Cat1_Purchased_Goods': round(scope3_cat1, 2),
            'Scope3_Cat4_Upstream_Transport': round(scope3_cat4, 2),
            'Scope3_Cat9_Downstream_Transport': round(scope3_cat9, 2),
            'Scope3_Cat12_End_of_Life': round(scope3_cat12, 2),
            'Scope3_Measured': round(scope3_measured, 2),
            'Scope3_Calculated': round(scope3_calculated, 2),
            'Scope3_Estimated': round(scope3_estimated, 2),

            # Totals & Intensity
            'Total_Emissions_tCO2e': round(total_emissions, 2),
            'Emissions_Intensity_tCO2e_per_tonne': round(intensity, 3),

            # Metadata
            'Data_Quality_Score': round(
                (scope1_measured + scope2_measured + scope3_measured) / total_emissions * 100, 1
            ),
            'Reporting_Standard': 'GHG Protocol + ESRS E1',
        })

    return pd.DataFrame(data), company_info


def create_excel_report(df, company_info, output_path):
    """Create formatted Excel workbook with multiple sheets"""

    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        # Sheet 1: Main emissions data
        df.to_excel(writer, sheet_name='Emissions_Data', index=False)

        # Sheet 2: Company information
        company_df = pd.DataFrame([company_info]).T
        company_df.columns = ['Value']
        company_df.to_excel(writer, sheet_name='Company_Info')

        # Sheet 3: Monthly summary
        summary = df.groupby('Year').agg({
            'Production_Tonnes': 'sum',
            'Scope1_Total_tCO2e': 'sum',
            'Scope2_Total_tCO2e': 'sum',
            'Scope3_Total_tCO2e': 'sum',
            'Total_Emissions_tCO2e': 'sum',
            'Emissions_Intensity_tCO2e_per_tonne': 'mean'
        }).round(2)
        summary.to_excel(writer, sheet_name='Annual_Summary')

        # Sheet 4: Data quality breakdown
        quality_data = []
        for scope in [1, 2, 3]:
            measured = df[f'Scope{scope}_Measured'].sum()
            calculated = df[f'Scope{scope}_Calculated'].sum()
            estimated = df[f'Scope{scope}_Estimated'].sum()
            total = measured + calculated + estimated

            quality_data.append({
                'Scope': f'Scope {scope}',
                'Measured_tCO2e': round(measured, 2),
                'Measured_Percent': round(measured/total*100, 1),
                'Calculated_tCO2e': round(calculated, 2),
                'Calculated_Percent': round(calculated/total*100, 1),
                'Estimated_tCO2e': round(estimated, 2),
                'Estimated_Percent': round(estimated/total*100, 1),
                'Total_tCO2e': round(total, 2)
            })

        quality_df = pd.DataFrame(quality_data)
        quality_df.to_excel(writer, sheet_name='Data_Quality', index=False)

    print(f"\n[OK] Excel report created: {output_path}")


def main():
    """Main execution function"""
    print("=" * 60)
    print("CSRD Climate Data Generator - Norrland Stål AB")
    print("=" * 60)

    # Generate data
    print("\nGenerating synthetic emissions data...")
    df, company_info = generate_emissions_data()

    # Display summary statistics
    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS (24 months)")
    print("=" * 60)
    print(f"\nCompany: {company_info['company_name']}")
    print(f"Location: {company_info['location']}")
    print(f"Industry: {company_info['industry']}")

    print(f"\nTotal Production: {df['Production_Tonnes'].sum():,.0f} tonnes")
    print(f"\nScope 1 Emissions: {df['Scope1_Total_tCO2e'].sum():,.0f} tCO2e")
    print(f"Scope 2 Emissions: {df['Scope2_Total_tCO2e'].sum():,.0f} tCO2e")
    print(f"Scope 3 Emissions: {df['Scope3_Total_tCO2e'].sum():,.0f} tCO2e")
    print(f"Total Emissions: {df['Total_Emissions_tCO2e'].sum():,.0f} tCO2e")

    print(f"\nAverage Emissions Intensity: {df['Emissions_Intensity_tCO2e_per_tonne'].mean():.3f} tCO2e/tonne")
    print(f"Data Quality Score: {df['Data_Quality_Score'].mean():.1f}%")

    # Create output directory if needed
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(output_dir, exist_ok=True)

    # Save to Excel
    output_path = os.path.join(output_dir, 'norrland_stal_emissions.xlsx')
    create_excel_report(df, company_info, output_path)

    print("\n" + "=" * 60)
    print("[SUCCESS] Data generation complete!")
    print("=" * 60)
    print(f"\nOutput file: {output_path}")
    print("\nNext steps:")
    print("1. Review data in Excel")
    print("2. Import to Power BI for visualization")
    print("3. Validate against ESRS E1 requirements")


if __name__ == "__main__":
    main()
