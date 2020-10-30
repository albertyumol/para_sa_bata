import spacy
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import telegram
from spacy import displacy
from pathlib import Path
import cairosvg

bot = telegram.Bot(token='TOKEN')

def utterance(update, context):
    msg = update.message.text
    nlp = spacy.load('en')
    doc = nlp(msg)

    svg = displacy.render(doc, style="dep", jupyter=False)
    output_path = Path("./visualizations/sentence.svg")
    output_path.open("w", encoding="utf-8").write(svg)

    cairosvg.svg2png(url='./visualizations/sentence.svg', write_to='./visualizations/image.png')
    pic = './visualizations/image.png'

    msg_id = update.message.chat
    bot.send_photo(msg_id['id'], open(pic,'rb'))


def start(update, context):
    update.message.reply_text('Hi! This is a grammar assistant. Type a sentence.')



updater = Updater('TOKEN', use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, utterance))
updater.start_polling()
updater.idle()
