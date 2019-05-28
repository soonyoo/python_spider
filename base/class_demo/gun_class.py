# coding: utf-8


class Gun(object):
    """士兵突击枪类"""
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    # 装子弹
    def add_bullet(self, num):
        self.bullet_count += num

    # 发射子弹
    def shoot(self):
        # 1.判断枪中还有没有子弹
        if self.bullet_count <= 0:
            print('[%s ]已没有子弹了' % self.model)
            return

        # 2.子弹数量减1
        self.bullet_count -= 1

        print('[%s] 发射子弹.. 还有[%d]发子弹！' % (self.model, self.bullet_count))


if __name__ == '__main__':
    gun_ak47 = Gun('AK47')
    gun_ak47.add_bullet(50)
    gun_ak47.shoot()
