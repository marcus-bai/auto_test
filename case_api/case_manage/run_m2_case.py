import unittest


# 设置运行case的模块（路径）
m2path = r'D:\PycharmProjects\auto_test\case_api\module02\case'

# 创建测试套件
suite = unittest.TestSuite()

#创建测试用例集，defaultTestLoader查找case
tests = unittest.defaultTestLoader.discover(m2path,pattern='*.py',top_level_dir=None)

# 在测试套件中添加测试用例集
suite.addTests(tests)

# 运行测试套件
runner = unittest.TextTestRunner(verbosity=0)
runner.run(suite)
