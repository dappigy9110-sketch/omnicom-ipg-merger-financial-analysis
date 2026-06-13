import pandas as pd
import matplotlib.pyplot as plt

# Read financial dataset
df = pd.read_csv("data/omnicom_ipg_financials.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Rename Revenue to Comparable_Revenue for a more conservative data definition
df = df.rename(columns={"Revenue": "Comparable_Revenue"})

# Calculate profitability metrics
df["Operating_Margin_%"] = df["Operating_Income"] / df["Comparable_Revenue"] * 100
df["Net_Margin_%"] = df["Net_Income"] / df["Comparable_Revenue"] * 100

# Round numbers for cleaner output
df = df.round(2)

# Print selected columns
print(df[[
    "Company",
    "Year",
    "Comparable_Revenue",
    "Operating_Margin_%",
    "Net_Margin_%"
]])

# Separate Omnicom and IPG data
omnicom = df[df["Company"] == "Omnicom"]
ipg = df[df["Company"] == "IPG"]

# Chart 1: Comparable revenue trend
plt.plot(omnicom["Year"], omnicom["Comparable_Revenue"], marker="o", label="Omnicom")
plt.plot(ipg["Year"], ipg["Comparable_Revenue"], marker="o", label="IPG")

plt.title("Omnicom vs IPG Comparable Revenue Trend")
plt.xlabel("Year")
plt.ylabel("Comparable Revenue")
plt.legend()

plt.savefig("charts/omnicom_ipg_revenue_trend.png")
plt.show()

# Chart 2: Margin trend
plt.figure()

plt.plot(omnicom["Year"], omnicom["Operating_Margin_%"], marker="o", label="Omnicom Operating Margin")
plt.plot(ipg["Year"], ipg["Operating_Margin_%"], marker="o", label="IPG Operating Margin")
plt.plot(omnicom["Year"], omnicom["Net_Margin_%"], marker="o", label="Omnicom Net Margin")
plt.plot(ipg["Year"], ipg["Net_Margin_%"], marker="o", label="IPG Net Margin")

plt.title("Omnicom vs IPG Margin Trend")
plt.xlabel("Year")
plt.ylabel("Margin (%)")
plt.legend()

plt.savefig("charts/omnicom_ipg_margin_trend.png")
plt.show()

# Combined comparable revenue
combined_revenue = df.groupby("Year")["Comparable_Revenue"].sum().reset_index()

print(combined_revenue)

# Chart 3: Combined comparable revenue trend
plt.figure()

plt.plot(combined_revenue["Year"], combined_revenue["Comparable_Revenue"], marker="o")

plt.title("Combined Comparable Revenue Trend")
plt.xlabel("Year")
plt.ylabel("Combined Comparable Revenue")

plt.savefig("charts/combined_revenue_trend.png")
plt.show()

# Export analysis outputs
df.to_csv("data/omnicom_ipg_analysis_output.csv", index=False)
combined_revenue.to_csv("data/combined_revenue_output.csv", index=False)