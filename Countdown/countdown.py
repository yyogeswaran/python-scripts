import time
import sys
i = input("enter total seconds of countdown....")
while i!=0:
    sys.stdout.write('\r'+str(i))
    sys.stdout.flush()
    i=i-1
    time.sleep(1)
