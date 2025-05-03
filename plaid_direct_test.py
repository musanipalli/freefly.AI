import os
from dotenv import load_dotenv
from plaid2 import Client
from datetime import datetime, timedelta

load_dotenv()

client = Client(
    client_id=os.getenv("PLAID_CLIENT_ID"),
    secret=os.getenv("PLAID_SECRET"),
    environment=os.getenv("PLAID_ENV", "sandbox")
)

# Step 1: Create Link Token
link_token = client.link_token.create({
    "user": {"client_user_id": "demo_user"},
    "client_name": "Demo Expense App",
    "products": ["transactions"],
    "country_codes": ["US"],
    "language": "en"
})
print("Link token:", link_token["link_token"])

# Step 2: Get sandbox public token
sandbox = client.sandbox.public_token.create(
    institution_id="ins_109508",
    initial_products=["transactions"]
)
public_token = sandbox["public_token"]

# Step 3: Exchange for access token
access_token = client.item.public_token.exchange(public_token)["access_token"]
print("Access token:", access_token)

# Step 4: Fetch transactions
start = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
end = datetime.now().strftime("%Y-%m-%d")
txs = client.transactions.get(access_token=access_token, start_date=start, end_date=end)
for tx in txs["transactions"]:
    print(tx["date"], "-", tx["name"], "– $", tx["amount"])