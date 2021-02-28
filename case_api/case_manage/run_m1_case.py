import unittest
import HTMLTestRunner
import time

# 设置运行case的模块（路径）
m1path = r'D:\PycharmProjects\auto_test\case_api\module01\case'

# 设置报告路径\时间\写入路径
report_path = r'D:\PycharmProjects\auto_test\test_report'
report_time = time.strftime('%Y%m%d%H%M%S',time.localtime())
report_file = report_path + r'\test' + report_time + '.html'
fb = open(report_file,'wb')

# 创建测试套件
suite = unittest.TestSuite()

#创建测试用例集，defaultTestLoader查找case
tests = unittest.defaultTestLoader.discover(m1path,pattern='*.py',top_level_dir=None)

# 在测试套件中添加测试用例集
suite.addTests(tests)

# 运行测试套件
# runner = unittest.TextTestRunner(verbosity=2)

# 运行带报告的测试套件
runner = HTMLTestRunner.HTMLTestRunner(stream=fb,title=u'测试报告',description=u'执行结果',tester=u'自动化测试')

runner.run(suite)
fb.close()
