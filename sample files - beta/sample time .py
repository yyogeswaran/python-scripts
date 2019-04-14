import datetime
x=datetime.datetime.now()
count =x.second
flag =count
end = count + 2 
print count,end
i=0
import sys
while True:
    print "inside while",count,end
    if count != end:
        #sys.stdout.write('%s'%i)
        count = datetime.datetime.now().second
        print i
        i=i+1
    else:
        print "the end"
        break
