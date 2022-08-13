# Асинхронный парсер PEP

Парсер документов PEP на базе фреймворка Scrapy.

## Описание

- Собирает номер, название и статус всех PEP.
- Подсчитывает общее количество каждого статуса, а также общую сумму всех статусов.
Парсер собирает данные с сайта ```https://www.python.org/```
Вся собранная информация сохраняется в файлах с расширением **csv** в папке ***/results/...***

## Как запустить проект

1. Клонировать репозиторий:
```git clone https://github.com/Skrapivn/scrapy_parser_pep.git```

2. Создать виртуальное окружение:
```python -m venv venv```

3. Активировать виртуальное окружение, обновить версию ```pip``` и установить зависимости из ```requirements.txt```:
```source venv/bin/activate```
```python -m pip install -–upgrade pip.```
```pip install -r requirements.txt```

4. Запустить  в консоле
```scrapy crawl pep```

[Sergey K.](https://github.com/skrapivn/)
