import requests
from lxml import etree
import pymongo
from getip import GETIP
import time
from multiprocessing import Pool


class GetFreeIP:
    def __init__(self, start_page, end_page):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Referer": "http://www.66ip.cn/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }
        self.url = ["http://www.66ip.cn/", ]
        self.end_page = end_page
        self.ip_proxy = GETIP().run()
        self.start = start_page

    def get_html(self):
        url_list = [self.url[0] + f'{p}.html' for p in range(self.start, self.end_page + 1)]
        return url_list

    def get_data(self, url):
        url_list = url
        ip_list = []
        try:
            res = requests.get(url, headers=self.headers, proxies={'http': self.ip_proxy}, timeout=2)
            html = etree.HTML(res.text)
            ip_port = [i.strip() for i in html.xpath('//tr[position()>1]/td[position()<=2]/text()')]
            num = len(ip_port)

            for q in range(0, num, 2):
                ip_a_port = 'http://' + str(ip_port[q]) + ':' + str(ip_port[q + 1])
                ip_list.append(ip_a_port)
        except Exception as e:
            self.ip_proxy = GETIP().run()
            error_page = url_list.index(url)
            self.get_data(url_list[error_page:])
        return ip_list

    def check_ip(self, ip):
        try:
            res = requests.get('http://httpbin.org/ip', headers=self.headers, proxies={'http': ip},
                               timeout=2)
            if res.status_code == 200:
                print('IP可用-->', ip)
                return ip
        except Exception:
            pass

    def save_data(self, ok_ip_list):
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client["ip_proxy"]
        for d in ok_ip_list:
            exists = db.ip_proxy.count_documents({'http': d})
            if exists == 0:
                db.ip_proxy.insert_one({'http': d})
                print("录入新IP:", d)
            else:
                print("当前IP已经录入:", d)
        client.close()

    def run(self):
        start = time.time()
        pool = Pool(processes=2)
        url_list = self.get_html()
        ip_list = pool.map(self.get_data, url_list)
        ip_lists = []
        for i in ip_list:
            ip_lists += i
        pool2 = Pool(processes=5)
        check_ip_list = pool2.map(self.check_ip, ip_lists)
        ok_ip = [i for i in check_ip_list if i is not None]
        self.save_data(ok_ip)
        print('用时:', time.time() - start)


if __name__ == '__main__':
    GetFreeIP(start_page=21, end_page=200).run()
