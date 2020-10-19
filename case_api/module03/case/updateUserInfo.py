import unittest
import requests
import json
from test_config.test_url import sit_url
'''
测试接口指定数据文件
实际是已经转换好json格式的txt文件
每个txt文件代表一个case
通过设置多个test函数和断言，执行不同的场景
适用于入参字段比较多的情况
'''
class updateUserInfo(unittest.TestCase):
    #设置用例文件路径
    updateUserInfo_case1 = open(r'D:\PythonProject\auto_test\case_api\module03\data\updateUserInfo_case1','r',encoding='utf-8')
    updateUserInfo_case2 = open(r'D:\PythonProject\auto_test\case_api\module03\data\updateUserInfo_case2','r',encoding='utf-8')

    # 构造接口请求函数（接口请求过程）
    def updateUserInfo(self,case) -> None:
        '''开始测试：updateUserInfo'''

        # 构造请求信息头
        test_headers = {'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'zh-CN,zh;q=0.9',
                        }
        # 构造请求地址
        test_url = sit_url + 'updateUserInfo'

        # 构造请求参数（参数化，调用函数传参）
        test_data = case

        # 构造请求过程
        test_request = requests.post(test_url, test_data, test_headers)

        # 构造响应结果
        test_response = json.dumps(test_request.json(), ensure_ascii=None)

        # 构造显示相关特征
        print(test_url,
              test_request.request,
              test_data,
              test_response)
        return test_response

    def test_case1(self):
        '''test_case1'''
        #传参时候读取设置的设置用例文件
        self.case = json.load(self.updateUserInfo_case1)
        #构造断言
        self.assertIn('400',self.updateUserInfo(case='"code": 400,'))

    def test_case2(self):
        '''test_case2'''
        self.case = json.load(self.updateUserInfo_case2)
        self.assertIn('400', self.updateUserInfo(case='"code": 400,'))




if __name__ == "__main__":
    unittest.main(verbosity=0)



