import telegram # this is from python-telegram-bot package

from django.conf import settings
from django.template.loader import render_to_string
from .models import Cart

def cook_data(cart):
    data = {}
    data["order_name"] = f"Заказ#{cart.id}"
    data["sum"] = cart.summ
    data["count"] = cart.count
    data["owner"] = cart.owner
    data["number"] = cart.number
    data["products"] = [f"Название:{i.product.name}, Цена{i.product.price}" for i in cart.cart_products.all()]
    data["url"] = cart.get_admin_url()
    return data

    # data = {}
    # data["order_name"] = "Заказ#4"
    # data["sum"] = 140
    # data["count"] = 3
    # data["owner"] = "erbol"
    # data["number"] = "+996702243534"
    # data["products"] = [ "Имя:jdofijdsf, Цена :140","name:jdosf, price :150" ]
    # data["url"] = "www.google.com"
    # return data

def post_event_on_telegram(cart):
    data = cook_data(cart)
    message_html = render_to_string('telegram.html', data)
    bot = telegram.Bot(token=settings.BOT_TOKEN)
    bot.send_message(chat_id=settings.GROUP_ID,
        text=message_html, parse_mode=telegram.ParseMode.HTML)