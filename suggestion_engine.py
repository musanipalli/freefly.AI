
from collections import defaultdict

def generate_savings_suggestions(transactions):
    suggestions = []

    category_totals = defaultdict(float)
    subscription_merchants = set()
    big_purchases = []

    for tx in transactions:
        category_totals[tx['category']] += tx['amount']
        if tx['category'] == 'Subscription':
            subscription_merchants.add(tx['merchant'])
        if tx['amount'] > 300:
            big_purchases.append(tx)

    # Rule 1: Multiple subscriptions
    if len(subscription_merchants) >= 2:
        suggestions.append({
            "text": f"You have {len(subscription_merchants)} active subscriptions ({', '.join(subscription_merchants)}). Consider canceling one to save $10-15/month.",
            "potential_savings": 120.0  # approx yearly
        })

    # Rule 2: High dining out
    if category_totals.get('Dining', 0) > 200:
        savings = category_totals['Dining'] * 0.2  # Recommend reducing by 20%
        suggestions.append({
            "text": f"You spent ${category_totals['Dining']:.2f} on Dining this month. Reducing by 20% could save about ${savings:.2f} monthly.",
            "potential_savings": savings
        })

    # Rule 3: Big one-time purchases
    for tx in big_purchases:
        suggestions.append({
            "text": f"Large purchase detected: {tx['merchant']} - ${tx['amount']:.2f}. Consider reviewing necessity or payment options.",
            "potential_savings": 0.0  # Hard to quantify
        })

    return suggestions

# Example usage
if __name__ == "__main__":
    from csv_loader import load_transactions
    from categorizer import categorize_transactions

    transactions = load_transactions("sample_transactions.csv")
    categorized = categorize_transactions(transactions)
    suggestions = generate_savings_suggestions(categorized)

    for sug in suggestions:
        print(sug)
