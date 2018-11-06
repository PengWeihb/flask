from flask import g
from flask import session

from info import constants
from info.models import News, User
from . import news_blue
from flask import render_template
from info.utils.common import user_login_data
@news_blue.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):

    user = g.user

    # 查询首页右边的热门排行新闻数据
    news = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)



    news_list = []

    for new_model in news:
        news_list.append(new_model.to_dict())

    # 根据新闻id获取到详情页面的数据
    news_content =  News.query.get(news_id)



    data = {
        "user_info": user.to_dict() if user else None,
        "click_news_list": news_list,
        "news":news_content
    }
    return render_template('news/detail.html',data = data)