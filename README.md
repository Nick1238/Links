# Обрезка ссылок с помощью Битли

Скрипт для создания коротких ссылок с помощью Битли и проверки количества переходов по ним.

### Как установить

Для работы скрипта потребуется API-ключ Bitly. Получить ключ можно на сайте [Bitly](https://bitly.com/)

После получения токена необходимо создать файл .env в корневой папке проекта и скопировать туда ключ с именем `BITLY_TOKEN`:
```angular2html
BITLY_TOKEN=SECRET_KEY_HERE
```
[документация по работе с Bitly](https://dev.bitly.com/)

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).