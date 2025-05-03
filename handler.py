from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from plaid2 import Client
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from mangum import Mangum

load_dotenv()

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

client = Client(
    client_id=os.getenv("PLAID_CLIENT_ID"),
    secret=os.getenv("PLAID_SECRET"),
    environment=os.getenv("PLAID_ENV", "sandbox")
)

@app.get("/create_link_token")
def create_link_token():
    return {
        "link_token": client.link_token.create({
            "user": {"client_user_id": "lambda_user"},
            "client_name": "Plaid Lambda App",
            "products": ["transactions"],
            "country_codes": ["US"],
            "language": "en"
        })["link_token"]
    }

@app.post("/exchange_token")
async def exchange_token(request: Request):
    data = await request.json()
    token = data.get("public_token")
    return {"access_token": client.item.public_token.exchange(token)["access_token"]}

@app.get("/transactions")
def transactions(access_token: str):
    start = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    end = datetime.now().strftime("%Y-%m-%d")
    txs = client.transactions.get(access_token=access_token, start_date=start, end_date=end)
    return {"transactions": txs["transactions"]}

handler = Mangum(app)