from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import requests
from bs4 import BeautifulSoup

url = "https://stooq.com/q/?s=usdkrw&c=1d&t=l&a=lg&b=0"
req = requests.get(url)
req.raise_for_status()

soup = BeautifulSoup(req.text, "html.parser")
dollar = soup.find("span", id="aq_usdkrw_c2").get_text()

accessToken = "6651535891:AAH8gDDZUjAMGVyw5ivhW58WW8FztZBsrbw"  # replace with your actual bot token.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    reply = "환율을 보려면 '달러'를 입력해주세요."
    update.message.reply_text(reply)

def echo(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()
    reply = "현재 환율을 보려면 '달러'를 입력해주세요."
    
    if '달러' in text:
        reply = f"달러 환율: {dollar}"

    update.message.reply_text(reply)


updater = Updater(accessToken)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & ~Filters.command, echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()

