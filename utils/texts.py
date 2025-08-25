# texts.py fayli
uz = \
"""
<b>
🎓 Pedagog.uz — o‘qituvchilar uchun resurslar platformasi!
Bu yerda siz dars ishlanmalar, metodik tavsiyalar, testlar, qo‘llanmalar va yana ko‘plab kerakli materiallarni topishingiz mumkin.
✔️ Fanlar bo‘yicha cheklanmagan resurslar
✔️ Zamonaviy o‘qituvchilarga mos yondashuv
✔️ Darslarni samarali tashkil qilish uchun qulay imkoniyatlar
Bizda yuzlab ijobiy fikrlar mavjud, lekin siz buni allaqachon eshitgansiz 😉
👇 Boshlash uchun tugmani bosing, shuningdek, kanalda obuna bo‘ling — eng yangi metodik materiallar va aksiyalar birinchi bo‘lib u yerda chiqadi!
</b>
"""

ru = \
"""
<b>
🎓 Pedagog.uz — платформа ресурсов для учителей!
Здесь вы найдёте конспекты уроков, методические рекомендации, тесты, пособия и множество других полезных материалов.
✔️ Неограниченные ресурсы по всем предметам
✔️ Современный подход для преподавателей
✔️ Удобные возможности для эффективной организации уроков
У нас сотни положительных отзывов, но вы, наверное, уже слышали об этом 😉
👇 Нажмите, чтобы начать, а также подпишитесь на канал — самые новые методические материалы и акции появляются там первыми!
</b>
"""

en = \
"""
<b>
🎓 Pedagog.uz — the resource platform for teachers!
Here you can find lesson plans, methodological guides, tests, handbooks, and many other useful materials.
✔️ Unlimited resources for all subjects
✔️ A modern approach for today’s teachers
✔️ Convenient tools to organize lessons effectively
We have hundreds of positive reviews, but you’ve probably already heard about that 😉
👇 Click to start, and don’t forget to subscribe to our channel — the hottest updates and materials always appear there first!
</b>
"""

START = {
    "uz": uz,
    "ru": ru,
    "en": en
}


HELP = \
"""
Pedagog.uz
"""


WEB_BUTTON = {
    "uz": "📚 Platformaga o‘tish",
    "ru": "📚 Перейти на платформу",
    "en": "📚 Go to the platform",
}

CHANNEL = {
    "uz": "🔔 Kanalga obuna bo‘lish",
    "ru": "🔔 Подписаться на канал",
    "en": "🔔 Subscribe to the channel",
}



COMPETITION = {
    "uz": "🏆 Siz <b>Konkurs</b> bo'limiga kirdingiz! 🎉 Omad tilaymiz!",
    "ru": "🏆 Вы вошли в раздел *Конкурс*! 🎉 Желаем удачи!",
    "en": "🏆 You have entered the *Competition* section! 🎉 Good luck!"
}


ref_phone_uz = "📱 Iltimos, pedagog.uz platformasida ro‘yxatdan o‘tgan telefon raqamingizni yuboring. \n\n📌 Format: +998 ** ** *** ** **"
ref_phone_ru = "📱 Пожалуйста, отправьте номер телефона, зарегистрированный на платформе pedagog.uz. \n\n📌 Формат: +998 ** ** *** ** **"
ref_phone_en = "📱 Please send the phone number registered on the pedagog.uz platform. \n\n📌 Format: +998 ** ** *** ** **"

REF_PHONE = {
    "uz": ref_phone_uz,
    "ru": ref_phone_ru,
    "en": ref_phone_en,
}




REF_PHONE_ACCEPTED = {
    "uz": "✅ Telefon raqamingiz qabul qilindi: {phone}",
    "ru": "✅ Ваш номер телефона принят: {phone}",
    "en": "✅ Your phone number has been accepted: {phone}",
}

REF_PHONE_INVALID = {
    "uz": "❌ Telefon raqami noto‘g‘ri. Faqat raqam yuboring va uzunligi kamida 9 ta bo‘lishi kerak.",
    "ru": "❌ Неверный номер. Отправьте только цифры, не менее 9 символов.",
    "en": "❌ Invalid number. Send only digits with at least 9 characters.",
}

REF_PHONE_ERROR = {
    "uz": "❌ Telefon raqamini yuborishda xatolik yuz berdi.",
    "ru": "❌ Произошла ошибка при отправке номера телефона.",
    "en": "❌ An error occurred while sending the phone number.",
}

REF_PHONE_NOT_FOUND = {
    "uz": "❌ Bu telefon raqam topilmadi.\n\nIltimos, avval [pedagog.uz](https://pedagog.uz) saytida ro‘yxatdan o‘ting.",
    "ru": "❌ Этот номер не найден.\n\nПожалуйста, сначала зарегистрируйтесь на [pedagog.uz](https://pedagog.uz).",
    "en": "❌ This phone number was not found.\n\nPlease register first at [pedagog.uz](https://pedagog.uz)."
}


REF_LINK = {
    "uz": "Quyidagi havolani do‘stlaringiz bilan ulashing va bonusga ega bo‘ling!\n\n<code>{}</code>",
    "ru": "Поделитесь этой ссылкой с друзьями и получите бонус!\n\n<code>{}</code>",
    "en": "Share this link with your friends and earn a bonus!\n\n<code>{}</code>",
}
