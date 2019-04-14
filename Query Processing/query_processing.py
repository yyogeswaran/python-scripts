#creating dictionary with name as index values
from collections import OrderedDict
global dbase
dbase= {}
dbase = OrderedDict()
dbase['a']=OrderedDict()
dbase['b']=OrderedDict()
dbase['c']=OrderedDict()
dbase['d']=OrderedDict()
dbase['e']=OrderedDict()
dbase['f']=OrderedDict()

#entering mark for each students

#entering marks for stud a
dbase['a'] ['sub1'] = 45
dbase['a'] ['sub2'] = 60
dbase['a'] ['sub3'] = 76

#entering marks for stud b
dbase['b'] ['sub1'] = 80
dbase['b'] ['sub2'] = 91
dbase['b'] ['sub3'] = 72

#entering marks for stud c
dbase['c'] ['sub1'] = 78
dbase['c'] ['sub2'] = 85
dbase['c'] ['sub3'] = 64

#entering marks for stud d
dbase['d'] ['sub1'] = 73
dbase['d'] ['sub2'] = 78
dbase['d'] ['sub3'] = 54

#entering marks for stud e
dbase['e'] ['sub1'] = 71
dbase['e'] ['sub2'] = 82
dbase['e'] ['sub3'] = 30


#entering marks for stud a
dbase['f'] ['sub1'] = 35
dbase['f'] ['sub2'] = 56
dbase['f'] ['sub3'] = 78


#display as a matrix table
from pandas import *
#print DataFrame(dbase).T
#print dbase

#retriving key values
index = []
index = dbase.keys()


#result set
res_dbase= []
#table set of result
from tabulate import tabulate

while True:
    #getting input query-choices
    choice = raw_input("Enter Your Query Choice(Name/Marks/Quit(q))...").lower()

    #processing query
    if choice == 'name':
        name = raw_input("Enter the name of the student...").lower()
        if name in dbase.keys():
            res_dbase = dbase[name].items()
            print res_dbase
            print "\n MarkList of student ",name.upper()
            print tabulate(res_dbase,headers = ['subjects','marks'],tablefmt='orgtbl')
        else:
            print "The name is not available"
    elif choice == 'marks' or choice == 'mark':
        subject=raw_input("Enter the name of the subject...").lower()
        if subject == 'sub1':
            res_dbase=[]
            for x in index:
                res_dbase.append(str(dbase[x]['sub1']))
                #print res_dbase
                length=len(index)
                #print "length is",length
    
            sorted_res = []
            count=0
            for x in index:
                tup=[]
                tup=list(tup)
                tup.append(x)
                tup.append(res_dbase[count])
                #print tup
                tup=tuple(tup)
                sorted_res.append(tup)
                del tup  
                count=count+1
                #print "count  = ",count,"\n",sorted_res
            print tabulate(sorted_res,headers = ['student name',subject+' marks'],tablefmt='orgtbl')

        
        elif subject == 'sub2':
            res_dbase=[]
            for x in index:
                res_dbase.append(str(dbase[x]['sub2']))
                #print res_dbase
                length=len(index)
                #print "length is",length

            sorted_res = []
            count=0
            for x in index:
                tup=[]
                tup=list(tup)
                tup.append(x)
                tup.append(res_dbase[count])
                #print tup
                tup=tuple(tup)
                sorted_res.append(tup)
                del tup  
                count=count+1
                #print "count  = ",count,"\n",sorted_res
            print tabulate(sorted_res,headers = ['student name',subject+' marks'],tablefmt='orgtbl')

    
        elif subject == 'sub3':
            res_dbase=[]
            for x in index:
                res_dbase.append(str(dbase[x]['sub3']))
                #print res_dbase
                length=len(index)
                #print "length is",length
    
            sorted_res = []
            count=0
            for x in index:
                tup=[]
                tup=list(tup)
                tup.append(x)
                tup.append(res_dbase[count])
                #print tup
                tup=tuple(tup)
                sorted_res.append(tup)
                del tup  
                count=count+1
                #print "count  = ",count,"\n",sorted_res
            print tabulate(sorted_res,headers = ['student name',subject+" marks"],tablefmt='orgtbl')

        else:
            print "The subject",subject," is not available"
    elif choice == 'q' or choice == 'quit':
        break
    else:
        print "please select opiton from below"
