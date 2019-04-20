import time
s = time.time()

min = s//60
min_cur = min % 60
hour = s // 3600
hour_cur = hour % 24

hour_i = int(hour_cur)
min_i = int(min_cur)

print("현재 시간 (영국 그리니치 시각:)" + str(hour_i) + "시", str(min_i) +"분")
