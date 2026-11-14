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
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": text}, timeout=10)
    except:
        pass

@app.route('/')
def home():
    return "Bot is Running!"

def start():
    time.sleep(5)
    send_msg("✅ Nitin bhai, aapka bot GitHub se Render par Live ho gaya!")

threading.Thread(target=start).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
