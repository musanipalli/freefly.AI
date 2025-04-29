
def categorize_transactions(transactions):
    category_rules = {
        "Subscription": ["Netflix", "Spotify", "Hulu"],
        "Coffee": ["Starbucks", "Dunkin"],
        "Shopping": ["Amazon", "Walmart", "Target"],
        "Transport": ["Uber", "Lyft"],
        "Groceries": ["Whole Foods", "Grocery Store", "Safeway", "Kroger"],
        "Dining": ["Uber Eats", "DoorDash", "Grubhub"],
        "Utilities": ["AT&T", "Verizon", "Comcast"],
    }

    for tx in transactions:
        matched = False
        merchant = tx['merchant'].lower()
        
        # Try to categorize based on rules
        for category, keywords in category_rules.items():
            for keyword in keywords:
                if keyword.lower() in merchant:
                    tx['category'] = category
                    matched = True
                    break
            if matched:
                break

        # If still not categorized, set as 'Other'
        if not tx.get('category'):
            tx['category'] = 'Other'

    return transactions

# Example usage
if __name__ == "__main__":
    from csv_loader import load_transactions
    transactions = load_transactions("sample_transactions.csv")
    categorized = categorize_transactions(transactions)
    for tx in categorized:
        print(tx)
