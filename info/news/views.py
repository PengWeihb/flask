from info import constants
from info.models import News
from . import news_blue
from flask import render_template
@news_blue.route('/<int:news_id>')
def news_detail(news_id):
    # 查询首页右边的热门排行新闻数据
    news = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)



    news_list = []

    for new_model in news:
        news_list.append(new_model.to_dict())
    data = {
        "click_news_list": news_list,
    }
    return render_template('news/detail.html',data = data)