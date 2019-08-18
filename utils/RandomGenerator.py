from .RandomDataType import *
import string
import random
import calendar
import time


def generateRandom(type,length=0,future_time_in_min=0,future_time_in_sec=0):
    if(RandomDataType.STRING==type and length!=0):
        return ''.join(random.choices(string.ascii_uppercase,k=length))
    if(RandomDataType.NUMBER==type and length!=0):
        return ''.join(random.choices(string.digits,k=length))
    if(RandomDataType.EMAIL==type and length!=0):
        return ''.join(random.choices(string.digits,k=length))+'@'+'email.com'
    if(RandomDataType.TIMESTAMP==type):
        return calendar.timegm(time.gmtime())+(future_time_in_min*60) + future_time_in_sec




