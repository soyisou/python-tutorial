# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
Selenium测试直接运行在浏览器中，就像真正的用户在操作一样

驱动安装地址
    https://npm.taobao.org/mirrors/chromedriver/
    chrome 对应版本号  95
    chromedriver 对应版本号 要是95版本


    pip install selenium  安装

通过代码进行浏览器搜索
    1. 创建浏览器对象
        。设置执行路径
        。设置可选项参数，比如浏览器是否显现
    2. 确定目标搜索地址
    3. 确定搜索框并将搜索内容送入搜索框
    4. 确定搜索点击按钮，并按确认
'''
from selenium import webdriver
import requests
import time

# 重建谷歌浏览器对象
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='D:/学习/综合实践/老师课程/chromedriver_win32/chromedriver.exe')

# 搜索地址
url = 'https://www.baidu.com/'
driver.get(url)  # 通过浏览器打开搜索页面
kw = driver.find_element(by=By.CSS_SELECTOR, value='#kw')  # 定位搜索框

kw.send_keys('python')  # 将搜索关键字'python'送入搜索框
su = driver.find_element(by=By.CSS_SELECTOR, value='#su')  # 定位搜索按钮
su.click()  # 点击搜索按钮

time.sleep(1)
for i in range(10):
    driver.execute_script('window.scrollBy(0, 1000)')  # 滚屏
    time.sleep(0.5)

# 页面截图
driver.save_screenshot('百度截图.png')

# 获取页面源码
html = driver.page_source
print(html)

# 关闭当前页面
driver.close()
# 关闭整个浏览器
driver.quit()