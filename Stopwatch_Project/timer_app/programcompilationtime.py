import time
import datetime

my_list=list(range(100000000))
element=700000

start=time.time()
for i in my_list:
    if i==element:
        break
end=time.time()
print(end-start)    