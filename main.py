import requests
import time
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

def scan_market():
    url = "https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=demo"
    response = requests.get(url)
    data = response.json()

    for stock in data:
        change = float(stock['changesPercentage'].replace('%',''))
        volume = int(stock['volume'])

        if change >= 3 and volume > 500000:
            msg = f"🚀 {stock['symbol']} 上升 {change}%\n成交量: {volume}"
            send_message(msg)

while True:
    scan_market()
    time.sleep(300)
  
