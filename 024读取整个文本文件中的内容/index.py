if __name__ == '__main__':
    file = open('test1.txt')
    for line in file.readlines():
        print(line) #一次读取一行

    file.close()

    with open('test1.txt') as file:
        print(file.readlines()) #将整个文件到内容读入到列表中


    with open('test2.txt') as file:
        print(file.read())  #将整个文件内容读入到字符串中


"""
    Python操作文件的思路基本上和PHP一样，打开文件后最后需要关闭资源。
    Python中用with打开文件，不用手动关闭，系统会自动关闭资源
    在操作比较大的文件时，最好一次读取一行，否则会造成系统资源的浪费
    
    如果读取的文件不是UTF-8,则需要设置encoding参数
"""
