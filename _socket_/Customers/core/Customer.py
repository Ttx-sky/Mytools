import asyncio
import socket
import json
import time

"""
class Client(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.loop = asyncio.get_running_loop()

    async def __aenter__(self):
        self.Client = socket.socket()
        self.Client.connect((self.ip, self.port))
        await self.loop.sock_connect(self.Client, (self.ip, self.port))
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.Client.close()

    async def recv(self, recv_num):
        data = await self.loop.sock_recv(self.Client, recv_num)
        return data

    async def send(self, data):
        await self.loop.sock_sendall(self.Client, data)


async def main():
    async with Client("192.168.1.5", 1008) as c:
        await c.send('abc')
    data = await c.recv(1024)
    print(data)


asyncio.run(main())
"""


def recv(_data_):
    with open("..\lib/txt.json", "rb") as this:
        data = json.loads(this.read())
        data["data"] = _data_
        return json.dumps(data)


def recv__(data):
    # print(data.decode("utf-8"))
    data = json.loads(data.decode())
    # print(data)
    time_ = time.time() - data["Time"]
    if time_ >= 10:
        print("超时")
    elif time_ < 10:
        return data["data"]


def Run(data):
    s = socket.socket()
    s.connect(data)
    while True:
        s.send(recv(input(">>>")).encode("utf-8"))
        data = recv__(s.recv(1024))
        print(data)


if __name__ == '__main__':
    Run(("192.168.1.5", 1005))
