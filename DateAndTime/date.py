import time,datetime
epoch = time.time()
print (epoch)
t=time.ctime(epoch)
print(t)


dt=datetime.datetime.today()
print (dt)

print(dt.day,dt.month,dt.year)
print (dt.hour,dt.minute,dt.second)