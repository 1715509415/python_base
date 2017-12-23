from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    content = 'PHP作为全球最普及、应用最广泛的互联网开发语言之一，从1994年诞生至今已被2000多万个动态网站采用，全球知名互联网公司Google、Yahoo、eBay和中国知名网站新浪、百度、阿里巴巴等均采用PHP技术！'
    new_content = None
    if request.method == 'POST':
        sub = request.form['text']
        new_content = content.replace(sub, "<b style='color:red;font-size:18px;'>%s</b>" % sub)
    return render_template('index.html', content = content, new_content = new_content)

if __name__ == '__main__':
    app.run()

"""
    Python中字符串对象提供replace方法进行子串替换操作
    另外注意的是模板引擎中使用safe方法能将html进行输出，否则只是普通的字符串
"""