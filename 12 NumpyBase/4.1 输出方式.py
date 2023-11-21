"""
4.1 输出方式
当你打印一个数组，Numpy以类似嵌套列表的形式显示它，但是呈现一下布局：
1. 最后的轴从左往右打印
2. 次后的轴从顶向下打印
3. 剩下的轴从顶向下打印，每个切片通过一个空行与下一个隔开

一维数组被打印成行，二维数组成矩阵，三维数组成矩阵列表
"""
# 一维数组
import numpy as np
a = np.arange(12)
print(a)

# 二维数组
b = np.arange(12).reshape(3, 4)
print(b)

# 三维数组
c = np.arange(24).reshape(2, 3, 4)
print(c)

# 四维数组
d = np.arange(16).reshape(2, 2, 2, 2)
print(d)

"""
打印省略
"""
# 一维数组
aa = np.arange(10000)
print(aa)

# 二维数组
bb = np.arange(10000).reshape(100, 100)
print(bb)