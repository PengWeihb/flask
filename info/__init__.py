import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

from config import Config,DevelopementConfig,ProdutionConfig,config_map

from flask_sqlalchemy import SQLAlchemy

import redis

from flask_wtf import CSRFProtect

from flask_session import Session


# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG) # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)

# 创建数据库对象,一定要注意上面加载配置文件和数据库的代码顺序不能混淆
db = SQLAlchemy()
def create_app(config_name):

    app = Flask(__name__)

    # 获取配置文件里面的key
    name =  config_map.get(config_name)
    # 加载配置文件DevelopementConfig,ProdutionConfig
    app.config.from_object(name)
    # 初始化
    db.init_app(app)
    # 创建redis对象(用来存储验证码,图片验证码和短信验证码)
    redis_store =  redis.StrictRedis(host=name.REDIS_HOST,port=name.REDIS_PORT)
    # 开启CSRF保护,避免视图函数受到攻击
    CSRFProtect(app)
    # 开启session
    Session(app)

    # 首页
    from info.index import index_blue
    app.register_blueprint(index_blue)

    # 登陆注册
    from info.passport import passport_blue
    app.register_blueprint(passport_blue)

    return app

