# 导入第三方库，并且为其起一个别名
import numpy as np

# numpy 版本
print(np.__version__)

# In 和 Out 都是IPython的特殊对象，用来存储我们输入与输出的值
# In 是列表类型，Out 是字典类型

# 如果不使用python输出，而是作为表达式计算值显示时，我们只能看到最后一个结果

# 忽略警告信息
import warnings
warnings.filterwarnings("ignore")

# 调用np的arange函数生成一个数据序列：从0-9
data = np.arange(0, 9)
print(data)
# print(type(data)) # <class 'numpy.ndarray'>

# 思考：如何对数据序列(0-9)的每个元素都进行加1操作？

list1 = list(range(10))
print(list1)
# print(type(list1)) # <class 'list'>

# 方法一：使用 list
res = []
for i in list1:
    res.append(i + 1)
print(res)

# 方法二：使用 numpy
data = np.arange(10)
# print(data)
data += 1
print(data)

# 使data中的每个元素都 * 2
data *= 2
print(data)

# 目的：深刻地认识到使用numpy来进行数据计算，要比使用原生的python要简单的多！



