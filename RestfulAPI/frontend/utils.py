import datetime
import time

def rest_of_day(): # 截止到目前当日剩余时间
    now = datetime.datetime.now()
    today = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d")
    tomorrow = today + datetime.timedelta(days=1)
    today_rest_time = tomorrow - now
    today_rest_seconds = today_rest_time.total_seconds()
    today_rest_time = '%dh %02dmin' % (today_rest_seconds / 3600, today_rest_seconds / 60 % 60)
    return {'today_rest_time': today_rest_time}