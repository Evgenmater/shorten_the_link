from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Добавьте длинную ссылку',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Optional(),
            Regexp(
                '^[0-9a-zA-Z]+$',
                message='Допустимый ввод только большие или маленькие латинские буквы и цифры без пробела.'
            )
        ]
    )
    submit = SubmitField('Создать')
