from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    phonenumber = StringField('请输入本人手机号码', validators=[DataRequired(), Length(11)])
    password = PasswordField('请输入密码', validators=[DataRequired()])
    remember_me = BooleanField('记住本次登陆（请勿在公共设备勾选）')
    submit = SubmitField('登陆')


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[
    DataRequired(), Length(4, 8),
    Regexp('^[A-Za-z0-9_\u4e00-\u9fa5]{4,8}$', 0,
           '用户名可以是字母或汉字，长度4-8位')])
    phonenumber = StringField('本人手机号码', validators=[DataRequired(),
        Regexp('^(13[0-9]|14[5|7]|15[0|1|2|3|4|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$', 0, '接收13，14，15，18开头的手机号码注册')])
    email = StringField('Email(电子邮箱)', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[DataRequired(),
        Regexp('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$', 0, '密码必须是包含大小写字母和数字的组合，不能使用特殊字符，长度小于20个字符')])
    password2 = PasswordField('再次输入密码', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    isteacher = RadioField('是否是教师', choices=[('t', '教师'), ('s', '学生或者家长')], validators=[DataRequired()])
    submit = SubmitField('提交注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名重复或不可用，请更换用户名')


    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('邮箱重复或不可用，请更换用户名')

    def validate_phonenumber(self, field):
        if User.query.filter_by(phonenumber=field.data).first():
            raise ValidationError('该手机号码已注册，请更换')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[DataRequired()])
    password = PasswordField('新密码', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('请再次输入密码',
                              validators=[DataRequired()])
    submit = SubmitField('更新密码')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email(电子邮箱)', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('重置密码')


class PasswordResetForm(FlaskForm):
    password = PasswordField('新密码', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('确认密码（请再次输入）', validators=[DataRequired()])
    submit = SubmitField('提交新密码')


class ChangeEmailForm(FlaskForm):
    email = StringField('新的邮箱', validators=[DataRequired(), Length(1, 64),
                                                 Email()])
    password = PasswordField('升学内参登陆密码（不是邮箱的密码）', validators=[DataRequired()])
    submit = SubmitField('更新我的邮箱')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('该邮箱已经被注册。')
