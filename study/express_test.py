# coding:utf-8
import unittest
import requests


class ExpressTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_yunda(self):
        # url拼接
        id = '1202247993797'
        kd = 'yunda'
        url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html'
        header = {
            "Connection": "keep - alive",
            "Content - Length": "160",
            "Accept": "* / *",
            "X - Requested - With": "XMLHttpRequest",
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit "
                            "/ 537.36(KHTML, like Gecko) Chrome / 81.0.4044.113 Safari / 537.36",
            "Content - Type": "application / x - www - form - urlencoded;charset = UTF - 8",
            "Origin": "http: // www.kuaidi.com",
            "Referer": "http: // www.kuaidi.com /",
            "Accept - Encoding": "gzip, deflate",
            "Accept - Language": "zh - CN, zh;q = 0.9",
            "Cookie": "lang = zh - cn; theme = default; sid = 344bfk4icp8mev1ito0bph1ca5;"
                      " UM_distinctid = 171919a363764 - 0b03108665326 - 39624006 - 100200 - 171919a36391fc;"
                      " __gads = ID = dcbb3a4bfd6796c7:T = 1587285735:S = ALNI_MZOlzVnPOwTc49AQg3kzM - hAUWnrA; "
                      "CNZZDATA1254194234 = 226183599 - 1587281945 - % 7C1587295958",
        }
        json_data = {
            "geetest_challenge": "f8a8887910046c96a2909e3d8121942bl3",
            "geetest_validate": "e433138b1d5a884a3566da05bc2187d2",
            "geetest_seccode": "e433138b1d5a884a3566da05bc2187d2 % 7 Cjordan"
        }

        res = requests.post(url, data=json_data, headers=header)
        # 获取响应内容--快递公司、订单状态
        result = res.json()
        print(result)
        print(type(result))
        company_name = result['company']
        print('快递公司：')
        print(company_name)
        # print('快递公司：' + company_name)

        data = result['data']
        mess = data[0]
        status = mess['context']
        print(status)
        # print('订单状态：' + status)

        # 断言
        self.assertEqual('韵达快递', company_name)
        self.assertIn('已签收', status)


if __name__ == '__main__':
    unittest.main()