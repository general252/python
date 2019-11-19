# -*- coding: utf-8 -*-
from id_validator import validator
import time


# 生成出生当年所有日期
def date_range(year):
    fmt = '%Y-%m-%d'
    bgn = int(time.mktime(time.strptime(year + '-01-01', fmt)))
    end = int(time.mktime(time.strptime(year + '-12-31', fmt)))
    list_date = [time.strftime(fmt, time.localtime(i)) for i in range(bgn, end + 1, 3600 * 24)]
    return [i.replace('-', '') for i in list_date]


# 遍历所有日期，print通过校验的身份证号码

def my_validator(id1, id2, id3):
    for i in date_range(id2):
        the_id = id1 + i + id3
        if validator.is_valid(the_id):
            print(the_id)


my_validator('340123', '1993', '8572')

print(validator.get_info('340123199302288572'))
