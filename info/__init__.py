from flask import Flask

from config import Config,DevelopementConfig,ProdutionConfig,config_map

from flask_sqlalchemy import SQLAlchemy

import redis

from flask_wtf import CSRFProtect

from flask_session import Session

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

    # 如果看不懂包的结构,通过alt + 回车
    from info.index import index_blue
    app.register_blueprint(index_blue)

    return app

