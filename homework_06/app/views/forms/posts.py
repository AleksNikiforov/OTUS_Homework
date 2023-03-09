from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField(
        label="Title",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
        render_kw={"placeholder": "Some title"},
    )
    body = StringField(
        "Body",
        validators=[DataRequired()],
        render_kw={"placeholder": "Some text from you"},
    )
