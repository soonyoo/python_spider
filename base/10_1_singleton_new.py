# coding = utf-8


# 单例设计模式之：重写__new__方法
class MusicPlayer(object):
    def __init__(self):
        print('播放器初始化...')

    def __new__(cls, *args, **kwargs):
        # 1.创建对象时，new方法会被自动调用
        print('__new__方法，创建对象，分配空间')
        # 2.为对象分配空间
        instance = super().__new__(cls)
        # 3.返回对象的引用
        return instance


if __name__ == '__main__':
    player1 = MusicPlayer()
    print(player1)
    player2 = MusicPlayer()
    print(player2)
