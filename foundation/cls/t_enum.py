from enum import Enum, unique


# 添加 unique 装饰器
# 可以借助 @unique 装饰器，这样当枚举类中出现相同值的成员时，程序会报 ValueError 错误。
@unique
class Color(Enum):
    # 为序列值指定value值
    # 枚举类中各个成员必须保证 name 互不相同，但 value 可以相同，
    red = 1
    green = 2
    blue = 3


# 还可以使用 Enum() 函数创建枚举类
# Enum() 函数可接受 2 个参数，第一个用于指定枚举类的类名，第二个参数用于指定枚举类中的多个成员。
Color1 = Enum("Color", ('red', 'green', 'blue'))

# 调用枚举成员的 3 种方式
print(Color.red)
print(Color['red'])
print(Color(1))

# 调取枚举成员中的 value 和 name
print(Color.red.value)
print(Color.red.name)

# 遍历枚举类中所有成员的 2 种方式
for color in Color:
    print(color)

# 枚举类成员之间不能比较大小，但可以用 == 或者 is 进行比较是否相等，例如：
print(Color.red == Color.green)
print(Color.red.name is Color.green.name)

Color.red = 4  # 枚举类中各个成员的值，不能在类的外部做任何修改，也就是说，下面语法的做法是错误的

# 枚举类还提供了一个 __members__ 属性，该属性是一个包含枚举类中所有成员的字典，通过遍历该属性，也可以访问枚举类中的各个成员。
for name, member in Color.__members__.items():
    print(name, "->", member)
