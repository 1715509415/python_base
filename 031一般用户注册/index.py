from flask import Flask, request, render_template
import pymysql
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def register():
    try:
        mysql_connect = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'root', charset = 'utf8', database = 'python')
        mysql_cursor = mysql_connect.cursor()
    except:
        return show_msg('连接数据库失败')
    username = request.form['username']
    truename = request.form['truename']
    password = request.form['pwd1']
    sex = request.form['sex']
    tel = request.form['tel']
    oicq = request.form['oicq']
    email = request.form['email']
    homepage = request.form['homepage']
    address  =request.form['address']

    try:
        sql = "INSERT INTO `user` (`username`, `truename`, `password`, `sex`, `tel`, `oicq`, `email`, `homepage`, `address`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (username, truename, password, sex, tel, oicq, email, homepage, address)
        mysql_cursor.execute(sql)
        mysql_connect.commit()  # 必须加入这行
    except:
        return show_msg('注册失败')
    print(sql)
    return show_msg('恭喜您，注册成功')



def show_msg(msg):
    return "<script type='text/javascript'>alert('%s');window.location='/';</script>" % msg

if __name__ == '__main__':
    app.run()

"""
    将用户的数据写入到数据库中，同样使用execute 执行SQL语句，与查询不同的是，操作增删改则需要提交事务 commit
"""