"""
3.2 其他创建数组的方式：函数和文件
fromfunction
frombuffer
fromfile
fromiter
"""

"""
np.fromfunction() # 使用比较少
"""
import numpy as np
# 定义一个函数
def f(x, y):
    return x * 10 + y

# 从一个函数生成一个二维数组
b = np.fromfunction(f, (4, 5), dtype=np.int32)
print(b)

"""
np.frombuffer() 用于实现动态数组。
numpy.frombuffer() 接收buffer输入参数，以流的形式读入转化成 ndarray 对象。
第一参数为流（stream）
第二参数为返回值的数据类型
第三参数指定读取多少个
第四参数指定从stream的第几位开始读入
data 为字符串的时候，python3默认str是unicode类型，所以要转成bytestring（在原str前加b）
"""

data = b"hello world"
a = np.frombuffer(data, dtype='S1', count=3, offset=6)
print(a)

"""
np.fromiter() 从可迭代对象中建立ndarray对象，返回一维数组
看起来有点像 numpy.array, array方法需要传入的是一个list，而fromiter可以传入可迭代对象
"""
myiter = (x * x for x in range(10))
a = np.fromiter(myiter, dtype=np.int32) # 传入list也可以
print(a)
