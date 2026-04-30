import requests
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
TWELVE_API_KEY = os.getenv("TWELVE_API_KEY")

SYMBOL = "AAPL"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": 6459645702,
        "text": message
    }
    try:
        response = requests.post(url, data=payload)
        print("Telegram response:", response.text)
    except Exception as e:
        print("Telegram send error:", e)

while True:
    try:
        url = f"https://api.twelvedata.com/quote?symbol={SYMBOL}&apikey={TWELVE_API_KEY}"
        response = requests.get(url)
        data = response.json()

        print("Raw API data:", data)

        # 如果 API 回傳 list
        if isinstance(data, list):
            data = data[0]

        # 檢查是否有 percent_change
        if "percent_change" not in data:
            print("API error:", data)
            time.sleep(30)
            continue

        change = float(data["percent_change"])
        volume = float(data["volume"])

        print("Change:", change)
        print("Volume:", volume)

        message = f"{SYMBOL}\nChange: {change}%\nVolume: {volume}"

        send_telegram_message(message)

    except Exception as e:
        print("Main loop error:", e)

    time.sleep(30)
    
