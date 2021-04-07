import pytest

class Test_abc():
    #每个测试函数前都执行一次
    def setup(self):
        print('setup')

    # 每个测试函数后都执行一次
    def teardown(self):
        print('teardown')

    def test_a(self):
        print('a')

    def test_b(self):
        print('b')

if __name__ == '__main__':
    pytest.main([])