from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from info import create_app,db
"""
入口程序
ctrl + alt + o :优化导包,去掉没用的包

"""

app = create_app("develope")


# 把app交给manager进行管理
manager = Manager(app)
# 创建数据库的迁移框架
Migrate(app,db)
# 添加迁移数据库框架的脚本
manager.add_command('xxx',MigrateCommand)


if __name__ == '__main__':
    manager.run()