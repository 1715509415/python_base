from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_form():
    return """
        <form action='/' method='post'>
            <p><input name='text'></p>
            <p><input name='password' type='password'></p>
            <p><button type='submit'>登陆</button></p>
        </form>
    """
@app.route('/', methods=['POST'])
def home():
    if (request.form['text'] == 'admin') and (request.form['password'] == 'admin'):
        return """
                <script type='text/javascript'>alert('您具有管理权限');</script>
            """
    return """
        <script type='text/javascript'>alert('您非权限用户');</script>
    """

if __name__ == '__main__':
    app.run()

"""
    此例子使用了flask模块搭建网络服务
    PHP逻辑与有两种写法，分别是&&和and
    Python使用的是and
"""