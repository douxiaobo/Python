from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    name=StringField(
        label='用户名',validators=[
            DataRequired("用户名不能为空"),
            Length(max=10,min=3,message="用户名长度必须在3到10之间")
        ]
    )
    password=PasswordField(
        label='密码',validators=[
            DataRequired("密码不能为空"),
            Length(max=10,min=6,message="密码长度必须在6到10之间")
        ]
    )
    submit=SubmitField(label='登录')


# UndefinedError jinja2.exceptions.UndefinedError: 'models.LoginForm object' has no attribute 'submit'
# 办法是写上submit