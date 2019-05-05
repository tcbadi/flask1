#encoding: utf-8

from flask import Flask, render_template, make_response, redirect, request, url_for, session
from flask_bootstrap import Bootstrap
from model import User, Part, Part_Apqp
from exts import db
import config

app = Flask(__name__)
app.config.from_object(config)
bootstrap = Bootstrap(app)
db.init_app(app)


@app.route('/')
def index():
    # return 'Hello World!123'
    # 增：
    # article1 = Article(title='aaa', content='bbb')
    # db.session.add(article1)
    # db.session.commit()

    # 查,改,删：
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # article1.title = 'leo'
    # article1.content = 'ok'
    # db.session.commit()
    # article2 = Article.query.filter(Article.title == 'leo').first()
    # db.session.delete(article2)
    # db.session.commit()

    return render_template("index.html")


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password == password).first()
        if user:
            session['user.id'] = user.id
            # pyhon后端用request.values.get("name")去获取
            if request.values.get("jizhuwo"):
                session.permanent = True
            return redirect(url_for('index'))
        else:
            return '用户不存在，请重新输入或注册新用户！'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        #         手机号码验证，如果已经注册，就不能再注册了
        user = User.query.filter(User.telephone == telephone).first()
        if telephone == "" or username == "" or email == "" or password1 == "":
            return '输入信息不能为空！'
        elif user:
            return '该手机号已注册，请更换手机号码！'
        else:
            # 验证password1和password2是否相等
            if password1 != password2:
                return '两次密码不一致，请重新输入！'
            else:
                user = User(telephone=telephone, username=username, password=password1, email=email)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.context_processor
def my_context_processor():
    # 下面3行语句用来判断用户是否登陆
    user_id = session.get('user.id')
    user = User.query.filter(User.id == user_id).first()
    if user:
        part = Part.query.filter(Part.sta1 == user.username).all()
        print(part)
        return {'user': user, 'part': part}
    else:
        return {'part': 1}


@app.route('/partlist/', methods=['GET', 'POST'])
def partlist():
    if request.method == 'GET':
        user_id = session.get('user.id')
        user = User.query.filter(User.id == user_id).first()
        if user:
            return render_template('partlist.html')
        else:
            return redirect(url_for('login'))
    else:
        part_name1 = request.form.get('part_name1')
        part_no1 = request.form.get('part_no1')
        supplier1 = request.form.get('supplier1')
        sta1 = request.form.get('sta1')
        pm1 = request.form.get('pm1')
        project1 = request.form.get('project1')
        ls_time1 = request.form.get('ls_time1')
        # 同一件号，同一供应商的零件，只能有一个。
        # 空白数据现在也能加入数据库，需解决。
        part = Part.query.filter(Part.part_no1 == part_no1 , Part.supplier1 == supplier1).first()
        if part_name1 == "" or part_no1 == "" or supplier1 == "" or ls_time1 == "":
            return '新增零件需要提供的信息至少包括：零件名称，零件号，供应商，投产时间！'
        elif part:
            return '该供应商零件号已存在，请重新确认录入信息！'
        else:
            part = Part(part_name1=part_name1, part_no1=part_no1, supplier1=supplier1, sta1=sta1, pm1=pm1, project1=project1, ls_time1=ls_time1)
            db.session.add(part)
            db.session.commit()
            return render_template('partlist.html')


@app.route('/part_apqp/<part_id>/')
def apqp(part_id):
    part = Part.query.filter(Part.id == part_id).first()
    return render_template('part_apqp.html', part_name1= part.part_name1, part_no1= part.part_no1)

if __name__ == '__main__':
    app.run()
