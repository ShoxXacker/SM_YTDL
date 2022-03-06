"""
|||| @SMODILOV ||||
"""

from pyrogram import Client, Filters

@Client.on_message(Filters.command(["help"]))
async def help(client, message):
    
    # Thought of somemore features but i am lazy lul
    
    helptxt = f"""Botdan qanday foydalanish bo'yicha qadamlar!
                  .˜”*°•**Maxfiy**•°*”˜.
 Har qanday  Youtube havolasidan nusxa oling va bot ichiga joylashtiring va amallarni bajaring.
                  .˜”*°•**Guruhlarda**•°*”˜.
 Meni istalgan guruhga qo‘shing, so‘ngra istalgan yaroqli Youtube havolasidan nusxa oling va bot ichiga joylashtiring va ko‘rsatmalarga amal qiling.
                 .**Yodingizda tuting**.
 - Hozirda pleylist qo'llab-quvvatlanmaydi.
 - Kattaroq yuklab olish fayl hajmi, ko'proq kutish vaqti.
 -Va bot 1,9 Gb Bcz TeleGram cheklovlari bilan yuklashi mumkin."""
        
    
    await message.reply_text(helptxt)
