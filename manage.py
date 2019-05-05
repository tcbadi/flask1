# encoding: utf-8

from flask_script import Manager
from app import app
from flask_migrate import Migrate, MigrateCommand
from exts import db
from model import User

manager = Manager(app)

# 使用migrate绑定db和app
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()