import requests
from utils.env import WEB_URL, BOT_TOKEN
from utils.texts import WEB_BUTTON, CHANNEL



def send_webapp_button(lang, user_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        "chat_id": user_id,
        "photo": "AgACAgIAAxkBAANPaKCeTXgEYx3UzZS7RoUg7l4beF8AAh77MRtZPwlJyzTculhniikBAAMCAAN4AAM2BA",  # file_id
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
