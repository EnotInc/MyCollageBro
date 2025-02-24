# MyCollageBro

Телеграмм бот [MyCollageBro](https://t.me/mycollagebrobot) предназначен для упрощения получения расписания с сайта колледжа. Пока проект в разработке и многих функций еще не хватает но базовый функционал уже в полне обширен и предлагает пользователям удобный вариант получения расписания на неделю

## Содержание
- [О работе бота](#о-работе-бота)
- [Самостоятельный запуск](#самостоятельный-запуск)
- [Команда разработки](#команда-разработки)

## О работе бота

Думаю каждый имеет представление о работе телеграм ботов. Ты нажимиешь на кнопки и он тебе что-то выдает в ответ. [Данный](https://t.me/mycollagebrobot) бот делает тоже самое.
Ты выбираешь за какую неделю хочешь получить расписание, а затем выбираешь курс, на котором сейчас обучаешься. Бот, получив данную информацию, отправляет необходимый файл с расписанием.
Но етсь загвоздка. Расписание на сайте обнавляетсься по вторникам. А это значит что в понедельник, при запросе расписания на данную неделю, бот будет высылать файл с расписанием прошлой недели. Разраб, к своему сожалению, ленивая жопа, и ближайшее время не планирует решать данную проблему. Уж сорян :)

## Самостоятельный запуск

***Важно!***
Для запуска всех команд необходимо находиться непосредственно в директории проекта

### Необходимые библиотеки

Для запуска проекта на локальной машине необходимо сначала установить следующие библиотеки:


#### *aiogram*

```sh
pip install aiogram 
```
библиотека для создания бота. Подробее с ней вы можете ознакомиться на сайте с [документацией](https://docs.aiogram.dev/en/v3.18.0/)

---

#### *dotenv*

```sh
pip install dotenv
```

библиотека необходимая для создания .env файла, в котором должны содержаться следующие константы:

```python
TOKEN='ТОКЕН ВАШЕГО ТГ БОТА'
URL='СЫЛЛКА НА ЗАПРОС С JSON ОТВЕТОМ, В КОТОРОМ ХРАНИТЬСЯ НЕОБХОДИМЫЕ ВАМ ФАЙЛЫ'
LINK='ССЫЛКА НА ГЛАВНУЮ СТРАНИЦУ САЙТА'
ACCEPT='ACCEPT'
USER_AGENT='USER_AGENT'
```

***ВАЖНО!***
Логика работы сайта в разных коледжах может координально отличаться, и шанс того что мое решение подойте вам крайне мал. По хорошему вам следует самим разобраться с тем, как извлечь расписание с вашего сайта и перепесать файл parser.py под себя.

---

#### *emoji*

```sh
pip install emoji
```

это библиотека позволяющая боту отправлять и видеть эмодзи телеграма.

### Запуск проекта

Проект необходимо запускать в консоли, используя следующую команду:
```sh
py app.py
```

Если данная команда не работает, можно использовать другую:
```sh
python app.py
```

## Команда разработки

- Мосов Егор - разработчик. Студент 1-го курса. 