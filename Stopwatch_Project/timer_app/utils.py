import time 
import datetime 
# Create your models here.
print("after 5 sec sleep time shows")
time.sleep(5)
print("sleep time")


current=datetime.datetime.now()
print ('current time ',str(current))
one_year=current + datetime.timedelta(days=365)
print('one year date',str(one_year))


seconds= time.time()
print("time in seconds  since the epoch",str (seconds))
local_time=time.ctime(seconds)
print ('ctime',str(local_time))