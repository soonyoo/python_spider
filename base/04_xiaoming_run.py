# coding: utf-8


class Person(object):
    """
    小明爱跑步：面向对象实例。
    """

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        # return "我的名字叫:%s,我的体重是:%.2f" % (self.name, self.weight)
        return "我的名字叫:{},我的体重是:{:.2f}公斤".format(self.name, self.weight)

    def run(self):
        print('{}爱跑步，跑步煅炼身体！'.format(self.name))
        self.weight -= 0.5

    def eat(self):
        print('{}是吃货，吃完这餐再减肥！'.format(self.name))
        self.weight += 1


if __name__ == '__main__':
    # 小明爱跑步
    xiaoming = Person('小明', 75)
    xiaoming.run()
    xiaoming.eat()
    print(xiaoming)
    print('#' * 40)
    # 小美也爱跑步
    xiaomei = Person('小美', 60)
    xiaomei.eat()
    xiaomei.run()
    print(xiaomei)
    # 再print一次小明，看看是否对结果产生影响
    print('#' * 40)
    print(xiaoming)
    # 结论，实例化对象里的属性互不影响




