Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Evgenmater/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить проект:

```
flask run
```

Примеры запросов к API:

* POST-запрос на создание новой короткой ссылки.

    ```
    http://127.0.0.1:5000/api/id/
    ```
* GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору

    ```
    http://127.0.0.1:5000/api/id/<short_id>/
    ```