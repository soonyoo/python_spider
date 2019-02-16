import os

class FileOpt(object):
    def __init__(self):
        # 1.获取文件当前所在的路径
        current_path = os.path.dirname(__file__)
        # 2.获取当前文件所在的路径的上级目录
        pre_path = os.path.dirname(current_path)
        # 3.拼接路径
        images_path = os.path.join(pre_path,'images')
        # 4.如果目录不存在，创建目录
        if not os.path.exists(images_path):
            os.mkdir(images_path)
            # print('文件夹不存在...')

        else:
            print('文件夹已存在...')



    def opt(self):
        pass


if __name__ == '__main__':
    file = FileOpt()