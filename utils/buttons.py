import requests
from utils.env import WEB_URL, BOT_TOKEN


def send_webapp_button(user_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": user_id,
        "text": text,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "Pedagog.uz",
                        "web_app": {
                            "url": f"{WEB_URL}"
                        }
                    },
                ]
            ]
        }
    }
    response = requests.post(url, json=payload)
    
    if not response.ok:
        print("❌ Ошибка при отправке инлайн-кнопки:", response.text)

