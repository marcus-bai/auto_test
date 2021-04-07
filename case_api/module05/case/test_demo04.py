import allure
import pytest
import os


@allure.feature('test_module_01')
def test_case_01():
    """
    用例描述：Test case 01
    """
    assert 0


@allure.feature('test_module_02')
def test_case_02():
    """
    用例描述：Test case 02
    """
    assert 0 == 0


if __name__ =="__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['test_demo04.py','--alluredir', './temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./temp -o ./report --clean')
