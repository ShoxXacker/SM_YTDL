"""
|||| @SMODILOV ||||
"""

from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["github"]), group=-2)
async def love(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("♂️ Github", url="https://github.com/PredatorHackerzZ")],
    ])
    Aww = f"""Salom <b>{message.from_user.first_name}</b>
Agar sizga mening loyiham yoqqan bo'lsa va GitHub ishtirokchisi bo'lishni istasangiz:
- 🗣️ MENI DASTURCHIM **@SMODILOV**
- 🧾 Menga Telegram orqali shaxsiy xabar yuborishingiz mumkin **@SMODILOV**   
- BOT FAQAT YOUTUBE VIDEO YUKLAYDI.\n
Agar siz mening loyihamni yoqtirgan bo'lsangiz va Danat qilishni xohlasangiz va , shu raqamga tashlashingiz mumkin:
- [TELEGRAM](https://t.me/SMODILOV) 
    
**<b>{message.from_user.first_name}</b> 😁 Botdan foydalanganingiz uchun rahmat**
[@YoutubeXDBot](https://telegra.ph/file/a532f298b920e99bd58bb.jpg)
"""      
    await message.reply_text(Aww, reply_markup=joinButton)
    raise StopPropagation
