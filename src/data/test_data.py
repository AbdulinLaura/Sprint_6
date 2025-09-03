from datetime import date, timedelta


def d(days):
    return (date.today() + timedelta(days=days)).strftime("%d.%m.%Y")


ORDER_DATA = [
    # Набор 1 — “простые” кириллические ФИО, адрес без квартиры, завтра, СУТКИ, верхняя кнопка
    {
        "name": "Иван",
        "surname": "Иванов",
        "address": "Москва, Тверская 1",
        "metro": "Тверская",
        "phone": "+79990000001",
        "date": d(1),
        "rent": "сутки",
        "entry": "top",
    },
    # Набор 2 — фамилия с «ё», адрес с квартирой, послезавтра, ДВОЕ СУТОК, нижняя кнопка
    {
        "name": "Мария",
        "surname": "Семёнова",
        "address": "Москва, Арбат 10, кв. 5",
        "metro": "Арбатская",
        "phone": "+79990000002",
        "date": d(2),
        "rent": "двое суток",
        "entry": "bottom",
    },
]
