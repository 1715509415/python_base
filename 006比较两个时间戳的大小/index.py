import time,math

if __name__ == '__main__':
    now_time = int(time.time())  #当前时间戳
    old_time_array = time.strptime('2011-5-5 0:0:0', '%Y-%m-%d %H:%M:%S') #返回struct_time元组
    old_time = int(time.mktime(old_time_array)) # 用mktime将struct_time转化为时间戳
    print(now_time)
    print('输出日期'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time)))
    print('==============================================')

    print(old_time)
    print('输出日期' + time.strftime('%Y-%m-%d %H:%M:%S', old_time_array))

    print('==============================================')

    print('距2011年5月5号已过去%d天' % math.ceil((now_time - old_time) / (3600 * 24)))


"""
    相比之下，用PHP处理时间戳比较简单一点，PHP可以把时间字符串直接转换成时间戳，也可以把时间戳直接转接成时间字符串
    而Python多了一层struct_time层(9个元素的元组)，该时间元组可以通过time.struct_time、time.strptime和time.localtime创建
    Python生成时间戳time.mktime需要使用时间元组作为参数
"""

