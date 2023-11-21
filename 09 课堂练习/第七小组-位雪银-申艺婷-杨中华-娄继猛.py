"""
做题须知：
    1、注意题意进行作答
    2、题中注意调用类、函数时括号问题
    3、选择题中注意字符中的坑
    4、名词解释给出重点即可得分
    5、小组可讨论
    6、截止当天11:00前发送邮件  343105980@qq.com   备注: 第几小组-xxx-xxx-xxx

    7、示例：
        1、以下正确的字符串是(ABCD )
            A   'abc"ab"
            B   'abc"ab'
            C   "abc"ab"
            D   "abc\"ab"



第一大题不定项选择(每题 3分)：


    1、以下正确的字符串是( BD )
        A   'abc"ab"
        B   'abc"ab'
        C   "abc"ab"
        D   "abc\"ab"


    2、"ab"+"c"*2 结果是( C )
        A: abc2
        B: abcabc
        C: abcc
        D: ababcc


    3、以下函数返回的值是( D )
        def myfun():
            pass
            return
        A: 0
        B: 出错不能运行
        C: 空字符串
        D: None


    4、函数如下 ( ABC )
        def showNumber(numbers)：
            for n in numbers:
                print(n)

        下面哪些在调用函数时会报错
        A: showNumer([2,4,5])
        B: showNnumber('abcesf')
        C: showNnumber(3.4)
        D: showNumber((12,4,5))



    5、定义类如下( C )
        class Hello():
            def __init__(self,name):
                self.name = name
            def showInfo(self):
                print(self.name)

        下面代码能正常执行的是哪些
        A: h = Hello
           h.showInfo()
        B: h = Hello()
           h.showInfo('张三')
        C: h = Hello('张三')
           h.showInfo()
        D: h = Hello('admin')
           h.showInfo


    6、以下哪些python能正常启动( D )
        A: 拼写错误
        B: 错误表达式
        C: 缩进错误
        D: 手动抛出异常

    7、有关异常说法正确的是( B )
        A: 程序中抛出异常终止程序
        B: 程序中抛出异常不一定终止程序
        C: 拼写错误会导致程序终止
        D: 缩进错误会导致程序终止


    8、下列叙述错误的( B )
        A: append方法是添加到列表最后
        B: append可同时添加多个元素
        C: insert可在任意位置对列表进行添加
        D: 拼接方法只能拼接相同类型


    9、下列程序说法输出打印正确的是( D )
        list1 = [1,2,3,4,5]
        for i in list1:
            if i >= 3:
                continue
            print(i)
        A: 1,2,3,4,5
        B: 1,2,3,4
        C: 1,2,3
        D: 1,2


    10、下列程序 输出a,b结果正确的是( 无正确答案 )
        a = 1
        b = 2
        if a*10 <=10 and b*2 >3:
            a+=1
            b-=3
            if a<15 or b>5:
                a*=5
                b+=a
        else:
            b+=1
            a*=b
            if a<=b or b<10:
                a*=10
                b+=a
        print(a, b)

        A: 55,56
        B: 33,34
        C: 54,55
        D: 61:50


第二大题 解释
    1、什么是动态数据、静态数据？
        答：
          静态数据:
          一些永久性的数据，一般存储在硬盘中。硬盘的存储空间一般都比较大，现在普通计算机的硬盘都有500G左右，因此硬盘中可以存放一些比较大的文件。
          计算机关闭之后再开启，这些数据依旧还在，只要不主动删除或者硬盘没坏，这些数据永远都在。
          静态数据一般是以文件的形式存储在硬盘上，比如：文档，照片，视频。

          动态数据:
          动态数据指在程序运行过程中，动态产生的临时数据，一般存储在内存中，内存的存储空间一般都比较小，现在普通计算机的内存只有8G左右，
          因此要谨慎使用内存，不要占用太多的内存空间。
          计算机关闭之后，这些临时数据就会被清除。
          当运行某个程序（软件）时，整个程序就会被加载到内存中，在程序运行过程中，会产生各种各样的临时数据，这些临时数据都是存储在内存中的。
          当程序停止运行或者计算机被强制关闭时，这个程序产生的多有的临时数据都会被清除。

    2、什么是类、对象、实例化
        答：
          类：客观世界中的许多对象，无论其属性还是其行为(方法)常常有许多共同性，抽象出这些对象的共同性便可以构成类。
          所以，类是对象的抽象和归纳，对象是类的实例。有相同特征的事物的集合。

          对象是对事物的抽象，而类是对对象的抽象和归纳。
          对象被称作类的一个实例，而类是对象的模板。

          实例化是类的具象，先定义类才能实例化，实例化需要引用类的名称。

    3、请列出课程案例-爬取北京新发地的操作步骤，越详细越好
        答：
        1. 明确爬取目标，列出爬取步骤
        2. 目标细分，按功能将目标细分为几个具体的函数，如：爬取函数，保存函数等，将各个函数封装成类
        2. 进入北京新发地网页
        3. 根据信息判断该信息是在静态网页还是动态网页，即是静态数据还是动态数据
        4. 接口分析，确定接口 url，方法分析，确定是 get 还是 post---> 该案例是 post， 需要提交 data
        4. 导入相应的包，如 import requests
        5. 获取目标的 URL
        6. 配置 headers --> 可按 F12 从网页获取
        7. 利用 post 函数获取相应信息
        8. 对信息进行处理
        9. 选取信息的保存格式，保存信息

    4、请列出课程案例-英雄联盟爬取所有皮肤图片操作步骤，越详细越好
        答：
        1.查找爬取皮肤所需要的URL；
        2.分析查找接口，查找我们所需要的信息，如：User-Agent
        3.进入接口，再次查找爬取皮肤所需要用到的信息；如：英雄序号，皮肤图片
        4.代码编写：
            1.导入所需要的包，并全局定义URL，Headers
            2.定义英雄序号获取函数，同样我们也需要通过requests方法获取URL链接中英雄序号的信息；
            3.定义CSV文件保存函数，并在CSV文件表头提前写入英雄名称，皮肤名称，皮肤链接等信息，便于后期信息的保存；
            4.定义皮肤图片下载函数，通过requests方法获取URL链接中英雄皮肤图片的信息；
            5.定义获取皮肤函数，通过requests函数获取url链接信息，在链接中找到皮肤链接，英雄名称，皮肤名称等信息，
            6.调用获取英雄皮肤的主函数，在函数中分别调用获取英雄序号函数，CSV文件保存函数，获取皮肤图片函数，即可成功爬取
                英雄的各种皮肤，并且成功保存早CSV文件中，并且把图片成功下载。

"""

"""
第三大题 编程

    1、写出删除字符串 'this is a desk'中重复的两个单词，使字符串变成
        'this a desk'，方法自定义，不可直接print
        提示： 可使用字符串范围提取替换、split切割、字符串拼接等

        string_1 = 'this is a desk'
        string_2 = string_1.split(' ')
        print(string_2)
        del string_2[1]
        count = 0
        string_3 = ''
        while count<3:
            string_3 = string_3+string_2[count]+' '
            count+=1
        print(string_3)

    2、  s = ' 123.33sdhf3424fdg323.324z10', 计算字符串中所有数字的和
        如 提取数字：  123.33 + 3424 + 323.324 + 10
        提示：范围提取，多提取几次，转换类型进行相加求和

        def sum(s):
            str = ''
            s = s.strip()
            for i in s:
                if '0' <= i <= '9' or i == '.':
                    str += i
                else :
                    str += ' '

            ls = str
            ls = ls.split(' ')

            sum = 0.0
            for i in ls:
                if i != '':
                    sum += float(i)

            print(sum)

        s = ' 123.33sdhf3424fdg323.324z10'
        sum(s)
"""

"""
    3、有如下代码，写出调用的顺序 以及打印结果
        def f1():
            print('funcname is f1')
        def f2():
            print('funcname is f2')
            return 1
        def f3(func1):
            l1 = func1()
            print('funcname is f3')
            return l1
        print(f3(f2))

        答：1. 调用顺序： f3-->f2
            2. 打印结果：
                funcname is f2
                funcname is f3
                1

爬取网址： https://jiameng.baidu.com/list?category=20907

要求：
    1、爬取当前页面 商铺名称
    2、爬取第二页商铺名称
提示：
    以动态数据爬取方式获取

import requests
import csv
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
}


file = open('shop.csv', 'a', encoding='utf-8', newline='')
file_csv = csv.writer(file)
file_csv.writerow(['商铺名称'])

def spiders(pageId):
    url = 'https://jiameng.baidu.com/portal/search?ajax=1&accessid=1488935512D0&device=pc&strategy=list&from=jmx&pageSize=20&page={}&category=20907'.format(
        pageId)
    res = requests.get(url = url,headers = headers)
    data = res.json()
    dic1 = data['data']
    ls1 = dic1['list']
    for i in range(len(ls1)):
        print(ls1[i]['name'])
        file_csv.writerow([ls1[i]['name']])

for i in range(1,3):
    spiders(i)

"""