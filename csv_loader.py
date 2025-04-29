
import pandas as pd
from datetime import datetime

def load_transactions(csv_file_path):
    df = pd.read_csv(csv_file_path)
    transactions = []

    for _, row in df.iterrows():
        transaction = {
            "date": datetime.strptime(row['Date'], '%Y-%m-%d'),
            "merchant": row['Merchant'],
            "amount": float(row['Amount']),
            "category": row['Category'],
            "description": row['Description']
        }
        transactions.append(transaction)
    
    return transactions

# Example usage
if __name__ == "__main__":
    transactions = load_transactions("sample_transactions.csv")
    for tx in transactions:
        print(tx)
