import datetime

now = datetime.datetime.now()

print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%f')) # 날월년-시분초 마이크로초

today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%f'))

print(now)
d = datetime.timedelta(weeks=1) # 날짜 계산기 월, 년은 안됨. 주 일 시간 분 초 마이크로 초
print(now - d)

import time

# time.sleep(2)
print(time.time())

import os
import shutil

file_name = 'test.txt'

if os.path.exists(file_name): # 파일 존재 시
    shutil.copy(file_name, f"{file_name}.{now.strftime('%y_%m_%d-%H_%M_%S')}") # 오늘자의 백업파일 생성

with open(file_name, 'w') as f:
    f.write('test')