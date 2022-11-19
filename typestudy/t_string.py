def func_main():
    # func_for_string()
    func_str_func()
    pass


def func_occupy():
    # f占位符 连接字符串
    name = "World"
    s = f'Hello {name}'
    print(s)

    # 占位符 连接字符串
    s1 = "Hello %s" % name
    print(s1)


def func_for_string():
    # s = "hello world"

    # 字符串长度使用len函数
    # print(len(s))
    # for循环可以遍历字符串
    # for i in s:
    #     print(i)

    # 字符串不支持通过索引进行修改
    # 'str' object does not support item assignment
    # s[0] = 's'
    # print(s)

    # 可以通过截取部分字符串再次拼接的方式，或者直接覆盖进行赋值
    # print('-------')
    # s = s[0:2] + 'bb'
    # print(s)
    # print('-------')
    # 截取字符串,[开始->结束]，不包含结束位置的字符，0表示从开头截取，-1表示从末尾截取
    # s1 = s[0:2]
    # print(s1)
    # *运算符，重复字符串本身
    # s2 = s * 2
    # print(s2)
    # in 成员运算符 - 如果字符串中包含给定的字符返回 True
    # not in 成员运算符 - 如果字符串中不包含给定的字符返回 True
    # 原始字符串 所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
    print(r'ssss\n')
    print('ssss\n')
    print(R'xxxxx\n')
    print('xxxxx\n')
    pass


def func_str_func():
    s = 'helloworld'
    # capitalize() 首字母大写
    s1 = s.capitalize()
    print(s1)
    # center(width, fillchar)返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
    s2 = s.center(3)
    print(s2)
    # count(str, beg= 0,end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
    s3 = s.count('l')
    print(s3)
    # endswith(suffix, beg=0, end=len(string)) 检查字符串是否以 suffix 结束，如果 beg 或者 end 指定则检查指定的范围内是否以 suffix 结束，如果是，返回 True,否则返回 False。
    s4 = s.endswith('l')
    print(s4)
    # find(str, beg=0, end=len(string)) 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
    s5 = s.find('l')
    print(s5)
    # index(str, beg=0, end=len(string)) 跟find()方法一样，只不过如果str不在字符串中会报一个异常。
    s6 = s.index('l')  # ValueError: substring not found
    print(s6)
