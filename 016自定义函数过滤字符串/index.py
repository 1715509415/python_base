from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home_form():
    return """
        <form action='/' method='post'>
            <p>内容：<textarea name='content'></textarea>
            <p><button type='submit'>提交</button></p>
        </form>
    """

@app.route('/', methods=['POST'])
def home_action():
    return handle_str(request.form['content'])
def handle_str(content):
    datas = str(['图书', '明日科技', '软件', '编程词典', '编程', '词典'])
    if content in datas:
        return """
            <script type='text/javascript'>alert('您使用了禁用词语，请重新输入');location.href='/'</script>
        """
    return '内容为：%s' % content

if __name__ == '__main__':
    app.run()


"""
    Python的in操作符可以判断元素是否包含在序列中，序列包括字符串、列表和元组，
    也可以使用正则表达式，只限制在字符串使用，有兴趣的可以试一下
"""