import pytest

#设置作用域为class,自动运行
@pytest.fixture(scope='class',autouse=True)

def token():
    token = 110
    return token

class Test_demo03():

    def test_case01(self,token):
        mydata = {'mytoken':token}
        assert (mydata != None)
        print(mydata)

    def test_case02(self,token):
        hedata = {'hedata':token}
        assert (hedata)
        print(hedata)

if __name__ == '__main__':
    pytest.main(['test_demo03.py'])