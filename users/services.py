import stripe
from forex_python.converter import CurrencyRates

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product():
    """Создает продукт в страйпе"""

    return stripe.Product.create(name="Education Course")


def convert_rub_to_usd(amount):
    """Конвертирует рубли в доллары"""

    c = CurrencyRates()
    rate = c.get_rate("RUB", "USD")
    return int(float(amount) * rate)


def create_stripe_price(amount, product):
    """Создаёт цену в страйпе"""

    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": product.get("name")},
    )


def create_stripe_session(price):
    """Создаёт сессию на оплату в страйпе"""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/users/payment/success/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
