# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

# 单行注释
# 打印 5 个单引号
# print("*****")

# 多行注释 ''' '''
'''
多行注释 —— 单引号
1. 变量
2. 变量的声明
3. 变量的类型
4. 变量的使用
5. 操作符的使用
'''

"""
多行注释 —— 双引号
1. 变量: int a = 10; String name;
        弱类型： 名 = 值，如：number = 10 具体什么类型，取决于你给它的值是什么类型
        判断变量的类型：type(变量名)
2. 变量的声明：格式：变量名 = 值
             变量的命名规则：
             A. 字母、数字、下划线
             B. 不能数字开头
             C. 不能使用关键字
             D. 区分大小写
             E. 见名知义：尽量使用英文
                驼峰式命名法  如：showName 第一个单词首字母小写，以后每个单词首字母大写
                            若是类，则每个单词的首字母都大写 如：Student
                下划线命名(推荐) 如：show_name,borrow_book
3. 变量的类型
4. 变量的使用
5. 操作符的使用
"""

# 解释器遇到注释就会跳过，不会执行

number = 10
print(number)
print(type(number))
name = '张三'

# ctrl + 左键 查看 print 函数详情
# print(number,name,end = ' ')

# print() # 打印空行

number = '1'
print(number)
print(type(number))

# 查看关键字
import  keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
'''
关键字
from,       import,     as
class,      def   ,     return
pass ,      while ,     for
if   ,      else  ,     elif         
in   ,      break ,     continue     

and ,       or,         not
True,       False ,     None
del ,       in,         is  
global,     nonlocal,   yield,      
try ,       except,     finally

raise,      async,      assert
await,      lambda 

'''

"""
# 即不要用一些常用的系统函数作为变量的命名
print = 6 # 可以定义
print(print) # 报错 系统先检索用户代码，再检索系统代码

"""
str1 = 'I love you'
list1 = str1.split(' ')
list1 = list1[-1::-1]
print(list1) # 列表类型

print(' '.join(list1))  # you love I

