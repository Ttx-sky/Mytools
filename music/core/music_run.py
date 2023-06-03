import datetime
import logging
import os
import queue
import random
import time
import eyed3
import pygame
# from eyed3 import AudioFile
from tqdm import tqdm
import pathlib
import sys
import warnings
import json

"""

Mytools工具箱
time = 2023/4

"""


class Mytools:
    def __init__(self, family=''):
        self.family = family

    def getMy(self, name=None, r="r", encode="utf-8"):
        with open(name, f'{r}', encoding=encode) as summ:
            summ = summ.read()
        return summ

    def putMy(self, name=None, a="a", encode="utf-8", write=None):
        with open(name, f'{a}', encoding=encode) as summ:
            summ.write(write)
            summ.close()
        return 0

    def end(self, family, room=','):  # 连接字符串
        summ = ''
        for i in family:
            summ = summ + i + room
        return summ

    def random_run(self, number1=0, number2=0):
        return random.randint(number1, number2)

    def json_bag(self, list: list = None):
        return json.dumps(list)

    def Piphelp(self):
        if sys.path[0] in ("", os.getcwd()):
            sys.path.pop(0)
        # If we are running from a wheel, add the wheel to sys.path
        # This allows the usage python pip-*.whl/pip install pip-*.whl
        if __package__ == "":
            # __file__ is pip-*.whl/pip/__main__.py
            # first dirname call strips of '/__main__.py', second strips off '/pip'
            # Resulting path is the name of the wheel itself
            # Add that to sys.path so we can import pip
            path = os.path.dirname(os.path.dirname(__file__))
            sys.path.insert(0, path)
        # Work around the error reported in #9540, pending a proper fix.
        # Note: It is essential the warning filter is set *before* importing
        #       pip, as the deprecation happens at import time, not runtime.
        warnings.filterwarnings(
            "ignore", category=DeprecationWarning, module=".*packaging\\.version"
        )


class Mygo:
    def __init__(self, number=0, family="False"):
        self.family = family
        self.number = number

    def go_10_2(self):  # 进制10 > 2
        # this will print a in binary
        if self.family == "False":
            print("null")
            pass
        elif self.family == "True":
            bnr = bin(self.number).replace('0b', '')
            x = bnr[::-1]  # this reverses an array
            while len(x) < 8:
                x += '0'
            bnr = x[::-1]
            return bnr

    def go_2_10(self):  # 进制2 > 10
        if self.family != "False":
            print("null")
            pass
        elif self.family == "False":
            return str(int(self.number, 2))

    def time_past(self):  # 获取时间戳
        if self.family == "Tiem":
            return datetime.datetime.now().timestamp()
        elif self.family != "Tiem":
            print("null")
            pass


class Mymusic:
    def __init__(self, family='-1', room='False', name="False", number=1):
        self.name = name
        self.family = family
        self.room = room
        self.number = number
        self.q = queue.Queue()
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

    def stop(self):
        pygame.mixer.music.stop()
        # 暂停

    def pause(self):
        pygame.mixer.music.pause()
        # 取消暂停

    def unpause(self):
        pygame.mixer.music.unpause()

    def music(self):
        def music_run(family='-1', music_time=0, number=self.number):  # 音乐播放器， 炸内存
            """
            获取mp3音频文件时长
            :param file_path:
            :return:
            :(self, iterable=None, desc=None, total=None, leave=True, file=None,
                 ncols=None, mininterval=0.1, maxinterval=10.0, miniters=None,
                 ascii=None, disable=False, unit='it', unit_scale=False,
                 dynamic_ncols=False, smoothing=0.3, bar_format=None, initial=0,
                 position=None, postfix=None, unit_divisor=1000, write_bytes=False,
                 lock_args=None, nrows=None, colour=None, delay=0, gui=False,
                 **kwargs):
            """
            global music, mp3Info
            # mp3Info = eyed3.load(family)
            # os.system(rf'{music}')
            if family == '-1' and self.family == '-1':
                print('music(name=.mp3) -->music = ?, {无效}')
                pass
            # pygame.mixer.init(frequency=15500, size=-16, channels=4, )
            # pygame.mixer.music.load(fr"{famly}")
            # pygame.mixer.Sound(fr'{family}').play()
            # pygame.mixer.get_busy()
            # pygame.mixer.music.play(loops=self.number)
            for _ in range(number):
                #try:
                pygame.mixer.init(frequency=15500, size=-16, channels=4, )
                pygame.mixer.Sound(fr'{family}').play()
                #except FileNotFoundError:
                #    print("A Bug in pygame", FileNotFoundError.)
                #    break
                for _ in tqdm(range(int(music_time))):
                    pygame.mixer.get_busy()
                    time.sleep(1)
            # while pygame.mixer.get_busy():
            #     time.sleep(mp3Info.info.time_secs)
            #     break
            # pygame.mixer.music.play()
            # pygame.mixer.music.load()
            # pygame.mixer.music.pause()  # 暂停
            # pygame.mixer.music.unpause()  # 取消暂停
            # 成功播放音乐，并有暂停，取消暂停功能。

        global directory
        path = os.listdir()
        if self.room != 'False':  # 直接命令播放
            music_run(self.room)
        if self.family == 'True_one' and self.room != 'False':
            while True:
                music_run(self.room)
        elif self.family == 'True':  # 进行音乐播放
            print(f'当前文件夹:{path}')
            # directory = askdirectory()
            directory = os.getcwd()
            os.chdir(directory)
            print('home:', directory)
            for i in path:
                bool = i.endswith(".mp3" or ".m4a")
                if self.name != "False":
                    bool = self.name.endswith(".mp3" or "m4a")
                    i = self.name
                logging.debug(f'Myfamily={self.family} & {i} : {bool} --> None')
                # print(f'Myfamily={self.family} & {i} : {bool} --> None')
            for i in path:
                bool = i.endswith(".mp3")
                if self.name != "False":
                    bool = self.name.endswith(".mp3")
                    i = self.name
                if bool:
                    try:
                        mp3Info = eyed3.load(i)
                        music_time = mp3Info.info.time_secs
                    except OSError or AttributeError:
                        music_time = 0
                    music_time_1 = (music_time // 60) / 1
                    music_time_2 = music_time - (music_time_1 * 60)
                    # logging.debug(f'正在播放:{directory}\{i}\nname={i}\ntime={music_time_1}:{music_time_2};{music_time}')
                    print(f'正在播放:{i}\nname={i}\ntime={int(music_time_1)}:{int(music_time_2)};{music_time}')
                    # print(music_time //1, music_time / 1)
                    music_run(i, music_time // 1)
                    if self.name != "False":
                        break
        elif self.family == 'True_th.':  # 只进行数据报告
            print(f'当前文件夹：{path}')
            # directory = askdirectory()
            directory = os.getcwd()
            os.chdir(directory)
            print('home:', directory)
            for i in path:
                bool = i.endswith(".mp3")
                print(f'Myfamily={self.family} & {i} : {bool} : None')


if __name__ == '__main__':
    Mymusic(family='True', name=fr'..\lib\music\GRRRLS.mp3', number=2).music()

