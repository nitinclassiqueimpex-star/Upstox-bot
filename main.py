import os
from flask import Flask
import requests
import threading
import time

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_msg(text):
    if not BOT_TOKEN or not CHAT_ID:
        print("TOKEN/CHAT_ID missing")
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        r = requests.post(url, json={"chat_id": CHAT_ID, "text": text})
        print(f"Telegram Response: {r.text}")
    except Exception as e:
        print(f"Error: {e}")

@app.route('/')
def home():
    return "Bot is Running!"

def start():
    time.sleep(5)
    print("Bot Starting...")
    send_msg("✅ Nitin bhai, aapka bot Live ho gaya!")

threading.Thread(target=start).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
