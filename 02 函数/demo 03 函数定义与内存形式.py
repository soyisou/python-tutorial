# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
函数：   --- 函数本身也是一个对象， 函数是存在某个地址空间的 (可以认为是一种特殊的变量， 函数变量)
    目的：减少代码的冗余，使一些重复的代码，定义在函数当中
    场景：
    格式：
        。def 函数名 ([形参, ···])
            函数体

        。函数的命名方式，同变量名
    调用：
        。函数名([实参,···])


'''
books = ['红楼梦', '西游记', '还珠格格', '新白娘子传奇']

# 定义函数
def show_books(books):
    print('图书馆的书籍如下：')
    for book in books:
        print(book)

# 调用函数
show_books(books)
print(show_books(books))  # None

