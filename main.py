import os
import time
import requests
from telegram import Bot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
TWELVE_API_KEY = os.environ.get("TWELVE_API_KEY")

bot = Bot(token=BOT_TOKEN)

chat_id = "6459645702"
symbol = "AAPL"

def get_stock_data():
    url = f"https://api.twelvedata.com/quote?symbol={symbol}&apikey={TWELVE_API_KEY}"
    response = requests.get(url)
    data = response.json()

if "percent_change" not in data:
    print("API error:", data)
    return None, None

price = float(data["close"])
change = float(data["percent_change"])
volume = float(data["volume"])

return change, volume


while True:
    change, volume = get_stock_data()

    if change is None:
        time.sleep(60)
        continue

    print("Change:", change, "Volume:", volume)

    if True:
    try:
        bot.send_message(
            chat_id=chat_id,
            text=f"{symbol} 變動 {change}% 成交量 {volume}"
        )
        print("✅ Message sent")
    except Exception as e:
        print("❌ Send error:", e)

    time.sleep(30)
