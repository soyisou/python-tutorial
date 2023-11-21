'''
字典的获取：
    获取都是根据 key得到 value：
    方式1：
        dict1[key] ---> value, 如果 key 不存在的话则报错 KeyError
    方式2：
        dict1.get(key, default)  --> value, 如果 key不存在的话，没有默认值, 则返回 None
                                        如果 key不存在，设置默认值default, 则返回 default的值
redis: key:value
    set()
    get(key) --> value

字典的增删改查：
    增加与修改的格式是一样的,dict1[key] = value 到底是作增加还是修改取决于字典中是否存在此 key
                                            如果存在则修改，不存在则添加
    删除：
    pop('key')  # 根据 key 删除键值对并将值返回
    popitem()  # 随机删除，从后往前删除键值对，返回值是(key, value)
    clear()  # 清除
    del dict1['key']  # --> 根据 key 删除键值对 类似 pop(key)
    del dict1  # 清空内容并回收内存

    查找：不支持查找

    取值：
    get()   --> 根据键得到值
    keys()  --> 得到所有 key
    values()  --> 得到所有的值 value
    items()  --> 得到所有的键值对，将键值对放到元组，多个元组保存在一个列表中[(), (), ()···]

'''
# 字典
dict1 = {'张三': 20, '李四': 21, '王五': 22}

# 获取都是根据 key 得到 value
print(dict1['张三'])
# print(dict1['赵六'])  # 报错

# 内置方法: get()
value = dict1.get('张三')
print(value)

value = dict1.get('赵六')
print(value)

# 字典是否支持增删改查
# 增加一个键值对
dict2 = {}
dict2['zhangsan'] = 19
print(dict2)

# 修改
dict2['zhangsan'] = 20
print(dict2)

dict2['张寒'] = 21
dict2['wangwu'] = 10
print(dict2)

# 删除：
# dict2.pop('wangwu')  # 删除键值对
# print(result)

# 删除：
result = dict2.pop('wangwu')  # 删除键值对并将其值进行返回
print(result)

result2 = dict2.popitem()  # 删除，并以元组返回键值对
print(result2)

# 查找
# 构建一个新的字典
res = dict.fromkeys(['a', 'b', 'c'])
print(res)

# 构建一个新的字典通过 iteralbe
res = dict.fromkeys(['a', 'b', 'c'], 100)
print(res)

dict3 = {'a': 210, 'b': 230, 'c': 344}
ks = dict3.keys()
print(ks)
print(list(ks))

vs = dict3.values()
print(vs)
print(list(vs))

# 经常用在遍历中
its = dict3.items()  # [('a', 210), ('b', 230), ('c', 344)]
print(its)

for key, value in dict3.items():
    print(key, value)