from datetime import date
import time
startTime=time.perf_counter()
ldates=[]
d1=date(2016,8,12)
d2=date(2017,8,12)
d3=date(2018,8,12)
d4=date(2019,8,12)

ldates.append(d1)
ldates.append(d4)
ldates.append(d3)
ldates.append(d3)

ldates.sort()
print(ldates)

time.sleep(3)
for d in ldates:
    print(d)
endTime=time.perf_counter()
print("Execution time: ", endTime-startTime)