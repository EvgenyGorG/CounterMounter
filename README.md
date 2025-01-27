# Обрезка ссылок с помощью VK 

Скрипт позволяет обрезать ссылку, а так же посмотреть количество переходов
по сокращенной ссылке.

### Как установить

Для работы скрипта необходим [Сервисный ключ к API VK](https://id.vk.com/about/business/go/docs/en/vkid/latest/vk-id/connection/tokens/service-token).
Необходимо создать `.env` файл, в котором будет храниться
переменная окружения `VK_SERVICE_TOKEN` [Сервисный ключ к API VK](https://id.vk.com/about/business/go/docs/en/vkid/latest/vk-id/connection/tokens/service-token).

[Python3](https://www.python.org/downloads/) должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2)
для установки зависимостей:
```
pip install -r requirements.txt
```

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)
для изоляции проекта.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе
для веб-разработчиков [dvmn.org](https://dvmn.org/).