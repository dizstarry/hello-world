import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

# Load your own dataset named 'sales_summary' from a CSV file
sales_summary = pd.read_csv('sales_summary.csv')

# Replace NaN or Inf values in 'Monthly Change (%)' with a placeholder (e.g., 0)
sales_summary['Monthly Change (%)'].replace([np.nan, np.inf, -np.inf], 0, inplace=True)

# Create a relplot
sns.relplot(data=sales_summary, kind="line", x="Total Sales", y="Monthly Change (%)", hue="Month", sort=False, linewidth=2.5)

# Adjust x-axis limits as needed
plt.xlim(3000, max(sales_summary["Total Sales"]))

# Adjust y-axis limits as needed
plt.ylim(-100, max(sales_summary["Monthly Change (%)"]))

# Show the relplot
plt.show()

