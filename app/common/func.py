# -*- coding:utf-8 -*-


import time, calendar
from random import randint as ran
from random import randrange
import hashlib
from datetime import datetime

random_list = lambda _list:(_list[randrange(len(_list))])


def IDGenerator():
    ratios = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    lastnos = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    provincelist = ['340621','110101','310000','230321']
    currenttime = time.localtime()
    currentyear = currenttime[0]
    pro = random_list(provincelist)
    preno = '%s%d%02d%02d%03d' % (pro, ran(currentyear - 80, currentyear - 18), ran(1, 12), ran(1, 28), ran(1, 999))
    tmpsum = 0
    for i in range(17):
        tmpsum += (int(preno[i]) * ratios[i])
    lastno = lastnos[tmpsum % 11]
    IDno = preno + lastno
    return IDno


def CMBGenerator(precmb):
    LastSeven = ran(1000000, 9999999)
    return precmb + str(LastSeven)


def GetMd5(param):
    bytestr = param.encode(encoding="utf-8")
    md5value = hashlib.md5(bytestr).hexdigest()
    return md5value


def GetWeekNo(year, month, day):
    count = 1
    for i in range(1, int(day)):
        if calendar.weekday(int(year), int(month), i) == 5:
            count += 1
    return count


def setUnnecessaryParam(body, param, default_value):
    try:
        key = body[param]
    except KeyError:
        key = default_value
    return key


def current_time():
    currentTime = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    return currentTime
