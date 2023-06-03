import os
from Mytools.PIP.lib.concurrent_log import GetLogger


class PIP:
    def __init__(self):

        pass

    def pip(self, moduls):  # 指定为清华大学镜像站
        module = f"pip install -i https://pypi.tuna.tsinghua.edu.cn/simple {moduls} "
        result = os.popen(module).read()
        return result

    def Help(self):  # 获取帮助
        return os.popen(f"pip --help").read()

    def Downloading_pip(self, PiP="pip"):  # 升级 pip
        return os.popen(f"python -m {PiP} install -U pip").read()

    def Uninstall(self, moduls):  # 卸载包
        return os.popen(f"pip uninstall {moduls}").read()

    def Search(self, moduls):  # 搜索包
        return os.popen(f"pip search {moduls}").read()

    def Show(self, moduls):  # 查看指定包的详细信息
        return os.popen(f"pip show -f {moduls}").read()

    def Pip_Order(self, order):  # 自定义
        return os.popen(order).read()

    def Version(self):  # 显示版本和路径
        return os.popen("pip --version").read()

    def List(self, order=None):  # 列出已安装的包
        return os.popen(f"pip list {order}").read()

    def Upgrade(self, moduls):  # 升级包
        return os.popen(f"pip install --upgrade {moduls}").read()

    def help_(self):
        print(PIP().Help())
        print(PIP().List())
        print(PIP().Version())
        while True:
            print(PIP().Pip_Order(input(">>>")))


if __name__ == '__main__':
    logger = GetLogger(logs_dir=r"Client_LOG", log_name="__LOG__").get_logger()
    while True:
        order = PIP().Pip_Order(input(">>>"))  # Get new pip.
        logger.info(order)

