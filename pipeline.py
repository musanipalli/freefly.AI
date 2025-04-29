from prefect import task, flow
from sqlalchemy.orm import Session
from data_models import Suggestion

@task
def fetch_transactions(user_id: int) -> list[dict]:
    # TODO: integrate Plaid / CSV loader
    return []

@task
def clean_transactions(raw_transactions: list[dict]) -> list[dict]:
    # Normalize and clean raw data
    return raw_transactions

@task
def categorize_transactions(transactions: list[dict]) -> list[dict]:
    # Assign categories via rules or ML
    return transactions

@task
def analyze_spending(transactions: list[dict]) -> dict:
    # Identify totals, spikes, unused subs
    return {"category_totals": {}, "spikes": [], "unused_subscriptions": []}

@task
def generate_savings_suggestions(analysis: dict) -> list[dict]:
    # Create actionable suggestions
    return []

@task
def store_to_db(user_id: int, transactions: list[dict], suggestions: list[dict]):
    from sqlalchemy import create_engine
    engine = create_engine("postgresql://user:pass@localhost/dbname")
    session = Session(engine)
    # Persist transactions & suggestions
    session.commit()

@flow
def expense_optimization_pipeline(user_id: int):
    raw = fetch_transactions(user_id)
    cleaned = clean_transactions(raw)
    categorized = categorize_transactions(cleaned)
    analysis = analyze_spending(categorized)
    suggestions = generate_savings_suggestions(analysis)
    store_to_db(user_id, categorized, suggestions)

if __name__ == "__main__":
    expense_optimization_pipeline(user_id=1)
