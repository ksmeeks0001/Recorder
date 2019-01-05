#unschedule the keylogger and remove the files
#failure to remove a certain task/file will not stop script from
#removing the rest.
import os
import getpass
def undo():
    user = getpass.getuser() 
    try:
        os.system('schtasks /Delete /TN logkeys')
    except:
        pass

    try:
        os.system('del ' + "C:\\Users\\" + user + "\\keylogger.py")
    except:
        pass

    try:
        os.system('del ' + "C:\\Users\\" + user + "\\log.txt")
    except:
        pass

    
        
undo()
