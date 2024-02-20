import json
import collections
import decimal


def func_main():
    func_loads()


def func_dumps():
    # python数据转json
    data = {"name": "许磊", "address": "地址"}

    # 将python对象编码成Json字符串
    # ensure_ascii=True：默认输出ASCLL码，如果把这个该成False,就可以输出中文。
    # check_circular：如果check_circular为false，则跳过对容器类型的循环引用检查，循环引用将导致溢出错误(或更糟的情况)。
    # allow_nan：如果allow_nan为假，则ValueError将序列化超出范围的浮点值(nan、inf、-inf)，严格遵守JSON规范，而不是使用JavaScript等价值(nan、Infinity、-Infinity)。
    # default：default(obj)是一个函数，它应该返回一个可序列化的obj版本或引发类型错误。默认值只会引发类型错误。
    # skipkeys：默认值是False，如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key 。
    # sort_keys =True:是告诉编码器按照字典排序(a到z)输出。如果是字典类型的python对象，就把关键字按照字典排序。
    # indent:参数根据数据格式缩进显示，读起来更加清晰
    # separators:是分隔符的意思，参数意思分别为不同dict项之间的分隔符和dict项内key和value之间的分隔符，把：和，后面的空格都除去了。
    jsonStr = json.dumps(data, indent=True, separators=(',', ':'), ensure_ascii=False)
    print(jsonStr)

    # json.dump() 是把python对象转换成json对象生成一个fp的文件流，和文件相关。
    pass


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def toJSON(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }

    @staticmethod
    def parseJSON(dct):
        if isinstance(dct, dict):
            p = Person(dct["name"], int(dct['age']), dct['gender'])
            return p
        return dct


def func_loads():
    # json.load()从json文件中读取数据

    # json.loads() json转python数据,json里的key必须是双引号
    jsonStr = '{"user_id": "66", "movie_id": "357", "rating": "5", "time": "2009"}'
    data = json.loads(jsonStr)
    print(data)

    s = '{"name": "马云", "age": 54, "gender": "man"}'
    # 测试json.loads方法的object_hook参数
    # object_hook参数是可选的，它会将（loads的)返回结果字典替换为你所指定的类型,这个功能可以用来实现自定义解码器，如JSON-RPC
    p = json.loads(s, object_hook=Person.parseJSON)
    print("json.loads 是否将字符串转为字典了: --> " + str(isinstance(p, dict)))
    print("json.loads 是否将字符串转为Person对象了: --> " + str(isinstance(p, Person)))

    s = '{"name": "马云", "age": 54, "gender": "man"}'
    # 测试json.loads方法的object_pairs_hook参数
    # object_pairs_hook参数是可选的，它会将结果以key-value有序列表的形式返回,形式如：[(k1, v1), (k2, v2), (k3, v3)],如果object_hook和object_pairs_hook同时指定的话优先返回object_pairs_hook
    print("-" * 30 + "> test object_pairs_hook <" + "-" * 30)
    p = json.loads(s, object_hook=Person.parseJSON, object_pairs_hook=collections.OrderedDict)
    # p = json.loads(s, object_hook=Person.parseJSON, object_pairs_hook=Person.parseJSON)
    print("json.loads 测试同时指定object_hook和object_pairs_hook,最终调用哪个参数: --> " + str(type(p)))
    print("json.loads 指定object_pairs_hook结果将会返回一个有序列表 --> {}".format(p))

    # 测试json.loads方法的parse_float参数
    # parse_float参数是可选的，它如果被指定的话，在解码json字符串的时候，符合float类型的字符串将被转为你所指定的，比如说你可以指定为decimal.Decimal
    print("-" * 30 + "> test parse_float <" + "-" * 30)
    p = json.loads("123.456", parse_float=decimal.Decimal)
    print(
        "json.loads 通过parse_float参数将原本应该转为float类型的字符串转为decimal类型: type(json.loads(\"123.456\", parse_float=decimal.Decimal)) --> " + str(
            type(p)))
    print("")

    # 测试json.loads方法的parse_int参数
    # parse_int参数是可选的，它如果被指定的话，在解码json字符串的时候，符合int类型的字符串将被转为你所指定的，比如说你可以指定为float
    print("-" * 30 + "> test parse_int <" + "-" * 30)
    p = json.loads("123", parse_int=float)
    print(
        "json.loads 通过parse_int参数将原本应该转为int类型的字符串转为float类型: type(json.loads(\"123\", parse_int=float)) --> " + str(
            type(p)))

    # parse_constant参数是可选的，它如果被指定的话，在解码json字符串的时候，如果出现以以下字符串:-Infinity，Infinity，NaN那么指定的parse_constant方法将会被调用到
    def transform(s):
        """
        此方法作为参数传给json.load(s)方法的parse_转译NAN, -Infinity,Infinity
        :param s:
        :return:
        """
        # NaN --> not a number
        if "NaN" == s:
            return "Not a Number"
        # 将负无穷大转为一个非常小的数
        elif "-Infinity" == s:
            return -999999
        # 将正无穷大转为一个非常大的数
        elif "Infinity" == s:
            return 999999
        else:
            return s

    # 测试json.loads方法的parse_constant参数
    print("-" * 30 + "> test parse_constant <" + "-" * 30)
    print("json.loads Infinity: --> " + str(json.loads('Infinity')))
    print("json.loads parse_constant convert Infinity: --> " + str(
        json.loads('Infinity', parse_constant=transform)))

    print("json.loads -Infinity: --> " + str(json.loads('-Infinity')))
    print("json.loads parse_constant convert -Infinity: --> " + str(
        json.loads('-Infinity', parse_constant=transform)))

    print("json.loads NaN: --> " + str(json.loads('NaN')))
    print("json.loads parse_constant convert NaN : --> " + str(json.loads('NaN', parse_constant=transform)))
    print("")

    # cls
    # 过官方文档的注释我们可以知道json.load(s)方法具体的实现是通过JSONCoder类实现的，而cls参数是用于自定义一个JSONCoder的子类，用于替换JSONCoder类，,通过这个功能你可以自定义上面的那些parse_xxx参数，
