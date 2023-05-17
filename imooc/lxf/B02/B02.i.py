# -- coding:utf-8 --
import time
def record_request(data_param):
    def func_outer(func):
        def func_inner(*args, **kwargs):
            print("装饰器带的参数:"+ data_param)
            print("被装饰函数名称："+func.__name__+"( );参数：", args[0])
            print('调用函数的时间为： ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            start = time.time()
            print("--函数运行开始时间：{} --".format(start))
            func(*args, **kwargs)
            end = time.time()
            print("--函数运行结束时间：{} --".format(end))
            print("-函数运营了：{}:秒---".format(end-start))
        return func_inner
    return func_outer
data = {"name": "张三", "age": 23}
@record_request("DEBUG")
def test(res):
    time.sleep(2)
    print("函数测试执行内容。。。。",(data))
test(data)
