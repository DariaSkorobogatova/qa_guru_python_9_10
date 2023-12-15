import dataclasses


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: str
    subject: str
    hobby: str
    avatar: str
    current_address: str
    city: str


user = User(
    full_name="Ada Lovelace",
    email="lovelace@rumbler.ru",
    gender="Female",
    phone_number="1112223344",
    date_of_birth="22 December,2000",
    subject="Economics",
    hobby="Reading",
    avatar="flower.png",
    current_address="Test street, 9-99",
    city="Uttar Pradesh Lucknow",
)
