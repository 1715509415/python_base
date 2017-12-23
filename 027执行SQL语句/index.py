from flask import Flask,request, render_template
import pymysql

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sql = request.form['text']
        if len(sql) == 0:
            return show_msg('请输入sql语句')
        try:
            mysql_connect = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'root', charset = 'utf8', database = 'xiaofu')
            mysql_cursor = mysql_connect.cursor()
        except:
            return show_msg('数据库连接失败')
        operation = '执行插入' if 'INSERT' in sql else '更新查询'

        try:
            mysql_cursor.execute(sql)
            return show_msg('您在{}操作'.format(operation))
        except:
            return show_msg('SQL语句出现错误')
    return render_template('index.html')

def show_msg(msg):
    return "<script type='text/javascript'>alert('{}');location.href='/';</script>".format(msg)

if __name__ == '__main__':
    app.run()

"""
    连接数据库的目的是为了让程序控制数据库的增、删、改、查等操作，该案例使用execute执行sql语句，
    同样使用异常判断是否执行成功。
    其实可以把语句都放在try里面，然后捕获可能出现的错误，即可以写多个except语句
"""