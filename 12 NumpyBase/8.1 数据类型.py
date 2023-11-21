"""
8.1 数据类型
在创建数组时，也可以使用dtype来显示指定数组中的类型（通过numpy提供的类型来指定）
如果没有指定，则会根据元素类型进行推断
如果元素的类型不同，则会选择一种兼容的类型
"""
import numpy as np

# 如果该没有指定元素类型，则会根据现有的元素，自动推断元素类型
x = np.array([1, 2, 3., "abc"])
print(x.dtype) # <U32

# 注意：不同的数据顺序，可能会影响到最终的数组类型
y = np.array(["abc", 1, 2, 3.])
print(y.dtype) # <U32

"""
在数据存储上，有两种形式：
1. 高维优先
2. 低维优先
"""
# 我们在创建数组时，可以使用dtype参数显式地指定数组的类型
w = np.array([1, 2, 3], dtype=np.float32)
print(w.dtype) # float32

"""
类型的转换
我们可以通过数组对象的 astype 函数来进行类型转换
"""
# 思考：是否可以直接修改dtype属性，进行类型的转换？ 可以(自答)

x = np.array([1.5, 2.3, 3.4, -1.2, -1.8, -1.5])
print(x.dtype) # float64

x = np.array([1.5, 2.3, 3.4, -1.2, -1.8, -1.5], dtype=np.int32)
print(x.dtype) # int32

# 进行类型转换
y = x.astype(np.int64)
print(y.dtype) # int64
