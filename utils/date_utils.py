from datetime import datetime, timedelta
import time


class DateUtils(object):
    @staticmethod
    def get_local_current_time():
        return datetime.now()

    @staticmethod
    def get_utc_current_time():
        return datetime.utcnow()

    @staticmethod
    def seconds_between(start_time, end_time):
        if isinstance(start_time, str):
            start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        if isinstance(end_time, str):
            end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        return (end_time - start_time).seconds

    @staticmethod
    def adjust_second_from_now(offset, data_format="%Y-%m-%d %H:%M:%S"):
        return (datetime.now() + timedelta(seconds=offset)).strftime(data_format)

    @staticmethod
    def adjust_day_from_now(offset, data_format="%Y-%m-%d %H:%M:%S"):
        return (datetime.now() + timedelta(days=offset)).strftime(data_format)

    @staticmethod
    def get_timestamp():
        return str(time.time())
