from config import *

@bot.message_handler(commands=['start', 'help'])
def greet(msg):
    bot.reply_to(msg, "hello " + str(msg.from_user.username))

@bot.message_handler(commands=['contentmessage'])
def start(msg):
    if msg.from_user.id != ADMIN:

        bot.reply_to(msg, "Not uncle B!!!!")


    else:

        bot.reply_to(msg, "Yes Boss!")



@server.route('/' + TOKEN, methods=['POST', 'GET'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Your bot application is still active!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=SERVER_URL + '/' + TOKEN )
    return "Application running!", 200


if __name__ == "__main__":
    if DEBUG != True:
        server.run(host="0.0.0.0", threaded=True, port=int(os.environ.get('PORT', 5000)))

    else:
        bot.remove_webhook()
        print("bot polling...")
        bot.polling()
        while True:
            pass
    
        