# encoding: utf-8

# 解决循环引用问题，创建db为SQLAlchemy对象

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
