# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
"""
跳转语句：
    break 跳出整个循环结构
    continue: 跳过本次循环后面的语句不执行，继续下一次循环
"""
for i in range(1, 31):
    if i % 3 == 0 and i % 4 == 0:
        # break
        continue
    print('-' * 15, i)
    i += 1