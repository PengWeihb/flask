import logging
from info import db
from . import index_blue
from flask import render_template,current_app
@index_blue.route("/")
def index():
    # logging.debug("This is a debug log.")
    # logging.info("This is a info log.")
    # logging.warning("This is a warning log.")
    # logging.error("This is a error log.")
    # logging.critical("This is a critical log.")
    # current_app:表示代理人对象,代理的app对象

    return render_template('news/index.html')

@index_blue.route('/favicon.ico')
def send_img():

    return current_app.send_static_file('news/favicon.ico')