from telebot import TeleBot, types
import translate

bot = TeleBot("7795549873:AAEtMz9pAwZ014758eNJ9X5shquKWGDgwCQ")
@bot.message_handler(["start"])
def start(message: types.Message):
    bot.send_message(message.from_user.id, "Assalomu alaykum, ushbu bot matnlarni tarjima qilishda yordam beradi")

@bot.message_handler()
def tarjimon(message: types.Message):
    bot.send_message(message.from_user.id, translate.tarjimon(message.text))

bot.polling()