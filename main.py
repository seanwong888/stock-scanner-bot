import requests
import time
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
API_KEY = os.environ.get("API_KEY")

def send_message(text):
    if not BOT_TOKEN or not CHAT_ID:
        print("Missing BOT_TOKEN or CHAT_ID")
        return
        
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

def scan_market():
    if not API_KEY:
        print("Missing API_KEY")
        return

    url = f"https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=r8LJk0xqF9hWssoD1kXPWZOPUe2Z7gLe"
    
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print("API error:", e)
        return

    if not isinstance(data, list):
        print("Unexpected API response:", data)
        return

    for stock in data:
        try:
            change = float(stock['changesPercentage'].replace('%','').replace('+',''))
            volume = int(stock['volume'])
        except:
            continue

        if change >= 0 and volume > 5000:
            msg = f"🚀 {stock['symbol']} 上升 {change}%\n成交量: {volume}"
            send_message(msg)

while True:
    scan_market()
    time.sleep(30)
