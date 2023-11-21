# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

"""
语句：
变量 --》 运算符 a >> 1 a + 10 ==> 语句

语句：
条件语句（判断语句）：if .. else
    格式：
        if 条件: （条件结果为 bool类型, 如关系运算符,逻辑运算符,成员,身份）
        else:
            条件不成立执行的代码

    (if 也可以单独用)

    嵌套使用：
    if 条件：
        if 条件：
        else:
    else:
        条件不成立执行的代码
循环语句：
跳转语句：

"""

# 判断年龄
age = int(input("输入年龄："))
if age > 18:
    print("哈哈，成年啦！")
    print("哈哈，我进网吧了！开始玩游戏！")
    game = input("请输入游戏名称：")
    if game == '连连看':
        print("回家玩去吧！")
    else:
        print("很喜欢玩:%s" % game)  # 字符串格式的方式
else:
    print("呜呜呜,怎么还不长大!")
"""
%s (str) 字符串的占位符，如果值是一个整数，默认会将整型: str(year)
%d (digit) 专门给整型占位的
%f (float) 给浮点型占位，设置小数点后面位数：%.nf（n 表示的是位数）
"""