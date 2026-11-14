import os
from flask import Flask
import requests, threading, time
app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_msg(t):
    if not BOT_TOKEN or not CHAT_ID: return
    try:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": t}, timeout=10)
        print("Message sent!")
    except Exception as e:
        print(f"Error {e}")

@app.route('/')
def home(): return "Bot is Running!"

def start():
    time.sleep(5)
    print("Bot Starting...")
    send_msg("✅ Nitin bhai, bot Live ho gaya! 12:05 AM")

threading.Thread(target=start).start()
