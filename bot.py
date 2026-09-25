from dotenv import load_dotenv
import os
import telebot

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


# /start
@bot.message_handler(commands=["start"])
def send_welcome(message):

    bot.reply_to(
        message,
        """Happy Anniversary, my love ❤️🥰

Here are the cute little surprises in this beautiful chatbot just for you:

💌 /message — A special message from my heart

📸 /memories — Our beautiful memories together

💭 /reply — Leave a little message for me 💕

I hope you enjoy every little part of it. 🥹❤️

I made this just for you, my love. 🌹"""
    )


# /memories
@bot.message_handler(commands=["memories"])
def memories(message):

    photos = [
        ("photo1.jpg", "How cute you areeee ❤️"),
        ("photo2.jpg", "Look at us , We were so cute! 🥺💕"),
        ("photo3.jpg", "Every moment with you is special  😭❤️"),
    ]

    for photo_path, caption in photos:

        with open(photo_path, "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption=caption
            )

    bot.send_message(
        message.chat.id,
        "And I hope we make thousands more memories together. 💕🥰"
    )


# /message
@bot.message_handler(commands=["message"])
def anniversary_message(message):

    bot.reply_to(
        message,
        """Happy two months Anniversary to us!! ❤️

I am so happy to have found you as my beloved boyfriend. 🥺❤️

I would never have known that I could become this special to you, Ratanak.

As your girlfriend, I really admire you. You are strong, smart, and kind, not just to me but to everyone around you.

Just remember that whenever hard times come, you can run to me at any time.

I will hug you and kiss you until you feel better. 🥰💕

I hope I can be the girl, and the only girl, who makes you feel the happiest.

And I hope we can spend the rest of our lives together in the future.

o sl bong klang klang❤️🌹"""
    )


# /reply
@bot.message_handler(commands=["reply"])
def ask_for_message(message):

    msg = bot.reply_to(
        message,
        """💌 Now it's your turn, my love...

Leave a little message for me ❤️

Write anything that's in your heart. 🥰"""
    )

    bot.register_next_step_handler(msg, save_message)


# Save his reply
def save_message(message):

    his_message = message.text

    bot.reply_to(
        message,
        """Awww 🥹❤️ I got your message!

I'll keep it as one of our special memories. 💕"""
    )

    print("His message:", his_message)


# Start bot
bot.infinity_polling()