#慕课网 廖雪峰教程 B4.9 例题
def fun():          #定义一个類外的函数
    return "Function"

class Apple:        # 類的三種方法

    def fun1(self): # 1.在類內定義的 普通方法
        return 'normal'

    @staticmethod   # 2.在類內定義的，用@staticmethod裝飾的 靜態方法；相當於類外的函數
    def fun2():
        return 'staticmethod'

    @classmethod    # 3.在類內定義的，用@classmethod裝飾的 類方法；第一參數是 cls，綁定了類，屬於方法。
    def fun3(cls):
        return 'classmethod'

print(fun())
print(Apple.fun1)   # 以類的名義調用三個方法
print(Apple.fun2())
print(Apple.fun3())
print("-"*80)
apple = Apple()     # 定義實例
print(apple.fun1)   # 以實例調用類的方法。返回的是函數的對象。
print(apple.fun2)
print(apple.fun3)
print("-"*80)
print(apple.fun1()) # 真正的以實例調用類的方法，返回的是這個方法的返回值。
print(apple.fun2())
print(apple.fun3())

