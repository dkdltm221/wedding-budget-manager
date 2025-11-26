from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, HiddenField
from wtforms.validators import DataRequired, NumberRange, Optional


class GuestForm(FlaskForm):
    name = StringField('이름', validators=[DataRequired()])
    side = SelectField('측', choices=[('groom', '신랑 측'), ('bride', '신부 측')], validators=[DataRequired()])
    amount = IntegerField('금액', validators=[DataRequired(), NumberRange(min=0, message="0 이상 입력하세요")])
    note = StringField('메모', validators=[Optional()])
    csrf_token = HiddenField()  # 템플릿 미사용 시에도 필드 정의


class ExpenseForm(FlaskForm):
    category = StringField('항목명', validators=[DataRequired()])
    description = StringField('설명/메모', validators=[Optional()])
    amount = IntegerField('금액', validators=[DataRequired(), NumberRange(min=0, message="0 이상 입력하세요")])
    csrf_token = HiddenField()
