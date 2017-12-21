if __name__ == '__main__':
    str1 = 'I Like Python'
    str2 = str1
    print(str1,str2)

    str2 = 'I Like PHP'
    print(str1, str2)

    str3 = 'I Like PHP'

    print(id(str2), id(str3))


    """
        由于PHP与Python表达变量的意义不一样，所以PHP的可变变量在Python中是不存在的
        Python的任何类型都是对象，变量只是对象的一个引用，如上面str2一开始是与str1一样指向'I Like Python'对象的引用
        str2后面指向了另外一个不同的对象，此过程中不影响str1的指向
        str3也是同样指向'I Like PHP'对象的引用，所以str2和str3指向同一个对象，此特点对于Python来说可节省不少内存空间
    """