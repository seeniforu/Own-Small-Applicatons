from ast import Try
import os
import ctypes, sys
from threading import Thread

def DNS_Flush():
    os.system('cmd /c "ipconfig/flushdns"')

def Windows_Temp():
    os.system('cmd /c "del c:\Windows\Temp /f /s /q"')

def User_Temp():
    os.system('cmd /c "del /q/f/s %TEMP%\*"')


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    t1 = Thread(target=DNS_Flush)
    t2 = Thread(target=Windows_Temp)
    t3 = Thread(target=User_Temp)
    t1.start()
    t2.start()
    t3.start()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)



