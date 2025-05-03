# 🏦 Plaid FastAPI Serverless Backend

This project is a serverless FastAPI backend integrated with [Plaid](https://plaid.com) to pull live bank transactions using AWS Lambda, API Gateway, and the Serverless Framework.

## 🚀 Features

- FastAPI + Mangum (for Lambda compatibility)
- Plaid API (Sandbox by default)
- Serverless deployment to AWS Lambda
- GitHub Actions CI/CD for auto-deploy
- Secrets stored securely in GitHub Actions

---

## 🛠️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/plaid-fastapi-serverless.git
cd plaid-fastapi-serverless
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file (optional for local testing)

```env
PLAID_CLIENT_ID=your_client_id
PLAID_SECRET=your_secret
PLAID_ENV=sandbox
```

---

## ☁️ Deploy to AWS Lambda

### One-time AWS setup:
Install Serverless Framework if you haven’t:

```bash
npm install -g serverless
```

Then deploy:

```bash
sls deploy
```

Your deployed URL will appear in the output (e.g., `https://xyz123.execute-api.us-east-1.amazonaws.com/dev/...`)

---

## 🔐 GitHub Actions Deployment

### Secrets Required (Set under GitHub → Settings → Secrets → Actions)

| Key                  | Value                       |
|----------------------|-----------------------------|
| `AWS_ACCESS_KEY_ID`  | From your AWS IAM user      |
| `AWS_SECRET_ACCESS_KEY` | From AWS IAM user       |
| `PLAID_CLIENT_ID`    | From Plaid Dashboard        |
| `PLAID_SECRET`       | From Plaid Dashboard        |

### Push to Main Branch

```bash
git add .
git commit -m "Initial deploy"
git push origin main
```

GitHub Actions will deploy your FastAPI app automatically.

---

## 📂 Project Structure

```
.
├── handler.py                # FastAPI app with Mangum for AWS Lambda
├── serverless.yml            # Serverless deployment config
├── requirements.txt          # Python dependencies
└── .github/
    └── workflows/
        └── deploy.yml        # GitHub Actions workflow
```

---

## 🧪 Testing Locally (Optional)

```bash
uvicorn handler:app --reload
```

> Note: for full functionality, test with Plaid Sandbox or production setup.

---

## 🧠 Credits

Built by [Your Name] • Powered by FastAPI + Serverless + Plaid