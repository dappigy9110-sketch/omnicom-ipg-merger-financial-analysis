import pandas as pd
import matplotlib.pyplot as plt

apple_df = pd.read_csv("data/apple_financials.csv")
apple_df = apple_df.sort_values("Year")

apple_df["Gross_Margin"] = apple_df["Gross_Profit"] / apple_df["Revenue"]
apple_df["Operating_Margin"] = apple_df["Operating_Income"] / apple_df["Revenue"]
apple_df["Net_Margin"] = apple_df["Net_Income"] / apple_df["Revenue"]

apple_df["Gross_Margin_%"] = apple_df["Gross_Margin"] * 100
apple_df["Operating_Margin_%"] = apple_df["Operating_Margin"] * 100
apple_df["Net_Margin_%"] = apple_df["Net_Margin"] * 100
apple_df["Revenue_Growth_%"] = apple_df["Revenue"].pct_change() * 100
apple_df = apple_df.round(2)

print(apple_df[[
    "Year",
    "Revenue",
    "Revenue_Growth_%",
    "Gross_Margin_%",
    "Operating_Margin_%",
    "Net_Margin_%"
]])
apple_df.to_csv("data/apple_financial_analysis_output.csv", index=False)
plt.plot(apple_df["Year"], apple_df["Revenue"], marker="o")

plt.title("Apple Revenue Trend")
plt.xlabel("Year")
plt.ylabel("Revenue (Million USD)")

plt.savefig("charts/apple_revenue_trend.png")
plt.show()
plt.figure()

plt.plot(apple_df["Year"], apple_df["Gross_Margin_%"], marker="o", label="Gross Margin %")
plt.plot(apple_df["Year"], apple_df["Operating_Margin_%"], marker="o", label="Operating Margin %")
plt.plot(apple_df["Year"], apple_df["Net_Margin_%"], marker="o", label="Net Margin %")

plt.title("Apple Margin Trend")
plt.xlabel("Year")
plt.ylabel("Margin (%)")
plt.legend()

plt.savefig("charts/apple_margin_trend.png")
plt.show()