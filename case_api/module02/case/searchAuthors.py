import unittest
import requests
import json
import parameterized
from test_config.test_url import sit_url


class searchAuthors(unittest.TestCase):
    #构造参数化变量列表
    names = []
    #利用文件内容参数化，维护参数化文件实现请求多次传参数
    name_data = open(r'D:\PycharmProjects\auto_test\case_api\module02\data\searchAuthors', 'r', encoding='utf-8')
    #循环文件内容添加到参数化变量列表
    for x in name_data:
        #分割文件内容
        x1 = x.split()
        #将分割的内容，循环添加到数化变量列表
        names.append(x1)

    #使用parameterized包，使用参数化变量列表
    @parameterized.parameterized.expand(names)
    #构造测试函数，引用参数化变量列表
    def test_searchAuthors(self,names):
        '''开始测试searchAuthors'''
        # 构造请求信息头
        test_headers = {'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'zh-CN,zh;q=0.9',
                        }

        # 构造请求地址
        test_url = sit_url + 'searchAuthors'

        # 构造请求参数（调用参数化变量列表）
        test_data = {'name': names}

        # 构造请求过程
        test_request = requests.post(test_url, test_data, test_headers)

        # 构造响应结果
        test_response = json.dumps(test_request.json(), ensure_ascii=None)

        #构造断言
        self.assertIn('200',test_response)

        # 构造显示相关特征
        print(test_url,
              test_request.request,
              test_data,
              test_response)
        return test_response

if __name__ == "__main__":
    unittest.main(verbosity=2)
