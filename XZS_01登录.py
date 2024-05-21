import unittest
from parameterized import parameterized
import requests
from 第十一周作业.XZS.HTMLTestRunner import HTMLTestRunner

def readFile():
    f = open('../txt/01登录.txt', mode='r', encoding='utf-8')
    datas = f.readlines()
    r = [tuple(i.split(',')) for i in datas]
    return r

class XZS_denglu(unittest.TestCase):
    # 使用@parameterized装饰器对测试方法进行参数化
    @parameterized.expand((readFile))
    def test_login01(self,userName,password,remember,code):
        session = requests.Session()  # 创建一个会话对象
        a = {
            "userName": userName,
            "password": password,
            "remember": remember
        }
        print(a)
        # 发送POST请求进行登录操作
        rep2 = session.post("http://localhost:8000/api/user/login", json=a)
        self.assertEqual(200, rep2.status_code)  # 断言响应状态码为200
        self.assertEqual(int(code), rep2.json()['code'])
        # 搜索所有

        session.close()


