from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'


@app.route('/')
def index():
    articles = [
        {'title': 'Web 开发入门', 'author': 'John', 'content': '这是一篇关于 Web 开发入门的文章。'},
        {'title': 'Python 基础教程', 'author': 'Jiet_h', 'content': '这是一篇关于 Python 基础教程的文章。'},
        {'title': '数据科学实践', 'author': 'Mike', 'content': '这是一篇关于数据科学实践的文章。'}
    ]
    return render_template('blogs.html', articles=articles)


class RegistrationForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    submit = SubmitField('注册')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        # 处理表单数据...
        return f'注册成功！name is {name}, email is {email}'

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()
