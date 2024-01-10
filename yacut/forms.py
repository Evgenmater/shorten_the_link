from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from settings import PATTERN, MAX_LENGTH


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Добавьте длинную ссылку',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(max=MAX_LENGTH),
            Optional(),
            Regexp(
                PATTERN,
                message='Допустимый ввод только большие или маленькие латинские буквы и цифры без пробела.'
            )
        ]
    )
    submit = SubmitField('Создать')
