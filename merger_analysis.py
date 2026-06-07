import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/omnicom_ipg_financials.csv")

df["Operating_Margin_%"] = df["Operating_Income"] / df["Revenue"] * 100
df["Net_Margin_%"] = df["Net_Income"] / df["Revenue"] * 100

df = df.round(2)

print(df[[
    "Company",
    "Year",
    "Revenue",
    "Operating_Margin_%",
    "Net_Margin_%"
]])
omnicom = df[df["Company"] == "Omnicom"]
ipg = df[df["Company"] == "IPG"]

plt.plot(omnicom["Year"], omnicom["Revenue"], marker="o", label="Omnicom")
plt.plot(ipg["Year"], ipg["Revenue"], marker="o", label="IPG")

plt.title("Omnicom vs IPG Revenue Trend")
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.legend()

plt.savefig("charts/omnicom_ipg_revenue_trend.png")
plt.show()
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
combined_revenue = df.groupby("Year")["Revenue"].sum().reset_index()

print(combined_revenue)
plt.figure()

plt.plot(combined_revenue["Year"], combined_revenue["Revenue"], marker="o")

plt.title("Combined Revenue Trend")
plt.xlabel("Year")
plt.ylabel("Combined Revenue")

plt.savefig("charts/combined_revenue_trend.png")
plt.show()
df.to_csv("data/omnicom_ipg_analysis_output.csv", index=False)
combined_revenue.to_csv("data/combined_revenue_output.csv", index=False)