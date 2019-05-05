# encoding: utf-8

from exts import db

# 用户列表
# nullable=False表示该列不能为空，但是可以为“”，所以感觉没乱用，需要配合if==“”进行判断
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False)

# 零件列表
class Part(db.Model):
    __tablename__ = 'part'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    part_name1 = db.Column(db.String(50), nullable=False)
    part_no1 = db.Column(db.String(20), nullable=False)
    supplier1 = db.Column(db.String(50), nullable=False)
    sta1 = db.Column(db.String(20), nullable=False)
    pm1 = db.Column(db.String(20), nullable=False)
    project1 = db.Column(db.String(20), nullable=False)
    ls_time1 = db.Column(db.String(20), nullable=False)


# class Part(db.Model):
#     __tablename__ = 'part'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     part_name1 = db.Column(db.String(50), nullable=False)
#     part_no1 = db.Column(db.String(20), nullable=False)
#     supplier1 = db.Column(db.String(50), nullable=False)
#     pm1 = db.Column(db.String(20), nullable=False)
#     project1 = db.Column(db.String(20), nullable=False)
#     ls_time1 = db.Column(db.String(20), nullable=False)
#
#     sta_id = db.Column(db.Integer, db.ForeignKey(User.id))
#     sta1 = db.relationship('User', backref = db.backref('parts'))

# 零件APQP计划
class Part_Apqp(db.Model):
    __tablename__ = 'part_apqp'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sko_date = db.Column(db.String(50), nullable=False)
    sko_output = db.Column(db.String(50), nullable=False)
    ftf_date = db.Column(db.String(50), nullable=False)
    ftf_output = db.Column(db.String(50), nullable=False)
    ott_date = db.Column(db.String(50), nullable=False)
    ott_output = db.Column(db.String(50), nullable=False)
    ots_date = db.Column(db.String(50), nullable=False)
    ots_output = db.Column(db.String(50), nullable=False)
    tto_date = db.Column(db.String(50), nullable=False)
    tto_output = db.Column(db.String(50), nullable=False)
    psw_date = db.Column(db.String(50), nullable=False)
    psw_output = db.Column(db.String(50), nullable=False)


# 数据库迁移需要初始化，在命令行的虚拟环境下执行：
# （venv）>python manage.py db init
# （venv）>python manage.py db migrate
# （venv）>python manage.py db upgrade
# 更新Column后，需要再次执行migrate和upgrade
# （venv）>python manage.py db migrate
# （venv）>python manage.py db upgrade

