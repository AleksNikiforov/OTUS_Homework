from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    title = StringField(
        label="Name",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
        render_kw={"placeholder": "Your name"},
    )
    title = StringField(
        label="Username",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
        render_kw={"placeholder": "Your nickname"},
    )
    title = StringField(
        label="e-mail",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
        render_kw={"placeholder": "Your e-mail"},
    )
