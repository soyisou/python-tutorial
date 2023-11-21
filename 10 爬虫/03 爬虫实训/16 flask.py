# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
快速建站：
    。搭建网站
    。python
        。Django
        。Flask
    。Flask
        。Server
        。Flask 是一个基于 Python 打造的轻量级框架（微框架）
        。微不代表功能弱
        。代表的是框架不为开发者做更多的选择
        。框架只保持核心模块，其余用的所有模块都是可以自选的
        。安装
            。pip install flask
        。使用
            。创建 flask 的对象
            。使用 flask 对象注册路由
                。@app.route('规则')
                。/
                。/users/
            。路由匹配到，调用下面的函数
            。函数返回 response
            。使用了框架的 static
                。可以直接被外部访问

'''
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/users/')
def users():
    return '用户名 '


if __name__ == '__main__':
    app.run()
8


