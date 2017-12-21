from flask import Flask, request, render_template
import pymysql
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
@app.route('/action', methods=['POST'])
def action():
    if len(request.form['host']) == 0 or len(request.form['user']) == 0 or len(request.form['password']) == 0:
        return "<script type='text/javascript'>alert('文本框不能为空');</script>"
    try:
        pymysql.connect(host = request.form['host'], user = request.form['user'], password = request.form['password'])
        return "<script type='text/javascript'>alert('连接MySQL服务器成功');location.href='/';</script>"
    except:
        return "<script type='text/javascript'>alert('错误了');location.href='/';</script>"
if __name__ == '__main__':
    app.run()

"""
    本案例使用pymysql模块连接数据库，用异常来判断是否连接成功，PHP可以使用@来抑制错误提示，用返回类型判断是否连接成功，当然用异常可以让代码更加健壮
    另外PHP不建议继续使用mysql系统函数操作数据库，用mysqli或pdo来操作Mysql数据库
"""