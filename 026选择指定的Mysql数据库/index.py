from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        mysql_connect = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'root', charset = 'utf8')
        tables = []
        with mysql_connect.cursor() as cursor:
            cursor.execute('show databases')
            for item in cursor.fetchall():
                tables.append(item[0])

    except:
        return "<script type='text/javascript'>alert('数据库连接失败');location.href='/';</script>"

    if request.method == 'POST':
        if request.form['select'] == '1':
            return "<script type='text/javascript'>alert('请选择数据库');location.href='/';</script>"
        try:
            mysql_connect.select_db(request.form['select'])
            return "<script>alert('已选择指定数据库');location.href='/';</script>"
        except:
            return "<script type='text/javascript'>alert('选择数据库失败');location.href='/';</script>"

    return render_template('index.html', tables = tables)
if __name__ == '__main__':
    app.run(port=5001)

"""
    使用select_db选择数据库，当然也可以设置connect的database参数来选择
    这里同样使用异常来判断是否成功选择数据库
"""