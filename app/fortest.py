# -*- coding:utf-8 -*-

import time
from datetime import datetime


print(time.ctime())
print(datetime.utcnow())
print(datetime.date(datetime.now()))
print(datetime.time(datetime.now()))
print(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
