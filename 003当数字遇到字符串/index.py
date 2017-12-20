a = 20
b = '我是字符串型数据'
b1 = '10'
if __name__ == '__main__':
    try:
        # e = a + int(b)
        f = str(a) + b
        g = a + int(b1)
        print(f)
        # print(e)
        print(g)
    except ValueError as e:
        print('非数字字符串无法转换整形')

"""
Python的数据类型比PHP严格一些，PHP支持数字和字符串进行相加操作，Python需要同类型变量才能进行相加操作
"""