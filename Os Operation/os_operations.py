import time
import datetime
import os, sys, traceback
import shutil
global usr_dir,file_name
def time_operations():
    print time.strftime(" current time is %I:%M:%S %p")
    return
def date_operations():
    now = datetime.datetime.now()
    print "day :",now.day,"("+time.strftime("%A")+")"
    print "month :",now.month,"("+time.strftime("%B")+")"
    print "year :",now.year
    return
def dir_operations():
    global usr_dir,file_name
    print "this is your current directory :",os.getcwd()
    usr_dir = raw_input("Enter the directory you want to surf(enter y to go with same dir)")
    if usr_dir == 'y':
        usr_dir = os.getcwd()
    while True:
        print "-----------------------------------------------------------------------------"
        choice =input("choose one (as number)\n1.list available dirs\n2.open files \n3.close files \n4.create dirs\n5.remove dirs\n6.change directory\n7.zipping dirs\n8.quit\n")
        if choice == 1:
            for x in os.listdir(usr_dir):
                print x
        elif choice == 2:
            file_name  = raw_input("entetr the name of file to be open...")
            #os.system("start"+file_name)
            os.startfile(usr_dir+'/'+file_name,'open')
        elif choice == 3:
            app_name =raw_input("enter the name of application to be closed...")
            os.system("Taskkill /IM "+app_name+".exe")
            """try:
                killed = os.system('tskill'+file_name)
            except Exception, e:
                killed = 0"""
    
        elif choice == 4:
            os.chdir(usr_dir)
            new_dir = raw_input("enter the directory name to be created...")
            os.makedirs(usr_dir+"/"+new_dir)
            print "dir created sucessfully"
        elif choice == 5:
            os.chdir(usr_dir)
            new_dir = raw_input("enter the directory name to be deleted...")
            shutil.rmtree(usr_dir+"/"+new_dir)
        elif choice == 6:
            #global usr_dir
            usr_dir = raw_input("enter the new directory to surf(start from drive letter)...")
            os.chdir(usr_dir)
        elif choice == 7:
            base_name = raw_input("enter the output fil name...")
            root_dir = raw_input("enter the directory file to be archived...(use forward slashs(/))")
            base_dir = root_dir
            while base_dir[-1]!='/':
                base_dir=base_dir[:-1]
            shutil.make_archive(base_dir+'/'+base_name,'zip',root_dir)
        elif choice == 8:
            break
            
while True:
    x = input("1.To see date and time\n2.To perform Dir operatoin\n3.Quit\n")
    if x == 1:
        date_operations()
        time_operations()
    elif x == 2:
        dir_operations()
    elif x == 3:
        print "\n process completed"
        break
    


