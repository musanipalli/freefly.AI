import streamlit as st
import requests
import streamlit.components.v1 as components

API_BASE = "http://localhost:8000"

st.title("💳 Connect Your Bank")

res = requests.get(f"{API_BASE}/create_link_token")
link_token = res.json().get("link_token")

components.html(f'''
  <script src="https://cdn.plaid.com/link/v2/stable/link-initialize.js"></script>
  <button onclick="launch()">Link Bank</button>
  <script>
    function launch() {{
      const handler = Plaid.create({{
        token: '{link_token}',
        onSuccess: function(public_token) {{
          fetch('{API_BASE}/exchange_token', {{
            method: 'POST',
            headers: {{ 'Content-Type': 'application/json' }},
            body: JSON.stringify({{ public_token }})
          }})
          .then(res => res.json())
          .then(data => {{
            window.location.href = '?access_token=' + data.access_token;
          }});
        }}
      }});
      handler.open();
    }}
  </script>
''', height=200)

access_token = st.query_params.get("access_token")
if access_token:
    st.success("✅ Connected!")
    tx = requests.get(f"{API_BASE}/transactions", params={"access_token": access_token})
    st.json(tx.json())