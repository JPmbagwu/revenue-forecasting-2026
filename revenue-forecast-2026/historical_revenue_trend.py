#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 10:23:20 2025

@author: johnpaulmbagwu
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for cleaner look
sns.set(style="whitegrid")

# Historical data from the task
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

df_hist = pd.DataFrame({'Quarter': quarters, 'Revenue ($M)': revenue})

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_hist, x='Quarter', y='Revenue ($M)', marker='o', linewidth=2, color='#0070F3')
plt.title('Historical Quarterly Revenue Trend (2020–2025)', fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.ylabel('Revenue ($M)')
plt.tight_layout()
plt.savefig('historical_revenue_trend.png', dpi=300)
plt.show()  # This will display it if you're in a notebook