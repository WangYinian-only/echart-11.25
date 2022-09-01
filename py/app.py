from flask_bootstrap import Bootstrap
import pymysql
from flask import Flask, render_template, jsonify, request
import test

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/caijing")
def cai():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='602511dtywyy', db='pyimport', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM caijing"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('caijing.html', cj=u)


@app.route('/fangchan')
def fang():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='602511dtywyy', db='pyimport', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM fangchan"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('fangchan.html', fc=u)


@app.route('/jiaoyu')
def jiao():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='602511dtywyy', db='pyimport', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM jiaoyu"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('jiaoyu.html', jy=u)


@app.route('/keji')
def ke():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='602511dtywyy', db='pyimport', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM keji"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('keji.html', kj=u)


@app.route('/junshi')
def jun():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='602511dtywyy', db='pyimport', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM junshi"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('junshi.html', js=u)


@app.route('/qiche')
def qi():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='602511dtywyy', db='pyimport', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM qiche"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('qiche.html', qc=u)


@app.route('/tiyu')
def ti():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='602511dtywyy', db='pyimport', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM tiyu"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('tiyu.html', ty=u)


@app.route('/yule')
def yu():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='602511dtywyy', db='pyimport', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM yule"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('yule.html', yl=u)


@app.route('/games')
def games():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='602511dtywyy', db='pyimport', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM games"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('games.html', g=u)


@app.route('/qita')
def qit():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='602511dtywyy', db='pyimport', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM qita"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('qita.html', qt=u)


@app.route('/')
def index():
    return render_template('tree.html')


@app.route('/render')
def echart():
    return render_template('render.html')


@app.route('/word')
def word():
    return render_template("word.html")


@app.route('/xiaoxi')
def xiaoxi():
    return render_template("xiaoxi.html")


# 词云图通过type区别
@app.route("/word_cloud_data_type")
def word_cloud_data_type():
    type = request.values.get("type")
    print(type)
    articlelist = test.find_word_bySql(type)
    word_cloud_num = []
    flag = 0
    for i in articlelist:
        word_cloud_num.append({"name": i[0], "value": i[1]})
        flag = flag + 1;
        if (flag > 100):
            break
    return jsonify({"data": word_cloud_num})
    pass


if __name__ == '__main__':
    app.run(debug=True)
