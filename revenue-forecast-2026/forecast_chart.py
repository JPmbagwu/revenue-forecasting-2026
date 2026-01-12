#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 10:30:54 2025

@author: johnpaulmbagwu
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set a clean style
sns.set(style="whitegrid")

# === Historical data (2020–2025) ===
quarters = [
    'Q1 2020', 'Q2 2020', 'Q3 2020', 'Q4 2020',
    'Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021',
    'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022',
    'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023',
    'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024',
    'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025'
]

revenue = [
    18.2, 16.8, 19.5, 22.1,
    23.8, 25.4, 27.1, 29.3,
    30.2, 31.8, 33.5, 35.7,
    36.9, 38.4, 40.2, 42.6,
    44.1, 46.3, 48.7, 51.2,
    53.0, 55.4, 58.1, 61.3
]

# === Generate historical_revenue_trend.png ===
df_hist = pd.DataFrame({'Quarter': quarters, 'Revenue ($M)': revenue})

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_hist, x='Quarter', y='Revenue ($M)', marker='o', linewidth=2, color='#0070F3')
plt.title('Historical Quarterly Revenue Trend (2020–2025)', fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.ylabel('Revenue ($M)')
plt.tight_layout()
plt.savefig('historical_revenue_trend.png', dpi=300)
plt.close()  # Close to avoid displaying if running as script

print("Saved: historical_revenue_trend.png")

# === 2026 forecast data ===
quarters_forecast = ['Q1 2026', 'Q2 2026', 'Q3 2026', 'Q4 2026']
base_forecast = [64.2, 67.1, 70.5, 78.2]
low_80 = [61.8, 64.0, 66.8, 73.4]   # ~10th percentile
high_80 = [66.9, 70.5, 74.8, 83.1]  # ~90th percentile

# Combine historical + forecast
all_quarters = quarters + quarters_forecast
revenue_all = revenue + base_forecast

df_full = pd.DataFrame({
    'Quarter': all_quarters,
    'Revenue': revenue_all,
    'Low': [np.nan] * len(revenue) + low_80,
    'High': [np.nan] * len(revenue) + high_80,
    'Type': ['Historical'] * len(revenue) + ['Forecast'] * len(quarters_forecast)
})

# === Generate forecast_chart.png ===
plt.figure(figsize=(14, 7))

# Historical line
sns.lineplot(data=df_full[df_full['Type'] == 'Historical'], x='Quarter', y='Revenue',
             marker='o', linewidth=3, color='#0070F3', label='Historical')

# Forecast line (dashed)
sns.lineplot(data=df_full[df_full['Type'] == 'Forecast'], x='Quarter', y='Revenue',
             marker='o', linewidth=3, color='#0070F3', linestyle='--', label='2026 Forecast')

# 80% confidence band
plt.fill_between(quarters_forecast, low_80, high_80, color='#0070F3', alpha=0.2, label='80% Confidence Interval')

plt.title('Revenue Forecast: Historical + 2026 Projection', fontsize=16)
plt.ylabel('Revenue ($M)')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.savefig('forecast_chart.png', dpi=300)
plt.close()

print("Saved: forecast_chart.png")