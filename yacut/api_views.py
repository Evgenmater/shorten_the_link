import re
from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id
from settings import PATTERN, MAX_LENGTH


@app.route('/api/id/', methods=['POST'])
def add_url():
    """Функция для создания коротких ссылок в API."""
    pattern = re.compile(PATTERN)
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if 'custom_id' not in data or data['custom_id'] is None or not data['custom_id'].strip():
        short = get_unique_short_id()
        data['custom_id'] = short
    elif len(data['custom_id']) > MAX_LENGTH or pattern.search(data['custom_id']) is None:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')
    url = URLMap(original=data['url'], short=data['custom_id'])
    db.session.add(url)
    db.session.commit()
    return jsonify(
        {
            'url': url.to_dict()['original'],
            'short_link': url_for('index_view', _external=True) + url.to_dict()['short']
        }
    ), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    """Функция для создания коротких ссылок в API."""
    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url.to_dict()['original']}), HTTPStatus.OK
