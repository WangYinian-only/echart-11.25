from pyecharts.charts import Bar
from pyecharts import options as opts

bar = Bar()
bar.add_xaxis(["财经", "房产", "游戏", "教育", "军事", "科技", "汽车", "体育", "娱乐", "其它"])
bar.add_yaxis("新闻", [8530, 99, 1197, 399, 78, 730, 546, 400, 797, 0])
# bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
bar.set_global_opts(title_opts=opts.TitleOpts(title="某新闻分类数量"))
bar.render()