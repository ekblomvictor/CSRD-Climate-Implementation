"""
CSRD Climate Visualization Generator
=====================================
Creates professional business charts from Norrland Stål AB emissions data
for portfolio presentation and Power BI integration.

Generates:
1. Stacked bar chart - Monthly emissions by Scope
2. Line chart - Emissions intensity trend with target
3. Pie chart - Data quality distribution

Author: Victor Ekblom
Date: 2024
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path

# Set style
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

# Professional color palette
COLORS = {
    'scope1': '#D32F2F',      # Red - Direct emissions
    'scope2': '#1976D2',      # Blue - Energy indirect
    'scope3': '#388E3C',      # Green - Value chain
    'target': '#FF6F00',      # Orange - Target line
    'measured': '#2E7D32',    # Dark green
    'calculated': '#FFA726',  # Orange
    'estimated': '#EF5350'    # Light red
}


def load_data(file_path):
    """Load emissions data from Excel file"""
    try:
        df = pd.read_excel(file_path, sheet_name='Emissions_Data')
        print(f"[OK] Loaded {len(df)} rows of emissions data")
        return df
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        print("Please run generate_mock_data.py first to create the Excel file.")
        return None
    except Exception as e:
        print(f"[ERROR] Failed to load data: {e}")
        return None


def create_stacked_bar_chart(df, output_path):
    """
    Chart 1: Monthly emissions by Scope (Stacked Bar Chart)
    Shows Scope 1, 2, 3 emissions over time
    """
    fig, ax = plt.subplots(figsize=(14, 6))

    # Prepare data
    x = range(len(df))
    scope1 = df['Scope1_Total_tCO2e']
    scope2 = df['Scope2_Total_tCO2e']
    scope3 = df['Scope3_Total_tCO2e']

    # Create stacked bars
    width = 0.8
    ax.bar(x, scope1, width, label='Scope 1: Direct Emissions',
           color=COLORS['scope1'], alpha=0.9)
    ax.bar(x, scope2, width, bottom=scope1, label='Scope 2: Energy Indirect',
           color=COLORS['scope2'], alpha=0.9)
    ax.bar(x, scope3, width, bottom=scope1+scope2, label='Scope 3: Value Chain',
           color=COLORS['scope3'], alpha=0.9)

    # Formatting
    ax.set_xlabel('Month', fontsize=12, fontweight='bold')
    ax.set_ylabel('GHG Emissions (tCO₂e)', fontsize=12, fontweight='bold')
    ax.set_title('Monthly GHG Emissions by Scope - Norrland Stål AB',
                 fontsize=14, fontweight='bold', pad=20)

    # X-axis labels
    ax.set_xticks(x[::2])  # Show every other month
    ax.set_xticklabels(df['Date'].iloc[::2], rotation=45, ha='right')

    # Legend
    ax.legend(loc='upper left', framealpha=0.95, fontsize=10)

    # Grid
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Format y-axis
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))

    # Add totals annotation
    total_emissions = df['Total_Emissions_tCO2e'].sum()
    ax.text(0.98, 0.98, f'Total 24-month emissions: {total_emissions:,.0f} tCO₂e',
            transform=ax.transAxes, fontsize=9, verticalalignment='top',
            horizontalalignment='right', bbox=dict(boxstyle='round',
            facecolor='wheat', alpha=0.8))

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Created: {output_path}")


def create_intensity_trend_chart(df, output_path):
    """
    Chart 2: Emissions Intensity Trend (Line Chart)
    Shows tCO2e per tonne steel with target line
    """
    fig, ax = plt.subplots(figsize=(14, 6))

    # Prepare data
    x = range(len(df))
    intensity = df['Emissions_Intensity_tCO2e_per_tonne']

    # Plot actual intensity
    ax.plot(x, intensity, marker='o', linewidth=2.5, markersize=6,
            color=COLORS['scope1'], label='Actual Emissions Intensity',
            alpha=0.9)

    # Add target line (0.70 tCO2e/tonne by 2030)
    target = 0.70
    ax.axhline(y=target, color=COLORS['target'], linestyle='--',
               linewidth=2, label=f'2030 Target: {target} tCO₂e/tonne',
               alpha=0.8)

    # Calculate and show trend
    z = np.polyfit(x, intensity, 1)
    p = np.poly1d(z)
    ax.plot(x, p(x), linestyle=':', linewidth=2, color='gray',
            label='Linear Trend', alpha=0.6)

    # Formatting
    ax.set_xlabel('Month', fontsize=12, fontweight='bold')
    ax.set_ylabel('Emissions Intensity (tCO₂e per tonne steel)',
                  fontsize=12, fontweight='bold')
    ax.set_title('Emissions Intensity Trend - Norrland Stål AB',
                 fontsize=14, fontweight='bold', pad=20)

    # X-axis labels
    ax.set_xticks(x[::2])
    ax.set_xticklabels(df['Date'].iloc[::2], rotation=45, ha='right')

    # Legend
    ax.legend(loc='upper right', framealpha=0.95, fontsize=10)

    # Grid
    ax.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add statistics box
    avg_intensity = intensity.mean()
    min_intensity = intensity.min()
    max_intensity = intensity.max()

    stats_text = f'Average: {avg_intensity:.3f} tCO₂e/t\n'
    stats_text += f'Range: {min_intensity:.3f} - {max_intensity:.3f}\n'
    stats_text += f'Gap to target: {avg_intensity - target:.3f} tCO₂e/t'

    ax.text(0.02, 0.98, stats_text,
            transform=ax.transAxes, fontsize=9, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

    # Highlight target zone
    ax.fill_between(x, 0, target, alpha=0.1, color=COLORS['target'],
                     label='Target Zone')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Created: {output_path}")


def create_data_quality_chart(df, output_path):
    """
    Chart 3: Data Quality Distribution (Pie Chart)
    Shows percentage of measured, calculated, and estimated data
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Overall data quality
    total_measured = (df['Scope1_Measured'].sum() +
                     df['Scope2_Measured'].sum() +
                     df['Scope3_Measured'].sum())
    total_calculated = (df['Scope1_Calculated'].sum() +
                       df['Scope2_Calculated'].sum() +
                       df['Scope3_Calculated'].sum())
    total_estimated = (df['Scope1_Estimated'].sum() +
                      df['Scope2_Estimated'].sum() +
                      df['Scope3_Estimated'].sum())

    total_all = total_measured + total_calculated + total_estimated

    # Pie chart 1: Overall data quality
    sizes1 = [total_measured, total_calculated, total_estimated]
    labels1 = ['Measured\n(Direct instrumentation)',
               'Calculated\n(Activity × EF)',
               'Estimated\n(Proxies/assumptions)']
    colors1 = [COLORS['measured'], COLORS['calculated'], COLORS['estimated']]
    explode1 = (0.05, 0, 0)  # Highlight measured

    wedges1, texts1, autotexts1 = ax1.pie(sizes1, explode=explode1, labels=labels1,
                                            colors=colors1, autopct='%1.1f%%',
                                            shadow=True, startangle=90,
                                            textprops={'fontsize': 10})

    # Make percentage text bold
    for autotext in autotexts1:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(11)

    ax1.set_title('Overall Data Quality Distribution\n(All Scopes Combined)',
                  fontsize=12, fontweight='bold', pad=20)

    # Pie chart 2: Data quality by scope
    scope_quality = {
        'Scope 1\nMeasured': df['Scope1_Measured'].sum(),
        'Scope 1\nCalculated': df['Scope1_Calculated'].sum(),
        'Scope 1\nEstimated': df['Scope1_Estimated'].sum(),
        'Scope 2\nMeasured': df['Scope2_Measured'].sum(),
        'Scope 2\nCalculated': df['Scope2_Calculated'].sum(),
        'Scope 3\nMeasured': df['Scope3_Measured'].sum(),
        'Scope 3\nCalculated': df['Scope3_Calculated'].sum(),
        'Scope 3\nEstimated': df['Scope3_Estimated'].sum(),
    }

    # Filter out zero values
    scope_quality = {k: v for k, v in scope_quality.items() if v > 0}

    labels2 = list(scope_quality.keys())
    sizes2 = list(scope_quality.values())

    # Color mapping by scope
    colors2 = []
    for label in labels2:
        if 'Scope 1' in label:
            if 'Measured' in label:
                colors2.append('#C62828')
            elif 'Calculated' in label:
                colors2.append('#E57373')
            else:
                colors2.append('#FFCDD2')
        elif 'Scope 2' in label:
            if 'Measured' in label:
                colors2.append('#1565C0')
            else:
                colors2.append('#64B5F6')
        else:  # Scope 3
            if 'Measured' in label:
                colors2.append('#2E7D32')
            elif 'Calculated' in label:
                colors2.append('#66BB6A')
            else:
                colors2.append('#A5D6A7')

    wedges2, texts2, autotexts2 = ax2.pie(sizes2, labels=labels2, colors=colors2,
                                            autopct='%1.0f%%', startangle=90,
                                            textprops={'fontsize': 8})

    for autotext in autotexts2:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)

    ax2.set_title('Data Quality by Scope\n(ESRS E1 Breakdown)',
                  fontsize=12, fontweight='bold', pad=20)

    # Add summary text
    quality_score = (total_measured / total_all) * 100
    summary_text = f'Data Quality Score: {quality_score:.1f}%\n'
    summary_text += f'(Measured data as % of total emissions)\n\n'
    summary_text += f'Total emissions: {total_all:,.0f} tCO₂e\n'
    summary_text += f'Measured: {total_measured:,.0f} tCO₂e\n'
    summary_text += f'Calculated: {total_calculated:,.0f} tCO₂e\n'
    summary_text += f'Estimated: {total_estimated:,.0f} tCO₂e'

    fig.text(0.5, 0.02, summary_text, ha='center', fontsize=9,
             bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))

    plt.suptitle('Data Quality Assessment - Norrland Stål AB (ESRS E1)',
                 fontsize=14, fontweight='bold', y=0.98)

    plt.tight_layout(rect=[0, 0.1, 1, 0.96])
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Created: {output_path}")


def main():
    """Main execution function"""
    print("=" * 60)
    print("CSRD Climate Visualization Generator")
    print("=" * 60)

    # Setup paths
    script_dir = Path(__file__).parent
    data_path = script_dir.parent / 'data' / 'norrland_stal_emissions.xlsx'
    output_dir = script_dir.parent / 'powerbi' / 'screenshots'

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n[OK] Output directory: {output_dir}")

    # Load data
    print(f"\nLoading data from: {data_path}")
    df = load_data(data_path)

    if df is None:
        print("\n[ERROR] Cannot proceed without data. Exiting.")
        return

    # Generate visualizations
    print("\n" + "=" * 60)
    print("Generating visualizations...")
    print("=" * 60)

    # Import numpy here for trend calculation
    import numpy as np
    globals()['np'] = np

    # Chart 1: Stacked bar chart
    print("\n[1/3] Creating stacked bar chart...")
    chart1_path = output_dir / 'emissions_by_scope_stacked.png'
    create_stacked_bar_chart(df, chart1_path)

    # Chart 2: Intensity trend
    print("\n[2/3] Creating emissions intensity trend...")
    chart2_path = output_dir / 'emissions_intensity_trend.png'
    create_intensity_trend_chart(df, chart2_path)

    # Chart 3: Data quality
    print("\n[3/3] Creating data quality distribution...")
    chart3_path = output_dir / 'data_quality_distribution.png'
    create_data_quality_chart(df, chart3_path)

    # Summary
    print("\n" + "=" * 60)
    print("[SUCCESS] All visualizations created!")
    print("=" * 60)
    print(f"\nOutput files:")
    print(f"1. {chart1_path.name}")
    print(f"2. {chart2_path.name}")
    print(f"3. {chart3_path.name}")
    print(f"\nLocation: {output_dir}")
    print("\n[NOTE] Images are 300 DPI and ready for:")
    print("  - Power BI import")
    print("  - Portfolio presentations")
    print("  - LinkedIn/GitHub showcase")
    print("  - ESG reporting documents")


if __name__ == "__main__":
    main()
