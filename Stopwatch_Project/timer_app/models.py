

import time
  
# Timer starts
starttime = time.time()
lasttime = starttime
lapnum = 1
value = ""
  
print("Press ENTER for each lap.\nType Q and press ENTER to stop.")
  
while value.lower() != "q":
              
    # Input for the ENTER key press
    value = input()
  
    # The current lap-time
    laptime = round((time.time() - lasttime), 2)
  
    # Total time elapsed since the timer started
    totaltime = round((time.time() - starttime), 2)
  
    # Printing the lap number, lap-time, and total time
    print("Lap No. "+str(lapnum))
    print("Total Time: "+str(totaltime))
    print("Lap Time: "+str(laptime))
            
    print("*"*20)
  
    # Updating the previous total time and lap number
    lasttime = time.time()
    lapnum += 1
  
print("Exercise complete!")
# from django.db import models

# import time 
# import datetime


# # timer starts
# starttime=time.time()
# endtime=starttime
# lapnum= 1
# values=""

# print ("press ENTER to start new lap.\ntype Q and press ENTER to stop ")

# while values.lower() != "q":
#     value=input()
#     laptime=round((time.time()-endtime),2)
#     totaltime=round(time.time(),starttime)
#     print('value',+str(value))
#     print('laptime',+str(laptime))
#     print('totaltime',+str(totaltime))
             
#     print("*"*20)
  
#     # Updating the previous total time and lap number
#     lasttime = time.time()
#     lapnum += 1
  
# print("Exercise complete!")




