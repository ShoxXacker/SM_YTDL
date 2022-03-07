"""
|||| @SMODILOV ||||
"""

from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🍃 KANAL", url="https://t.me/Hacker_Bey"),
         InlineKeyboardButton("🛡 Support", url="https://t.me/SMODILOV")],
        [InlineKeyboardButton("🎗️ Deploy", url="https://github.com/ShoxXacker/SM_YTDL"),
         InlineKeyboardButton("🤖 MENING 2 - BOTIM", url="https://t.me/Advokat_Sbot")],
    ])
    welcomed = f"""
    Assalamu Aleykum 🙋,
Xurmatli janob<b>{message.from_user.first_name}</b>
Bu YouTube havola yuklovchi boti. Yordam uchun /help Bot haqida qo'shimcha ma'lumot olish uchun.
    [📥](https://telegra.ph/file/39812237fd7a1bfc02532.jpg)"""
  
    
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
