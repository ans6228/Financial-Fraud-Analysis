

import pandas as pd
df= pd.read_csv("transactions.csv")
print(df.head())
print (df.columns)
print(len(df))
print(df.info())

print(df["type"]. value_counts())
print(df.groupby("type")["amount"].sum())
print(df.groupby("type")["amount"].mean())

import matplotlib.pyplot as plt
transaction_counts = df["type"].value_counts()
transaction_counts.plot(kind="bar")
plt.title( "Transactions Number by Type")
plt.xlabel("Type")
plt.ylabel(" Transactions Number")
plt.xticks(rotation=0)
from matplotlib.ticker import StrMethodFormatter
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
plt.show()

fraud_counts = df["isFraud"].value_counts()
print(fraud_counts)
fraud_percent = df["isFraud"].mean() * 100
print(f"Fraud Percentage: {fraud_percent:.4f}%")

fraud_transactions = df[df["isFraud"] == 1]
fraud_by_type = fraud_transactions["type"].value_counts()
print(fraud_by_type)

fraud_by_type.plot(kind="bar")
plt.title("Fraudulent Transactions by Transaction Type")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Fraudulent Transactions")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
