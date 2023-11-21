# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
数组切分
    。indice: 标记，代数中的下角标
'''

import numpy as np

a1 = np.random.randint(1, 100, size=(6, 6))
print(a1)

print('=' * 50)

# indices_or_sections 将数组分为几份，如果设置的是一个数据，那就表示均分
a2 = np.split(a1, indices_or_sections=3, axis=1)  # 默认行进行切割，均分成了3份
print(a2)

print('=' * 50)

# 思考：如果遇到不能等分的情况，我们该如何去做？  自定义分组情况！
# indices_or_sections=[第一刀下标，第二刀下标，···]  根据刀的下标进行切片22221
a3 = np.split(a1, indices_or_sections=[2, 3], axis=1)  # 切列
print(a3)

print('=' * 50)

a4 = np.split(a1, indices_or_sections=[2, 3], axis=0)  # 切行
print(a4)

