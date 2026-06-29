# Financial-Fraud-Analysis

 Project Overview:
 This project analyzes over 6.3 million financial transactions using Python to identify fraud patterns and explore transaction behavior. The analysis uses pandas for data manipulation and Matplotlib for data visualization.

 Business Question:
 Which transaction types dominate financial activity, and which transaction types are most vulnerable to fraud?

 Dataset:
- Synthetic Financial Dataset (Kaggle)
- 6,362,620 transactions
- 11 variables
- Includes transaction type, amount, account balances, and fraud indicators

 Tools Used:
- Python
- pandas
- Matplotlib

Analysis Performed:
- Explored transaction types
- Calculated the percentage/amount of fraudulent transactions
- Identified which transaction types experienced fraud

Key Findings:
- Transaction volume varied across transaction types.
- Fraud represented approximately 0.13% (0.1291) of all transactions.
- Fraudulent activity was concentrated in specific transaction types rather than evenly distributed.
- All fraudulent activity was seen in "Cash Out" and "Transfer" transaction types with cashout being 4116 and transfer being 4097. Suggesting that transactions dealing with moving money out of accounts were more high risk.

Business Recommendation:
The analysis suggests that fraud is not evenly distributed across all transaction types. Financial institutions should tailor fraud detection rules based on transaction type rather than applying the same level of monitoring across every transaction. This targeted approach can improve detection accuracy and optimize the use of fraud prevention resources.

Project Visualizations:

Transaction Types

![Transaction Types](transaction_types.png)


