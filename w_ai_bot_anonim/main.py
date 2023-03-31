import json
import os
import random
import time
from datetime import datetime

import amanobot.namedtuple
import pytz
import requests
from amanobot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from amanobot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

from config import TOKEN

token = TOKEN
# "6268136991:AAHRudSAmV1EoYCRR2I2a39l4PMOuPdmqlQ"
bot = amanobot.Bot(token)

queue = {
    "free": [],
    "occupied": {}
}
users = []
user3 = []
ADMIN = ['sardor']


def saveConfig(data):
    return open('config.json', 'w').write(json.dumps(data))


if __name__ == '__main__':
    s = time.time()
    print('[#] Sun`iy\n[i] Sardor Egamberdiyev tomonidan yaratilgan\n')
    print('[#] konfiguratsiyani tekshiring...')
    if not os.path.isfile('config.json'):
        print('[#] konfiguratsiyani tekshiring...')
        open('config.json', 'w').write('{}')
        print('[#] Bajarildi')
    else:
        print('[#] Konfiguratsiya topildi!')
    print('[i] Bot onlaynda ' + str(time.time() - s) + 's')


def exList(list, par):
    a = list
    a.remove(par)
    return a


def handle(update):
    global queue
    try:
        config = json.loads(open('config.json', 'r').read())
        if 'text' in update:
            text = update["text"]
        else:
            text = ""
        uid = update["chat"]["id"]

        if uid not in user3:
            users.append(uid)

        if not uid in config and text != "/nopics":
            config[str(uid)] = {"pics": True}
            saveConfig(config)

        if uid in queue["occupied"]:
            if 'text' in update:
                if text != "/next" and text != "❌ Chiqish" and text != "Keyingisi ▶" and text != "/exit":
                    bot.sendMessage(queue["occupied"][uid], "" + text)

            if 'photo' in update:
                captionphoto = update["caption"] if "caption" in update else None
                photo = update['photo'][0]['file_id']
                bot.sendPhoto(queue["occupied"][uid],
                              photo, caption=captionphoto)

            if 'video' in update:
                captionvideo = update["caption"] if "caption" in update else None
                video = update['video']['file_id']
                bot.sendVideo(queue["occupied"][uid],
                              video, caption=captionvideo)

            if 'document' in update:
                captionducument = update["caption"] if "caption" in update else None
                document = update['document']['file_id']
                bot.sendDocument(queue["occupied"][uid],
                                 document, caption=captionducument)

            if 'audio' in update:
                captionaudio = update["caption"] if "caption" in update else None
                audio = update['audio']['file_id']
                bot.sendAudio(queue["occupied"][uid],
                              audio, caption=captionaudio)

            if 'video_note' in update:
                video_note = update['video_note']['file_id']
                bot.sendVideoNote(queue["occupied"][uid], video_note)

            if 'voice' in update:
                captionvoice = update["caption"] if "caption" in update else None
                voice = update['voice']['file_id']
                bot.sendVoice(queue["occupied"][uid],
                              voice, caption=captionvoice)

            if 'sticker' in update:
                sticker = update['sticker']['file_id']
                bot.sendSticker(queue["occupied"][uid], sticker)

            if 'contact' in update:
                nama = update["contact"]["first_name"]
                #	nama = update["contact"]["last_name"]
                contact = update['contact']['phone_number']
                bot.sendContact(queue["occupied"][uid],
                                contact, first_name=nama, last_name=None)

            if 'dice' in update:
                dice = update["dice"]["emoji"]
                keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
                    text="Telegram", url="https://t.me/egamberdiyevsardor")]])
                bot.sendDice(queue["occupied"][uid],
                             emoji=dice, reply_markup=keyboard)

        if text == "/start" or text == "/refresh":
            if not uid in queue["occupied"]:
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/welkin_group/"),
                     InlineKeyboardButton(text="Telegram", url="https://t.me/Welkin_GR"),
                     InlineKeyboardButton(text="Telegram", url="https://t.me/egamberdiyevsardor"),
                     InlineKeyboardButton(text="Telegram", url="https://t.me/kama_alone")]])
                # InlineKeyboardButton(text="ɢʀᴜᴘ ʙᴏᴛ", url="t.me/Welkin_GR"),
                # InlineKeyboardButton(text="ʙᴏᴛ ɴᴜʟɪꜱ", url="t.me/Welkin_GR")]])
                bot.sendMessage(uid,
                                "𝗪 - 𝗔𝗡𝗢𝗡𝗬𝗨𝗠𝗢𝗨𝗦 𝗖𝗛𝗔𝗧 💬\n\nSiz o'z suhbatdoshingizni toping va "
                                "dunyoqarashingizni kengaytiring Istalgan tilda muloqot qilishingiz mumkin.\n\n🤖: "
                                "Chatda do'stlarini topish uchun quydagi buyruqdan foydalaning  /search 👈🏻\n\nObuna "
                                "bo'lishni unutmang ❗️",
                                parse_mode='MarkDown', disable_web_page_preview=True, reply_markup=keyboard)

        if 'message_id' in update:
            if not uid in queue["occupied"]:
                if text != "/start" and text != "Foydalanuvchi👤" and text != "Keyingisi ▶" and text != "/refresh" and text != "/help" and text != "/search" and text != "Qidirish 🔍" and text != "🔙 Asosiy menyu" and text != "RandomPhoto📷" and text != "Ma`lumot profili 📌" and text != "/mabar" and text != "Ajablanadigan havolalar" and text != "Youtube▶️" and text != "/user":
                    news = ReplyKeyboardRemove()
                    # news = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="ɢʀᴏᴜᴘ ᴄʜᴀᴛ",
                    # url="t.me/caritemanh"), InlineKeyboardButton(text="𝔽𝕆𝕃𝕃𝕆𝕎 𝕄𝔼",
                    # url="https://instagram.com/rianfirnandaa_")]])
                    bot.sendMessage(uid,
                                    "[❗️] Kechirasiz, siz chatda emassiz\nchatga kirish uchun /refresh yoki "
                                    "/search bosishingiz kerak bosgan bo`lsangiz👇🏻",
                                    parse_mode="MarkDown", reply_markup=news, reply_to_message_id=update['message_id'])
                    # pesan = bot.sendMessage(uid, "Wait...", reply_markup=keyboarddihapus)
                    # time.sleep(4)
                    # hapus = pesan['message_id']
                    # bot.deleteMessage((uid,hapus))
        # if 'text' in update and update['text'] == '/pis':
        #	with open('id.txt', 'r') as file:
        #		user_ids = file.read()
        #		if str(uid) not in user_ids:
        #			with open('id.txt', 'w') as f:
        #				f.write(user_ids+"\n"+str(uid))
        #			bot.sendMessage(uid,"Id saved")
        #		else:
        #			bot.sendMessage(uid, "kmu sudah ada di bot")
        # with open('./id.txt', 'r') as idfile:
        #	chat_id=int(idfile.read())
        #	bot.sendMessage(chat_id, "Someone is in your house!")

        # if text == "/bs":
        #	text = " ".join(update["text"].split()[1:])
        #	# = json.loads(open("id.txt", "r").read())
        #	try:
        #		for uid in users:
        #			bot.sendMessage(int(uid), text)
        #	except:
        #		raise
        # if update["text"].split()[0] == "/bc":
        #	text = update["text"].split()
        #	if len(text) == 0:
        #		return bot.sendMessage(uid, "masukkan text")
        #	try:
        #		for uid in user3:
        #			bot.sendMessage(uid, " ".join(text[1:]))
        #	except:
        #		pass

        if text == "/mabar":
            if not uid in queue["occupied"]:
                if str(uid) in ADMIN:
                    pesan = "Oʻyin rejimi yoqilgan"
                    keyboard = ReplyKeyboardMarkup(keyboard=[['ML', 'PUBG', 'FF'], [
                        '🔙 Asosiy menyu']], resize_keyboard=True, one_time_keyboard=True)
                    bot.sendMessage(uid, pesan, reply_markup=keyboard,
                                    reply_to_message_id=update['message_id'])
                else:
                    bot.sendDice(uid, emoji="🎳")
                    bot.sendMessage(
                        uid, "⚡️ Bu buyruq faqat administrator uchun ⚡️")

        # if text == "/test": if not uid in queue["occupied"]: lolt = ReplyKeyboardMarkup(keyboard=[ ['Oddiy matn',
        # KeyboardButton(text='Faqat matn')], [dict(text='phone', request_contact=True), KeyboardButton(
        # text='Location', request_location=True)]], resize_keyboard=True) bot.sendMessage(uid, "contoh",
        # reply_markup=lolt)

        elif text == "Foydalanuvchi👤":
            file = json.loads(open("app.json", "r").read())
            text = "Hozirgi onlayn foydalanuvchilar: " + str(len(file)) + " Foydalanuvchi👤"
            bot.sendMessage(uid, text)

        elif text == "/user":
            # if str(uid) in ADMIN :
            file = open("is.txt", "r")
            text = "Kanal obunachilar: " + str(len(file.readlines())) + " Foydalanuvchi👤"
            bot.sendMessage(uid, text)
            # else:
            # bot.sendMessage(uid, "⚡️ Perintah ini hanya untuk admin ⚡️")
        elif text == 'Ma`lumot profili 📌':
            # if str(uid) in ADMIN :
            # if "last_name" not in update["from"]:
            # return bot.sendMessage(uid, "Harap Isi Nama Belakang Kamu!!")
            # if not update["from"]["last_name"] == None else update["from"]["last_name"]:
            # lastname = update["from"]["last_name"] if "last_name" in update else None
            name = update["from"]["first_name"]
            _id = update["from"]["id"]
            # username = update["from"]["username"] if "username" not in update None
            username = update["from"]["username"]
            tipe = update["chat"]["type"]
            date1 = datetime.fromtimestamp(update["date"], tz=pytz.timezone(
                "asia/jakarta")).strftime("%d/%m/%Y %H:%M:%S").split()
            text = "*Yo'q : " + str(name) + "*" + "\n"
            text += "*Sizning ID :* " + "`" + str(_id) + "`" + "\n"
            text += f"*Foydalanuvchi nomi :* @{username}" + "\n"
            text += "*Chat turi* : " + "_" + str(tipe) + "_" + "\n"
            text += "*Sana :* " + str(date1[0]) + "\n"
            text += "*Vaqt :* " + str(date1[1]) + " WIB" "\n"
            bot.sendMessage(uid, text, parse_mode='MarkDown',
                            reply_to_message_id=update['message_id'])
            # else:
            # forw = update["forward_from"]['language_code']
            # bahasa = update["from"]["language_code"]
            # name = update["from"]["first_name"]
            # _id = update["from"]["id"]
            # bot.sendMessage(uid, f"Nama = {name}\nID = `{_id}`\nBahasa = {bahasa}", parse_mode="MarkDown")

        elif text == 'Qidirish 🔍' or text == "/search":
            if not uid in queue["occupied"]:
                keyboard = ReplyKeyboardRemove()
                bot.sendMessage(uid, 'Sziga sherik qidirilmoqda... bir daqiqa kutib turing😊',
                                parse_mode='MarkDown', reply_markup=keyboard)
                print("[SB] " + str(uid) + " Chatga qo'shiling")
                queue["free"].append(uid)

        elif text == '❌ Chiqish' or text == '/exit' and uid in queue["occupied"]:
            print('[SB] ' + str(uid) + ' O`z do`stingizni belgilab qoldiring ' +
                  str(queue["occupied"][uid]))
            keyboard = ReplyKeyboardMarkup(keyboard=[['Qidirish 🔍'], [
                'Foydalanuvchi👤', '🔙 Asosiy menyu']], resize_keyboard=True, one_time_keyboard=True)
            bot.sendMessage(uid, "🔸 Chat tugadi",
                            parse_mode='MarkDown', reply_markup=keyboard)
            bot.sendMessage(queue["occupied"][uid], "🔹 Sizning sherigingiz chatni tark etadi",
                            parse_mode='MarkDown', reply_markup=keyboard)
            del queue["occupied"][queue["occupied"][uid]]
            del queue["occupied"][uid]

        elif text == '🔙 Asosiy menyu':
            keyboard = ReplyKeyboardMarkup(keyboard=[['Qidirish 🔍'], ['Foydalanuvchi👤']], resize_keyboard=True,
                                           one_time_keyboard=True)
            bot.sendMessage(uid, "🔄 Takrorlash", parse_mode='MarkDown',
                            disable_web_page_preview=True, reply_markup=keyboard)

        # elif text == 'RandomPhoto📷':
        #     picls = glob("img/*.jpg")
        #     love = random.choice(picls)
        #     with open(love, 'rb') as photo:
        #         bot.sendPhoto(uid, photo)

        elif text == "Keyingisi ▶" or text == "/next" and uid in queue["occupied"]:
            print('[SB] ' + str(uid) + ' bilan suhbat qoldiring ' +
                  str(queue["occupied"][uid]))
            keyboard = ReplyKeyboardMarkup(
                keyboard=[['Qidirish 🔍', '🔙 Asosiy menyu']], resize_keyboard=True, one_time_keyboard=True)
            bot.sendMessage(uid, "🛑 Suhbat tugadi!",
                            parse_mode="MarkDown")
            bot.sendMessage(queue["occupied"][uid], "🛑 Suhbat tugadi!",
                            parse_mode="MarkDown", reply_markup=keyboard)
            del queue["occupied"][queue["occupied"][uid]]
            del queue["occupied"][uid]
            if not uid in queue["occupied"]:
                key = ReplyKeyboardRemove()
                bot.sendMessage(uid, 'Yangi Suhbatdosh qidiryapsizmi... bir daqiqa kutib turing 😊',
                                parse_mode="MarkDown", reply_markup=key)
                print("[SB] " + str(uid) + "Chatga qo'shiling")
                queue["free"].append(uid)

        if text == "/nopics":
            config[str(uid)]["pics"] = not config[str(uid)]["pics"]
            if config[str(uid)]["pics"]:
                bot.sendMessage(uid, "Juftlik suratlarini yuborish")
            else:
                bot.sendMessage(uid, "Turmush o'rtog'i fotosuratlarni yubora olmaydi")
            saveConfig(config)

        if len(queue["free"]) > 1 and not uid in queue["occupied"]:
            partner = random.choice(exList(queue["free"], uid))
            if partner != uid:
                keyboard = ReplyKeyboardMarkup(keyboard=[
                    ["🎲", "🎯", "🎳", "🏀", "⚽", "🎰"], ['Keyingisi ▶', '❌ Chiqish'], [
                        dict(text='Raqamni ulashish', request_contact=True)]
                ], resize_keyboard=True, one_time_keyboard=True)
                print('[SB] ' + str(uid) + ' bilan mos ' + str(partner))
                queue["free"].remove(partner)
                queue["occupied"][uid] = partner
                queue["occupied"][partner] = uid
                bot.sendMessage(uid, '🎈Sizning sherigingiz topildi, suhbat boshlashingiz mumkin 😀',
                                parse_mode='MarkDown', reply_markup=keyboard)
                bot.sendMessage(partner, '🎈Sizning sherigingiz topildi, suhbat boshlashingiz mumkin 😀',
                                parse_mode='MarkDown', reply_markup=keyboard)
    except Exception as e:
        print('[!] Error: ' + str(e))


if __name__ == '__main__':
    bot.message_loop(handle)
    while 1:
        time.sleep(3)
