from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import requests
from utils.env import WEB_URL, BOT_TOKEN, IMAGE_ID
from utils.texts import WEB_BUTTON, CHANNEL

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



UZ = "🏆 Konkurs"
RU = "🏆 Конкурс"
EN = "🏆 Competition"

Competition = {
    "uz": UZ,
    "ru": RU,
    "en": EN,
}


def send_webapp_button(lang, user_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
   

    payload = {
        "chat_id": user_id,
        "photo":  IMAGE_ID, 
        "caption": text,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": WEB_BUTTON[lang],
                        "web_app": {
                            "url": f"{WEB_URL}"
                        }
                    },
                    {
                        "text": Competition[lang],
                        "callback_data": "competition"
                    },
                ],
                [
                    {
                        "text": CHANNEL[lang],
                        "url": "https://t.me/+uym0YuNPP4A5YmUy"
                    },
                ]
            ]
        }
    }

    response = requests.post(url, json=payload)
    
    if not response.ok:
        print("❌ Ошибка при отправке инлайн-кнопки:", response.text)


referral_uz = "🔗 Referal olish"
points_uz = "💎 Ballarim"
gifts_uz = "🎁 Sovg‘alarni ko‘rish"
back_uz = "⬅️ Orqaga"

referral_ru = "🔗 Получить реферал"
points_ru = "💎 Мои баллы"
gifts_ru = "🎁 Посмотреть подарки"
back_ru = "⬅️ Назад"

referral_en = "🔗 Get referral"
points_en = "💎 My points"
gifts_en = "🎁 View gifts"
back_en = "⬅️ Back"


top_referrals_uz = "🏆 Eng faol referlar"
top_referrals_ru = "🏆 Топ рефералы"
top_referrals_en = "🏆 Top Referrals"



def compotition_menu(lang):
    if lang == "uz":
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=referral_uz),
                    KeyboardButton(text=points_uz),
                ],
                [
                    KeyboardButton(text=gifts_uz),
                    KeyboardButton(text=top_referrals_uz),
                ],
            ],
            resize_keyboard=True
        )

    elif lang == "ru":
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=referral_ru),
                    KeyboardButton(text=points_ru),
                ],
                [
                    KeyboardButton(text=gifts_ru),
                    KeyboardButton(text=top_referrals_ru),                    
                ],
            ],
            resize_keyboard=True
        )

    else:  
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=referral_en),
                    KeyboardButton(text=points_en),
                ],
                [
                    KeyboardButton(text=gifts_en),
                    KeyboardButton(text=top_referrals_en),                   
                ],
            ],
            resize_keyboard=True
        )

    return keyboard



def ref_phone(lang):
    if lang == "uz":
        text = "📱 Telefon raqamni yuborish"
    elif lang == "ru":
        text = "📱 Отправить номер телефона"
    else:
        text = "📱 Send phone number"

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=text, request_contact=True)
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard




def referral_buttons(ref_link, lang):
    texts = {
        "uz": {
            "share": "📤 Ulashish"
        },
        "ru": {
            "share": "📤 Поделиться"
        },
        "en": {
            "share": "📤 Share"
        }
    }

    buttons = [
        [InlineKeyboardButton(text=texts[lang]["share"], switch_inline_query=ref_link)]
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)





def send_ref_button(lang, user_id, text, ref_link):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"   

    print(ref_link)
    payload = {
        "chat_id": user_id,
        "photo":  IMAGE_ID, 
        "caption": text,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": WEB_BUTTON[lang],
                        "web_app": {
                            "url": f"{ref_link}"
                        }
                    },
                ],
            ]
        }
    }

    response = requests.post(url, json=payload)
    
    if not response.ok:
        print("❌ Ошибка при отправке инлайн-кнопки:", response.text)
        
        

def create_url_button(lang, url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=WEB_BUTTON[lang], url=url)]
        ]
    )
