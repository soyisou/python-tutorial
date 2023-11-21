"""
10 minutes to pandas
"""
import numpy as np
import pandas as pd
# import matplotlib.pypot as plt

# 1. 通过传递一个list对象，来创建一个Series(pandas会默认创建整型索引)
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
"""
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
"""

# 通过创建一个numpy array "时间索引以及列标签来创建一个DataFrame"
dates = pd.date_range('20210101', periods=6)
print(dates)
"""
DatetimeIndex(['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
               '2021-01-05', '2021-01-06'],
              dtype='datetime64[ns]', freq='D')
"""
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
"""
2021-01-01  0.124091  0.855288 -0.202487 -0.729226
2021-01-02 -0.713687 -0.664750  1.610716  1.872655
2021-01-03 -0.129220  0.023797  0.590349  2.607066
2021-01-04 -0.065618 -0.026974  0.423845 -0.982344
2021-01-05  0.401615 -2.402376 -2.121791  0.361678
2021-01-06 -0.093487 -0.127893 -0.098821  1.194148
"""

# 3. 通过传递一个能够被转换成类似序列结构的字典对象，来创建一个DataFrame
df2 = pd.DataFrame({
    'A': 1,
    'B': pd.Timestamp('20220101'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'foo'
})
print(df2)
"""
   A          B    C  D      E    F
0  1 2022-01-01  1.0  3   test  foo
1  1 2022-01-01  1.0  3  train  foo
2  1 2022-01-01  1.0  3   test  foo
3  1 2022-01-01  1.0  3  train  foo
"""

# 4. 查看不同列的数据类型
print(df2.dtypes)
"""
A             int64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
"""