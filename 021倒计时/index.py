import time, math
if __name__ == '__main__':
    now_time = int(time.time())
    target_time = int(time.mktime(time.strptime('2019-01-01', '%Y-%m-%d')))
    print('距2019元旦还有%d天' %  math.ceil((target_time - now_time) / (3600 * 24)))

"""
    所有时间到比较到头来都是时间戳到比较，PHP需要设置默认时区，而Python不用
    就是Python中时间字符串与时间戳的转换相比PHP比较麻烦一点
"""