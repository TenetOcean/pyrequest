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
        """用户名为空"""
        payload = dict(UserType=1,UserName=None,PassWord='123123',pwd='',UserCode='dfdsg2165498jdofdfd')
        r = requests.post(self.base_url,data=payload)
        result = r.text.split("'")
        assert "系统错误" in result[3]

if __name__ == '__main__':
    pytest.main()
