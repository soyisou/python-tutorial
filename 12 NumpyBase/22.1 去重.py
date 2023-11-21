"""
22.1 去重

np.unique(
参数1：a, 数组：
参数2：return_index=True/False, 新列表元素在旧列表中的位置；
参数3：retun_inverse=True/False, 旧列表元素在新列表中的位置
参数4：return_counts, 元素的数量
参数5: axis=0/1, 0表示行，1表示列
)
"""
# 查找array中的唯一元素
import numpy as np

aa = np.array([1, 2, 3, 4, 5, 5, 6, 6, 6])
bb = np.unique(aa)
print(bb) # [1 2 3 4 5 6]

aa = np.array([[1, ]])

