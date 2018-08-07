from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired


class Dashboard(FlaskForm):
    """Openstack default flask page view form."""
    room = StringField('Room', validators=[DataRequired()])
    submit = SubmitField('Enter Chat room')
