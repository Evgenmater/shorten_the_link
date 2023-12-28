import re

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id
from settings import LOCAL_HOST


@app.route('/api/id/', methods=['POST'])
def add_url():
    """Функция для создания коротких ссылок в API."""
    pattern = re.compile('^[0-9a-zA-Z]+$')
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    if 'custom_id' not in data or data['custom_id'] is None or not data['custom_id'].strip():
        short = get_unique_short_id()
        data['custom_id'] = short
    if pattern.search(data['custom_id']) is None or len(data['custom_id']) > 16:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')
    url = URLMap()
    fields = {'original': data['url'], 'short': data['custom_id']}
    url.from_dict(fields)
    db.session.add(url)
    db.session.commit()
    return jsonify(
        {
            'url': url.to_dict()['original'],
            'short_link': LOCAL_HOST + url.to_dict()['short']
        }
    ), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    """Функция для создания коротких ссылок в API."""
    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url.to_dict()['original']}), 200
