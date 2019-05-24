# coding: utf-8


class HouseItem(object):
    """
    家具类
    """
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House(object):
    """
    房子类
    """
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具List
        self.house_item = []

    def add_item(self, item):
        if self.free_area < item.area:
            print("%s 的面积太大了，无法添加" % item.name)
            return
        # 添加家具
        self.house_item.append(item.name)
        # 剩余面积
        self.free_area -= item.area

    def __str__(self):
        return (" [%s] 户型，总面积[%.2f],剩余面积[%.2f] \n 家具:%s "
                % (self.house_type, self.area, self.free_area, self.house_item))


if __name__ == '__main__':
    bed = HouseItem("席梦思", 4.5)
    table = HouseItem("餐桌", 1.5)
    chest = HouseItem("衣柜", 2)
    # print(bed)
    my_house = House("两室一厅", 60)
    # my_house.add_item(bed)
    my_house.add_item(table)
    my_house.add_item(chest)
    print(my_house)


