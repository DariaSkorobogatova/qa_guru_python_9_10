import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    bd_month: str
    bd_year: str
    bd_day: str
    subject: str
    hobby: str
    avatar: str
    current_address: str
    user_state: str
    user_city: str


test_user = User(
    first_name='Ada',
    last_name='Lovelace',
    email="lovelace@rumbler.ru",
    gender="Female",
    phone_number="1112223344",
    bd_month='December',
    bd_year='2000',
    bd_day='22',
    subject="Economics",
    hobby="Reading",
    avatar="flower.png",
    current_address='Test street, 9-99',
    user_state='Uttar Pradesh',
    user_city='Lucknow',
)


