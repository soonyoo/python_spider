# coding = utf-8


class Game(object):
    # 游戏最高分，类属性
    top_score = 0

    # 定义实例属性
    def __init__(self, player_name):
        self.player_name = player_name

    # 定义静态方法,游戏说明
    @staticmethod
    def show_help():
        print('帮助信息：让僵尸走进房间')

    # 定义类方法
    @classmethod
    def show_top_score(cls):
        print("游戏最高分是 %d" % cls.top_score)

    # 定义实例方法
    def start_game(self):
        print('[%s] 开始游戏...' % self.player_name)


if __name__ == '__main__':
    # 1. 查看游戏帮助
    Game.show_help()
    # 2. 查看游戏最高分
    Game.show_top_score()
    # 3. 创建游戏对象，开始游戏
    game = Game('小明')
    game.start_game()
    # 4. 游戏结束，查看游戏最高分
    Game.show_top_score()
