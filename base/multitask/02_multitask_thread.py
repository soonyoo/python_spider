# coding = utf-8

import time
import threading


def sing():
    """唱歌5秒钟"""
    for i in range(5):
        print('...正在唱青花瓷...')
        time.sleep(1)


def dang():
    """跳舞5秒钟"""
    for i in range(5):
        print('...正在跳舞...')
        time.sleep(1)


def main():
    task1 = threading.Thread(target=sing)
    task2 = threading.Thread(target=dang)
    task1.start()
    task2.start()


def say_sorry():
    print('亲爱的，我错了。。。')
    time.sleep(1)


if __name__ == '__main__':
    # main()
    for i in range(5):
        task3 = threading.Thread(target=say_sorry)
        task3.start()




