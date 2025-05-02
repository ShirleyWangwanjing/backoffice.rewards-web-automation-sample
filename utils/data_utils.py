# -*- coding: utf-8 -*-
import random
from datetime import datetime


class DataUtils(object):
    @staticmethod
    def get_random_data(from_data, to_data, except_list=None):
        start_time = datetime.now()
        end_time = datetime.now()
        time_available = (end_time - start_time).seconds <= 2
        while time_available is True:
            result = random.randint(from_data, to_data)
            if result not in except_list:
                return result
        return None


