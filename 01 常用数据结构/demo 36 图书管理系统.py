# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
综合练习:
    图书管理系统：
        1. 借书
        2. 还书
        3. 查询书籍
        4. 显示所有书籍
        5. 退出系统

    存储数据：
        1. 姓名
        2. 所借书籍
        ···

编程建议：
    1. 写代码，先搭架构
    2. 先易后难，各个击破

'''
import time

print('=' * 50)
print('--------------欢迎来到深大图书馆------------------')
print('=' * 50)

# 图书馆的书籍定义
books = [['防脱发指南', 5], ['颈椎康复指南', 6], ['活着', 4], ['追妹攻略', 4]]

# 学生借书容器
students_books = []  # ['姓名', {'', ''}]

while True:  # 哪里最简单，就从哪里开始填充
    choice = input('请选择功能：1. 查询 2. 借书 3. 还书 4. 查询所有书籍 5. 查看借阅情况 6. 退出系统')
    if choice == '1':
        # 查询书籍
        print('--------------查询书籍------------------')
        search_book = input('请输入要查询书籍的名称：')
        # 遍历 books
        for book in books:
            if search_book in book:
                print('书籍名称：{}  剩余数量：{}'.format(book[0], book[1]))
                break
        else:
            print('本图书馆不存在此书！')

    elif choice == '2':
        # 借书
        print('--------------借阅书籍------------------')
        username = input('请输入用户名:')

        flag = True
        while flag:
            book_name = input('请输入书名：')
            # 查书
            for book in books:
                if book_name in book:
                    print('书籍名称：{}  剩余数量：{}'.format(book[0], book[1]))
                    # 判断可借数量
                    if book[1] > 0:
                        # 可以借书
                        for stubooks in students_books:
                            if username in stubooks:
                                # 说明用户借过书
                                if book_name in stubooks[1]:
                                    print('您已借过此书，不能再借！')
                                else:
                                    stubooks[1].add(book_name)
                                    # 减少该书数量
                                    book[1] -= 1
                                    print('正在借书中，请稍等···')
                                    time.sleep(1)
                                    print('{}借书成功！'.format(book_name))
                                    flag = False
                                # 退出
                                break
                        else:
                            # 此人从来没有在图书馆借书
                            # 构建结构：['人名', {'', ''}]
                            sbooks = set()
                            sbooks.add(book_name)
                            sbooks_list = [username, sbooks]
                            # 将其添加到student_books
                            students_books.append(sbooks_list)
                            book[1] -= 1
                            print('正在借书中，请稍等···')
                            time.sleep(1)
                            print('{}借书成功！'.format(book_name))

                        flag = False
                    break
            else:
                print('本图书馆不存在此书！请重新输入书名：')

    elif choice == '3':
        # 还书
        print('--------------退还书籍------------------')
        username = input('请输入用户名:')
        book_name = input('请输入要还的书籍名称：')
        # 开始遍历
        for stubooks in students_books:  # ['姓名', {'', ''}]
            if username in stubooks:
                # 说明此人借过书
                if book_name in stubooks[1]:
                    # 说明借过此书
                    stubooks[1].remove(book_name)
                    # 修改数量
                    for book in books:
                        if book_name in book:
                            book[1] += 1
                            break
                    print('正在还书中，请稍等···')
                    time.sleep(1)
                    print('{}还书成功！'.format(book_name))
                else:  # 未借过此书
                    print('没有借过此书！')

                # 退出
                break

            else:
                print('查无此用户, {}暂未借过书！'.format(username))

    elif choice == '4':
        # 显示所有书籍
        print('--------------深大图书馆所有书籍如下------------------')
        print('书名：\t\t\t\t数量')
        for book, num in books:
            print('{}\t\t\t\t{}'.format(book, num))

    elif choice == '5':
        # 查看用户借书情况
        print('--------------个人所借书籍----------------')
        username = input('请输入用户名:')
        # 开始遍历
        for stubooks in students_books:  # ['姓名', {'', ''}]
            if username in stubooks:
                # 说明此人借过书
                for book in stubooks[1]:
                    print('用户姓名：{}\t\t所借书籍：{}'.format(username, book))

            else:
                print('查无此用户, {}暂未借过书！'.format(username))

    elif choice == '6':
        # 退出系统
        ans = print('确定要退出图书管理系统吗？(yes/no)')
        if ans.lower() == 'yes':
            print('即将退出系统，请稍等···')
            time.sleep(1)
            print('系统关闭，欢迎下次使用！')
            break

    else:
        print('输入错误，请重新输入：')