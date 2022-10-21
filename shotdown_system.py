#shotdown system in python :
import os
import pyautogui
shotdown = input('do you want your off loptop (yes / no) ')
if shotdown == 'yes' :
    os.system('shutdown /s /t 1')
else :
    pyautogui.alert("Ok your system is not turn off \U0001F914")
    print ('shotdown is not requested (:')    
