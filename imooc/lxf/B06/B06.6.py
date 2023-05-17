#慕课网 廖雪峰教程 B06.5 例题  __add__( )方法
class Model:
    def __init__(self,x):                   # 定义构造方法
        self.x=x
        print('调用构造方法')

    def __add__(self, other):               # 定义 __add__( ) 方法，二个参数是加数
        print('调用add()',self.x,'+',other.x)
        return  Model(self.x+other.x)       # 返回二参数相加之和。
    def __str__(self):                      # 定义转换成字符串方法 __str__( ) 。
        print('调用__str__()')
        return ("两个对象相加的值是：{x}".format(x=self.x))   # 返回格式化字符串

a=Model(5)      # 实例化对象
b=Model(7)      # 实例化对象
print('-'*80)
print(a+b)      # 二个实例对象相加，会自动调用类中的 __add__( )，然后打印输出。






