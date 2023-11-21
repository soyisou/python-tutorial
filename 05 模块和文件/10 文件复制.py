# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

# 文件上传的时候尽量保持原名上传，当然也可以在文件名后加随机数字
file_path = r'C:\Users\LJM\Pictures\照片\戴眼镜（处理过）.jpg'  # 原文件目录
with open(file_path, 'rb') as rstream:
    content = rstream.read()
    # 写入
    filename = file_path[file_path.rfind('\\') + 1:]
    with open(filename, 'wb') as wstream:  # 存到当前目录，文件名不变
        wstream.write(content)
print('复制完成！')
