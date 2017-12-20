import random, time
if __name__ == '__main__':
    arr1 = ['生日快乐', '今天是你的出生日', '同学们为你许愿']
    arr2 = ['祝你万事如意', '祝你生日快乐', '祝你福如东海长流水寿比南山不老松']
    print(random.choice(arr1), random.choice(arr2))

    random.seed(time.time())

    rand = random.randint(0,2)
    print(arr1[rand], arr2[rand])


"""
    Python的random模块可以生成随机数，如random.randint，为了提离随机性，使用了seed播种随机种子，
    也可以用random.choice随机返回一个序列单位
"""