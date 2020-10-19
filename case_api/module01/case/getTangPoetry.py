import unittest
import requests
import json
from test_config.test_url import sit_url
'''
针对接口测试函数，将接口请求的入参作为形参
维护test_case时候将形参赋予值
实现一个接口对用多个不同入参场景
维护每个test_case的入参，断言即可
适用于每个场景断言不一致的情况
'''
#创建getTangPoetry接口的测试类
class getTangPoetry(unittest.TestCase):
    #构造接口请求函数（接口请求过程）
    def getTangPoetry(self,page,count) -> None:
        '''开始测试：getTangPoetry'''
        #构造请求信息头
        test_headers = {'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
                        'accept-encoding':'gzip, deflate, br',
                        'accept-language': 'zh-CN,zh;q=0.9',
                        }
        #构造请求地址
        test_url =  sit_url + 'getTangPoetry'

        #构造请求参数（参数化，调用函数传参）
        test_data = {'page':page,
                     'count':count,}

        #构造请求过程
        test_request = requests.post(test_url,test_data,test_headers)

        #构造响应结果
        test_response = json.dumps(test_request.json(),ensure_ascii=None)

        #构造显示相关特征
        print(test_url,
              test_request.request,
              test_data,
              test_response)
        return test_response

    #针对接口请求函数构造多个测试用例（不同入参（场景），比如一个接口的正常场景、异常场景等）
    def test_case1(self):
        '''test_case1'''
        page = 1
        count = 1
        #构造断言
        self.assertIn('200',self.getTangPoetry(page,count))

    def test_case2(self):
        '''test_case2'''
        page = 1
        count = 2
        self.assertIn('200',self.getTangPoetry(page,count))

if __name__ == "__main__":
    unittest.main(verbosity=0)