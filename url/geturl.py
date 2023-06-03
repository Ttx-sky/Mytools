import requests
import json


# import URL


class Get:
    def __init__(self, url=None, head=None):
        self.html = None
        self.head = head
        if url is None:
            print("url == None")
        elif url is not None:
            self.url = "https://" + url
        self.response = requests.get(url=self.url, headers=self.head)
    def get_HTML(self):
        # 获取网页信息
        html = self.response.text
        url = self.response.url
        encode = self.response.encoding
        return url, encode, html


head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
# HTML, url = Get(url="www.baidu.com", head=head).get_HTML()

if __name__ == '__main__':
    def jng(url, head):
        url, encode, HTML = Get(url=url, head=head)
        print(HTML)
        return HTML


    payload = {"account": "12312312",
               "is_bh2": "false",
               "is_crypto": "true",
               "mmt_key": "94cglx1k2VBIKvc9bVZ85PVJu5MeFkMh",
               "password": "HYxz2Ms20S8oRA1GJIiOBSX+v3f0JZPCzHN2DjuZ164nt8bd9ZcsWfbJp4nsZ/AmUoaLjvgoCx0s6X5rexTpp5eYvsayPZCuGpcQriCLLxizkcoA7bNZsPzk9tV1M50G6rBnmF8ww8TuFzHG2AG1K48RuwOMx8NY3Q5n3vj5K6I=",
               "support_reactivate": "true",
               "t": 1680672086034,
               "token_type": 4
               }
    header = {"Connection": "application/json;"}
    # 字典转换为json串
    e = arguments = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        "account": "13571845242",
        "geetest_challenge": "7511d13e41da33c406efd36a8caeae0c",
        "geetest_seccode": "263986626b657856d7a0efd2b8259f73|jordan",
        "geetest_validate": "263986626b657856d7a0efd2b8259f73",
        "is_bh2": "false",
        "is_crypto": "true",
        "mmt_key": "mGWFA6XtE8XepTYGyDEvAvsEEkXFYPWT",
        "password": "wclTY8gk9xxSYBcIGqIKKhBPJER6oTGDKm5/f9tQbNszag9HbOwbQo4IW8o2nV0e39YRBzbo4Q2Ok/a2Ku9jSpNTftV5HqY+2Et7qNU8+t8B+Ntn14meYm3f6C8IraluDe71ioVjke7JIjg/z+/W0uxxXddYg42VhG5nlZBM5JA=",
        "support_reactivate": "true",
        "t": 1680675155625,
        "token_type": 4
    }
    arguments = {
        ":authority": "api - edge.cognitive.microsofttranslator.com",
        ":method": "POST",
        ":path": "/ translate?from=en & to = zh - CHS & api - version = 3.0 & includeSentenceLength = true",
        ":scheme": "https",
        "accept": "* / *",
        "accept - encoding": "gzip, deflate, br",
        "accept - language": "zh - CN, zh;q = 0.9, en;q = 0.8, en - GB;q = 0.7, en - US;q = 0.6",
        "authorization": "Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6ImtleTEiLCJ0eXAiOiJKV1QifQ.eyJyZWdpb24iOiJnbG9iYWwiLCJzdWJzY3JpcHRpb24taWQiOiI2ZjY1YjliY2JkNjA0ZDg4ODhiZWI2M2I4MTM4ODZlZSIsInByb2R1Y3QtaWQiOiJUZXh0VHJhbnNsYXRvci5TMyIsImNvZ25pdGl2ZS1zZXJ2aWNlcy1lbmRwb2ludCI6Imh0dHBzOi8vYXBpLmNvZ25pdGl2ZS5taWNyb3NvZnQuY29tL2ludGVybmFsL3YxLjAvIiwiYXp1cmUtcmVzb3VyY2UtaWQiOiIvc3Vic2NyaXB0aW9ucy84MWZjMTU3Yi0zMDdlLTRjMjEtOWY3MS0zM2QxMDMwNGRmMzMvcmVzb3VyY2VHcm91cHMvRWRnZV9UcmFuc2xhdGVfUkcvcHJvdmlkZXJzL01pY3Jvc29mdC5Db2duaXRpdmVTZXJ2aWNlcy9hY2NvdW50cy9UcmFuc2xhdGUiLCJzY29wZSI6Imh0dHBzOi8vYXBpLm1pY3Jvc29mdHRyYW5zbGF0b3IuY29tLyIsImF1ZCI6InVybjptcy5taWNyb3NvZnR0cmFuc2xhdG9yIiwiZXhwIjoxNjgwOTM1MTkyLCJpc3MiOiJ1cm46bXMuY29nbml0aXZlc2VydmljZXMifQ.iTPweoES_dknxiGW3yFxUhwyzL_bfD2mVj-ddkigU0VfBOgQuKKT3uTKAPwaBQGVuMpu4eZcGhWrMEWl45xRpg",
        "content - length": 28,
        "content - type": "application / json",
        "origin": "https: // so.csdn.net",
        "referer": "https: // so.csdn.net / so / search?spm = 1001.2101.3001.4498 & q = py % 2B % E7 % 88 % AC % E8 % 99 % AB % 2BChatGPT & t = chat & u =",
        "sec - ch - ua": '"Chromium";v = "112", "Microsoft Edge";v = "112", "Not:A-Brand";v = "99"',
        "sec - ch - ua - mobile": "?0",
        "sec - ch - ua - platform": "Windows",
        "sec - fetch - dest": "empty",
        "sec - fetch - mode": "cors",
        "sec - fetch - site": "cross - site",
        "user - agent": "Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 112.0.0.0Safari / 537.36Edg / 112.0.1722.34",
    }
    data = json.dumps(arguments)
    print(data)
    # url = "https://static.geetest.com/captcha_v3/custom_batch/v3/17/2022-11-17T11/icon/cd3989143b2343edb60b826068723889.jpg?challenge=ba864f61ede5bf942a80b39d658dc51a"
    # url = 'https://eu-sycdn.kuwo.cn/e4fa25b8783b5aa5bf35e228207f629e/642d0375/resource/n2/36/89/2614506450.mp3'
    # url = "https://passport-api-v4.mihoyo.com/account/auth/api/webLoginByPassword"
    url = {
        "https://api-edge.cognitive.microsofttranslator.com/translate?from=en&to=zh-CHS&api-version=3.0&includeSentenceLength=true"}


    # res = requests.post(url, data=data, headers=header)
    # res = requests.get(url=url,headers=head)
    # print(url)
    # log: list = res.text
    # print(log)

    def run(url="https://api-edge.cognitive.microsofttranslator.com/translate?from=en&to=zh-CHS&api-version=3.0&includeSentenceLength=true",
            header=head, arguments=arguments):
        data = json.dumps(arguments)
        res = requests.post(url=url, data=data, headers=header)
        print(res.url)
        return arguments, res, res.text, res.encoding


    for i in url:
        arguments, log, __log__, encode = run(url=i)
        print(arguments)
        print(__log__)
        print(log, "->", encode)
