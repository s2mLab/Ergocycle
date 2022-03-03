import time

t=2
t_sec = 60*(t)
while t_sec :
    min = t_sec//60
    sec = t_sec % 60
    t_layout = '{:02d}:{:02d}'.format(min, sec)
    print(t_layout)
    time.sleep(1)
    t_sec -= 1
print("done")
