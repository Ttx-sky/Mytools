import socket
import json
import asyncio
import time
import datetime
import logging.config
import mkcloud
from Mytools._socket_.lib import settings
from Mytools._socket_.lib.concurrent_log import GetLogger
from Mytools.Email.main import Email

# import logger_BIND
# import logger_CLOSE

# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/5/27/15.37
# @Software: PyCharm
# @Order: Administrator GetNew客户.py
# @USE     : https://github.com/dkvnejvn


def recv(_data_):
    with open("./db/txt.json", "rb") as this:
        data = json.loads(this.read())
        data["Time"] = time.time()
        data["data"] = _data_
        this.close()
        return json.dumps(data)


class Client:
    def __init__(self):
        # logger_BIND.getLogger('用户登录')
        # logger_CLOSE.getLogger('用户下线')'
        with open("./db/Key.json", "rb") as this:
            self.read = json.loads(this.read())
        self.logger = GetLogger(logs_dir=r"./logs/Client_LOG", log_name="__LOG__").get_logger()
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')
        pass

    async def waiter(self, conn, addr, loop):
        self.logger.info(f"A new conn:{addr}.")

        while True:
            try:
                data = await loop.sock_recv(conn, 2048)
                if not data:
                    break
                # print(data.decode())
                data = json.loads(data.decode())
                YUE_data = recv(mkcloud.robot.chat(data["data"]))
                # print(YUE_data, YUE_data.encode())
                await loop.sock_sendall(conn, YUE_data.encode())
            except ConnectionResetError:
                break
        # print(datetime.datetime.now(), "A conn close:", addr)
        self.logger.info(f"A conn close:{addr}")  # -> 单个， 否则使用“,”隔开
        # logging.debug((datetime.datetime.now(), "A conn close:", addr))
        # self.logger_CLOSE.info(addr)
        conn.close()

    async def main(self, ip="localhost", port=5000):
        try:
            # print(f"The socket accept at (IP:{ip} PORT:{port}) time={time.time()};{datetime.datetime.now()}")
            self.logger.info(f"The socket accept at (IP:{ip} PORT:{port}) ")
            # logging.debug(f"The socket accept at (IP:{ip} PORT:{port}) time={time.time()};{datetime.datetime.now()}")
            server = socket.socket()
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((ip, port))
            server.listen(10)
            server.setblocking(False)
            loop = asyncio.get_running_loop()
            while True:
                conn, addr = await loop.sock_accept(server)
                # logging.debug((datetime.datetime.now(), "A new conn:", addr))
                # self.logger_BIND.info(addr)
                loop.create_task(Client().waiter(conn, addr, loop))
        finally:
            self.logger.error(f"The socket Client has a bug ({time.time()}/{datetime.datetime.now()})")
            data = Email(data=f"The socket Client has a bug ({time.time()}/{datetime.datetime.now()})<Call to Debug engineer.",
                         from_name="Client",
                         to_name="何锦晴",
                         connect="smtp.qq.com",
                         email_main=f"ClientDeBug",
                         Password="qxbztofgsnsibfeh",
                         from_email="676105282@qq.com",
                         To_email=["q.w.e.a.s@icloud.com", "676105282@qq.com"]
                         ).Email()
            if data == "<200>":
                print("Email True")
            else:
                print("Email False")

if __name__ == '__main__':
    asyncio.run(Client().main(ip="192.168.1.5", port=1005))
