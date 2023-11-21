# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
文件写操作
    。可以模拟用户注册
    。只要是写操作，如果没有此文件则默认会创建该文件
    。方法：
        。write(s)
        。writelines(list)   ---> 其实没有换行功能！ 需要我们在列表汇总，手动添加  \n
'''
# 之前的方式需要三个步骤，每次都得关闭流，否则就会占用资源，比较麻烦，有没有更好的方式？  用 with

# 对于流操作，我们更多地是使用该格式，比较方便
with open(r'D:\python\lesson-online\05 模块和文件\a.txt', 'r', encoding='utf-8') as rstream:  # 节省了关闭操作
    all = rstream.read()
    print(all)
    # 不用关闭了，系统会默认调用close()操作

print('=================')
# 思考：能够往文件里写呢？   当然可以啦
with open('user.txt', 'w', encoding='utf-8') as wstream:  # 如无该文件，则会自动创建该文件
    '''
    'w'       open for writing, truncating the file first
    怎么理解：truncating ?   可以理解为：将要写的文件内容清空，然后文件光标指向第一个位置！
    可以测试一下，见测试1：
    '''
    # 判断文件是否可读
    flag = wstream.writable()
    if flag:
        wstream.write('明天就是周末啦···')  # 即便是多次执行，也是只有一遍：明天···，因为咱的是写操作
        # 可以测试一下： --- 测试1  --- 执行结果：文件内容为‘明天’
        # wstream.write('明天')  # 即便是多次执行，也是只有一遍：明天···，因为咱的是写操作

        # 思考：是否可以写多行？  可以！ 用 writelines
        wstream.writelines(['hello', 'world', '!'])  # 其实并没有换行效果！

        # 思考：该方法的名字是writelines，那么它是否会写完之后，自动换行呢？   不会哦~ 既没有换行，也没有空格
    # 注意：写完之后，不用我们关闭，系统会自动关闭！
