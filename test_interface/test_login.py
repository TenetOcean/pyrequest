import sys
import requests
import pytest
from os.path import dirname,abspath

sys.path.insert(0,dirname(dirname(abspath(__file__))))

class TestLgoinInterface:
    

    def setup(self):
        self.base_url = "http://192.168.9.50:8100/Login/Validation"

    def teardown(self):
        print('end')

    def test_user_name_none(self):
        """用户名为None"""
        payload = dict(UserType=1,UserName=None,PassWord='123123',pwd='',UserCode='dfdsg2165498jdofdfd')
        r = requests.post(self.base_url,data=payload)
        result = r.text.split("'")
        assert "系统错误" in result[3]

    def test_user_name_empty(self):
        """用户名为空"""
        payload = dict(UserType=1,UserName=" ",PassWord='123123',pwd='',UserCode='dfdsg2165498jdofdfd')
        r = requests.post(self.base_url,data=payload)
        result = r.text.split("'")
        assert "用户名或密码不正确！" in result[3]

    def test_user_password_none(self):
        """登录密码为None"""
        payload = dict(UserType=1,UserName="02899999",PassWord=None,pwd='',UserCode='dfdsg2165498jdofdfd')
        r = requests.post(self.base_url,data=payload)
        result = r.text.split("'")
        assert "系统错误" in result[3]

    def test_user_password_empty(self):
        """登录密码为空"""
        payload = dict(UserType=1,UserName="02899999",PassWord=" ",pwd='',UserCode='dfdsg2165498jdofdfd')
        r = requests.post(self.base_url,data=payload)
        result = r.text.split("'")
        assert "用户名或密码不正确！" in result[3]

    def test_user_name_and_password_is_right(self):
        """用户名和密码正确"""
        payload = dict(UserType=1,UserName="02899999",PassWord="123123",pwd='',UserCode='dfdsg2165498jdofdfd')
        r = requests.post(self.base_url,data=payload)
        assert r.status_code == 100

if __name__ == '__main__':
    pytest.main()