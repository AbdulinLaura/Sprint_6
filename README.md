# Sprint_6
Описание

Проект содержит набор UI-автотестов на Python + PyTest + Selenium с применением Page Object Model и генерацией Allure-отчёта.
Тестируется учебное веб-приложение https://qa-scooter.praktikum-services.ru.

Покрытые сценарии:

FAQ/Аккордеон — при клике по каждому вопросу открывается соответствующий текст (8 тестов через параметризацию).

Позитивный заказ самоката — полный флоу с двумя наборами валидных данных, прогоняемым для двух точек входа (верхняя/нижняя кнопки «Заказать»).

Навигация по логотипам — клик по логотипу Самоката ведёт на главную; клик по логотипу Яндекса открывает новую вкладку с Dzen (через редирект).

Проект рассчитан на «джун-уровень»: минимум абстракций, понятные локаторы и «умные» клики (скролл + JS-фолбэк) для стабильности.

Стек технологий

Python 3.9+

Selenium WebDriver 4

PyTest 8

Allure PyTest

Firefox + Geckodriver

PyCharm (IDE)

Структура проекта
Sprint_6/
├─ src/
│  ├─ pages/                 
│  │  ├─ base_page.py         
│  │  ├─ main_page.py         
│  │  └─ order_page.py        
│  └─ data/
│     ├─ test_data.py         
│     └─ faq_expected.py     
├─ tests/
│  ├─ conftest.py            
│  ├─ test_faq_accordion.py   
│  ├─ test_order_flow.py     
│  └─ test_logos_navigation.py
├─ requirements.txt
└─ README.md

Установка
# 1) Виртуальное окружение (рекомендуется)
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -U pip

# 2) Firefox + Geckodriver (должен быть в PATH)
# macOS:  brew install --cask firefox && brew install geckodriver
# Linux/Win: установите вручную и добавьте geckodriver в PATH

# 3) Зависимости проекта
pip install -r requirements.txt


В PyCharm пометьте папку src как Sources Root (ПКМ по src → Mark Directory as → Sources Root).
Запуск из корня проекта (Working directory = корень).

Запуск тестов
# все тесты
pytest -v -s

# только FAQ
pytest -v -s tests/test_faq_accordion.py

# только заказ
pytest -v -s tests/test_order_flow.py

# один тест
pytest -v -s tests/test_order_flow.py::test_positive_order_for_each_entry

Allure-отчёт
# собрать результаты
pytest -v -s --alluredir=allure-results
# открыть интерактивный отчёт локально
allure serve allure-results


(потребуется установленный Allure CLI)

Детали реализации

Page Object: для каждой страницы — свой класс.
Общая логика кликов/ожиданий — в BasePage.

Умный клик: BasePage.click() скроллит элемент в центр, делает небольшой оффсет (от залипающей шапки) и при необходимости кликает через JS — меньше флапов.

Параметризация:

FAQ: range(8) + ожидаемые тексты из faq_expected.py.

Заказ: ORDER_DATA × ["top","bottom"] — каждый набор данных прогоняется для обеих кнопок.

Защита шагов формы: OrderPage.ensure_step1() гарантирует, что перед заполнением полей мы на шаге 1 (вернёт со второго шага кнопкой «Назад», если нужно).

Надёжные локаторы:

поля — по частям placeholder (CSS [*=...]);

кнопка «Заказать» на шаге 2 — только внутри контейнера формы (//div[contains(@class,'Order_Buttons')]/button[.='Заказать']);

кнопка «Да» — внутри модалки подтверждения.

Полезные команды
# запустить в "тихом" режиме (без вывода логов print)
pytest -q

# отфильтровать тесты по имени
pytest -k faq -v

# переиспользовать старый браузер (быстрее) — по желанию
# (для этого нужно изменить scope фикстуры driver на 'session')

Примечания

Баннер cookies закрывается методом accept_cookies() на главной странице.

Даты для заказа генерируются «завтра/послезавтра» в test_data.py, чтобы всегда были валидными.

Если понадобятся негативные проверки валидации — их удобно вынести в отдельный файл tests/test_order_negative.py.

Если что-то не запускается — проверьте, что:

Firefox и geckodriver в PATH;

зависимости установлены в активном venv;

тесты запускаются из корня проекта;

src помечен как Sources Root.

