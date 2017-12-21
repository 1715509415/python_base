from flask import Flask, request, render_template
import re
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    content = None
    if request.method == 'POST':
        if len(request.form['text']) == 0 or (len(request.form['te']) == 0 and request.form['check'] == '1'):
            return """
                <script type='text/javascript'>alert('内容不能为空');location.href='/'</script>
            """
        else:
            if len(request.form['check']) or request.form['select'] != '1':
                content = '标题：%s<br/>%s' % (request.form['text'], handle_str(request.form['te'] + request.form['check']))
            else:
                content = '标题：%s<br/>%s' % (request.form['text'], request.form['te'])
    return render_template('index.html', content = content)

def handle_str(string):
    string = re.sub(' ', '&nbsp;', string)
    string = re.sub('\r\n', '<br/>', string, re.S)
    return '内容：%s' % string

if __name__ == '__main__':
    app.run()

"""
    flask里带有模板引擎模块，可以直接渲染模板，只是注意模板必须放在templates目录里,模板引擎语法与PHP框架差不多，
    静态文件一般放在static目录里，也可以使用url_for构造
    使用re正则表达式模块处理空格符和回车符
"""