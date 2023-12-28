import random
import string

from flask import abort, flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from settings import LOCAL_HOST

MAX_CHARACTER = 6


def get_unique_short_id():
    """Функция для автоматического формирования коротких символов."""
    url = URLMap.query.all()
    url_short = [f.short for f in url]
    random_character_generation = ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=MAX_CHARACTER
        )
    )
    while random_character_generation in url_short:
        random_character_generation = ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=MAX_CHARACTER
            )
        )
    return random_character_generation


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """Функция для создания коротких ссылок."""
    form = URLMapForm()
    if form.validate_on_submit():
        if URLMap.query.filter_by(short=form.custom_id.data).first() is not None:
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('urlmap.html', form=form)
        if form.custom_id.data is None or not form.custom_id.data.strip():
            custom_id = get_unique_short_id()
        else:
            custom_id = form.custom_id.data
        urlmap = URLMap(
            original=form.original_link.data,
            short=custom_id
        )
        db.session.add(urlmap)
        db.session.commit()
        result = LOCAL_HOST + urlmap.short
        return render_template('urlmap.html', form=form, result=result)
    return render_template('urlmap.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def urlmap_view(short_id):
    """Функция для переадрисация ссылки."""
    url = URLMap.query.filter_by(short=short_id).first()
    if url is not None:
        return redirect(url.original)
    abort(404)
