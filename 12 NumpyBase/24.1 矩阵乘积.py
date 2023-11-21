"""
24.1 矩阵乘积

(M行，N列)*(N行，M列) = (M行，Z列)
"""
import numpy as np

st_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 平时成绩占40%， 期末成绩占60%， 计算结果
q = np.array([[0.4], [0.6]])
# q = np.array([0.4, 0.6])
result = np.dot(st_score, q)
print(result)