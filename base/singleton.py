# coding = utf-8
"""
# 单例实现原理:
# 1.判断类属性是否为空对象
    # 1.1 如果为空，则为对象分配空间
    # 1.2 如果不为空，则直接返回
"""


class MusicPlayer(object):
    # 定义类属性
    # # 记录第一个被创建对象的引用
    instance = None
    # # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否为空对象
        # 1.1 如果为空，则为对象分配空间
        # 1.2 如果不为空，则直接返回
        if cls.instance is None:
            # 2.调用父类方法，为第一个对象分配内存空间
            cls.instance = super().__new__(cls)
        # 3 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        if not MusicPlayer.init_flag:
            print('初始化音乐播放器..')
            MusicPlayer.init_flag = True


if __name__ == '__main__':
    player1 = MusicPlayer()
    print(player1)
    player2 = MusicPlayer()
    print(player2)
