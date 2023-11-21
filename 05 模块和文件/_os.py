# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
import os
    。mkdir()
    。rmdir()  # 只能删除空文件夹，非空文件夹不能删除 OSError: [WinError 145] 目录不是空的。
    。思考：如何删除非文件夹？
        。方法一：
            。先采用递归方式，删除里面的文件及文件夹
            。最后再采用 rmdir()删除外面的文件夹
        。方法二
            。import shutil
            。shutil.rmtree(path)  # 直接删除非空文件夹
    。os.listdir(path)  # 查看path下的内容, 并以列表的形式返回
    。os.getcwd()  # 获取当前文件的路径（绝对路径）
    。os.getpid()   # get process id  获取当前的进程号
    。os.getppid()  # get parent process id 获取父进程的 id
'''
import os
# print(os.name)  # nt
# os.mkdir('张三')
# os.remove('张三')
# os.removedirs('张三')  # 删除目录  os. removedirs ( name )
# os.rmdir('./张三')  # Remove a directory.  os. rmdir ( path, *, dir_fd=None )
# os.rmdir(r'C:\Users\LJM\Desktop\杨中华照片')  # Remove a directory.  os. rmdir ( path, *, dir_fd=None )
# os.removedirs(r'C:\Users\LJM\Desktop\杨中华照片')  # OSError: [WinError 145] 目录不是空的。

# 思考：rmdir()和removedirs()都不能直接删除非空文件夹，有没有可以直接删除非空文件夹的函数呢？ 有
import shutil
# shutil.rmtree(r'C:\Users\LJM\Desktop\杨中华照片')  # 直接删除非空文件夹！

# 只能看到文件夹，但是不能没有层次效果 --- 浏览当前路径下的所有的内容[文件或者文件夹], 并以列表的形式返回
# files = os.listdir('../05 模块和文件')
# for file in files:  # 不能看到带有层侧的内容
#     print(file)

# print(os.getcwd())  # 返回当前文件所在的绝对路径    D:\python\lesson-online\05 模块和文件

# 分别获取进程号和父进程号
# print(os.getpid())  # 1812
# print(os.getppid())  # 13376

os.chdir('../04 异常')  # 切换目录  chdir --> change directory
files = os.listdir(os.getcwd())  # os.getcwd()表示获取当前文件的绝对路径
for file in files:  # 不能看到带有层侧的内容
    print(file)