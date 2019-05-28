# coding: utf-8
from gun_class import Gun


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        # 1. 判断士兵是否有枪
        if self.gun is None :
            print('[%s] 还没有枪！' % self.name)
            return
        # 2.高喊口号
        print('冲啊...[%s]' % self.name)

        # 3.让枪装填子弹
        self.gun.add_bullet(50)

        # 4.让枪发射子弹
        self.gun.shoot()


if __name__ == '__main__':
    xusanduo = Soldier('许三多')
    gun_ak47 = Gun('AK47')
    xusanduo.gun = gun_ak47
    xusanduo.fire()


