import pytest
import allure
import os

class Test_demo02():
    #每个测试函数执行前，仅执行一次
    def setup_class(self):
        print('setup')

    # 每个测试函数执行后，仅执行一次
    def teardown_class(self):
        print('teardown')

    @allure.title('用例case01')
    def test_case01(self):
        print('case01')

    @allure.title('用例case02')
    def test_case02(self):
        print('case02')

if __name__ == '__main__':
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(["-s","-v","test_demo02.py",'--alluredir', './temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./temp -o ./report --clean')