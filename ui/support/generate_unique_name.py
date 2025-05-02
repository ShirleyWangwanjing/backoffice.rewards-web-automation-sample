import random
import string
from datetime import date
from time import time


class GenerateUniqueName(object):
    prefix = ''
    surfix = ''

    def __init__(self):
        self.surfix = '_' + date.today().strftime('%Y%m%d')+'_'+self.get_snap_shot()
        self.prefix = ''.join(random.sample(string.ascii_letters, 7))

    def set_prefix(self):
        self.prefix = ''.join(random.sample(string.ascii_letters, 7))

    def set_surfix(self):
        self.surfix = '_' + date.today().strftime('%Y%m%d')+'_'+self._get_random()

    def get_prefix(self):
        return self.prefix

    def get_surfix(self):
        return self.surfix

    def _get_random(self):
        return str(random.randint(0, 1000))

    def get_snap_shot(self):
        time_snap_shot = str(time())
        time_snap_shot = time_snap_shot.replace('.', '')
        return time_snap_shot
