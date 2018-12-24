# keylogger
DISCLAIMER: 
  This is code is meant to be used for personal use only. Any one using this code is responsible for any and all uses.
  This was not meant to be used for malicious or illegal purposes and anyone who does such is responsible for their own actions. 



logdemo.py: 
    Everything typed is logged locally and optionally to your
own email adress. This Demo logs what you type to a log.txt
In order to stop it press ctrl+c then check the log.txt file
If you want to have logs sent to your email run following command 
python logdemo.py your@gmail.com password
check your smtp settings for non gmail 
The log.txt is read/emailed/erased every 15 mins. To change the time replace the number 900 with any amount of seconds you would like.

logdemo.exe:
  Used auto-py-to-exe to create windows executable file. 
  Works exactly like logdemo.py, also accepts command line arguments for email.
  Must open task manager and end the task in order to stop the process.

keylogger.py: (only works on windows)
  The main functionality is exactly the same as the demo.
  The difference is that this code makes a copy of itself, and uses windows command to schedule itself at a one minute interval. By
  default task scheduler will not start the process again if it is still runnning. So scheduling it for every minute is just a way to
  ensure you are always recording. You must set variables with your email address and password in the send function. This is because this
  script is meant to be converted with auto-py-to-exe. The user can then start logging from keyboard just by executing the .exe and the 
  log will always be running and the user of computer would never know. (python does not need to be installed to run the exe) After adding your email and password if you decide to convert to exe (recommended) before converting be sure to change the '.py' inside the file to '.exe' or it will not work properly. 
After running the keylogger.py in order to stop the process you must open task scheduler and delete the scheduled task. Use task manager to end the process. (will likely be under background processes) and also delete the copy it made of itself in C:\Users\<user that ran>
If you do not delete the copy it made of itself it will not schedule itself to run again becuase this is what it checks to determine if it has been ran previously or not.

TO DO: 
write a scipt that automates the deletion of the copy, the removal of the scheduled task, and ensures that you are not being logged.

Create an executable version that can accept different argument such as:
email and password
email interval time
uninstall and delete time so that a computer can be logged for a certain amount of time completely unnoticed and then all evidence of the program self erase.



