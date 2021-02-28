import unittest
import requests
from test_config.test_url import sit_url


class poetryFull(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        pass

    @classmethod
    def tearDown(self) -> None:
        pass

    def test_poetryFull_case01(self):
        '''poetryFull接口'''
        test_headers = {'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'zh-CN,zh;q=0.9',
                        }

        test_url = sit_url + 'poetryFull'

        test_data = {"count": 1,
                     "page": 1, }

        test_request = requests.get(test_url, test_data)

        test_response = test_request.json()

        self.assertEqual(test_response['code'],200,msg='code错误')
        self.assertEqual(test_response['message'], '成功!', msg='message错误')

        return print(test_response)



if __name__ == "__main__":
    unittest.main(verbosity=0)