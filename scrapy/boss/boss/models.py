from datetime import datetime, timedelta


class ProxyModel(object):
    def __init__(self, data):
        self.ip = data['ip']
        self.port = data['port']
        self.expire_time = datetime.strptime(data['expire_time'], "%Y-%m-%d %H:%M:%S")
        self.proxy = 'https://{}:{}'.format(self.ip, self.port)
        self.blacked = False

    @property
    def is_expiring(self):
        if(self.expire_time - datetime.now()) < timedelta(seconds=10):
            return False
        else:
            return True
