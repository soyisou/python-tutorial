"""
21.1 三目运算符

三目运算符：np.where()
三目满足 condition,则为 x, 不满足 condition,则为 y
"""
import numpy as np

score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 如果数值小于80，替换为0；如果数值大于80，则替换为90
re_score = np.where(score < 80, 0, 90)
print(re_score)