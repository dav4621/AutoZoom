# AutoZoom
# John Davis

# Supported Platforms: Windows, macOS
# I included the code for the script to run on a Linux distrobution, however it won't work. Scrot needs to be installed for the screenshots to be recognized, and Scrot depends on a module called Pillow. However, in Debian distros (Red Hat distros don't even support scrot) there's a bug within Pillow where jpg and png images are not supported. There was no consistent fix that is currently available.

# Use version 5.0.1, some of the buttons have changed how they look

# Dependencies needed (installed through pip):
#   - pyautogui
#   - darkdetect

import pyautogui                # library for system gui functions
import os                       # library to write shell commands in a python script
import platform                 # used to determine user platform
from pymsgbox import prompt     # used to allow user to input necessary information
from pymsgbox import confirm
import time                     # used to handle time operation
from datetime import datetime   # !!
import darkdetect               # will check for dark mode on macOS

pyautogui.failsafe = True       # so it doesn't mess up

# Initial alert prompt
Alert = confirm(text='BEFORE RUNNING, best if used on a 1080p display. Other resolutions may currently xcause trouble.\nMake sure these options are checked in the video and audio settings:\n-"Turn off my video when joining a meeting"\n-"Mute microphone when joining a meeting"\nClick Cancel in promps to quit program', title='Attention', buttons=['OK', 'Cancel'])
if Alert == 'Cancel':       # if cancel is pressed, quits program
    exit()

# saves link to access zoom lobby
link = prompt(text='Enter the Meeting ID or the numbers at the end of your zoom join link\nExample: https://calu.zoom.us/j/867530999 should enter 867530999:', title='Enter url', default='')
if link == None:
    exit()                  # if cancel is pressed, quits program

# creates time object to compare to system clock
StartTime = prompt(text='enter the start time of your class as "Month Day Year HH:MMam/pm"\nExample: June 15 2020 12:30pm', title='Start Time', default='')
if StartTime == None:   # if cancel is pressed, quit program
    exit()
else:
    StartTime_obj = datetime.strptime(StartTime, '%B %d %Y %I:%M%p')
    print('StartTime_obj =')
    print(StartTime_obj)

# creates time object to compare to system clock
EndTime = prompt(text='enter the end time of your class as "Month Day Year HH:MMam/pm"\nExample: June 15 2020 12:30pm', title='End Time', default='')
if EndTime == None:     # if cancel is pressed, quit program
    exit()
else:
    EndTime_obj = datetime.strptime(EndTime, '%B %d %Y %I:%M%p')
    print('EndTime_obj =')
    print(EndTime_obj)

run_prog = False
# keeps program in a waiting state until proper time
while run_prog == False:
    if datetime.today() >= StartTime_obj:
        run_prog = True
        time.sleep(1)

# once unlocked, will begin automation
# launches zoom based on platform
if run_prog == True:
    # will launch zoom on platform being used
    if platform.system() == 'Darwin':
        os.system('open -a "zoom.us"')
    elif platform.system() == 'Linux':
        os.system('zoom')   # ignore terminal verbose (could be virtual machine specific)
    elif platform.system() == 'Windows':
        pyautogui.press('winleft')  # can't launch from cmd/powershell since zoom is installed under %AppData%
        pyautogui.write('zoom')
        pyautogui.press('enter')

# click the join button, and enter the lobby data
if platform.system() == 'Darwin':   # for macOs
    time.sleep(5)   # 5 second delay to ensure that commands aren't executed before the program actually loads
    if darkdetect.theme() == 'Dark':
        initJoin = pyautogui.locateOnScreen('ZoomInitJoinMacDark.png')
    else:
        initJoin = pyautogui.locateOnScreen('ZoomInitJoinMacLight.png')
    pyautogui.click(initJoin)
    time.sleep(3)
    pyautogui.write(link)   # puts link into text area
    if darkdetect.theme() == 'Dark':
        joinMeeting = pyautogui.locateOnScreen('JoinMeetingMacDark.png')
    else:
        joinMeeting = pyautogui.locateOnScreen('JoinMeetingMacLight.png')
    pyautogui.click(joinMeeting)    # joins the meeting
    time.sleep(5)
    if darkdetect.theme() == 'Dark':
        joinMeeting2 = pyautogui.locateOnScreen('JoinWithComputerAudioMacDark.png')
    else:
        joinMeeting2 = pyautogui.locateOnScreen('JoinWithComputerAudioMacLight.png')
    pyautogui.click(joinMeeting2)

if platform.system() == 'Windows':  # for Windows
    time.sleep(5)
    initJoin = pyautogui.locateOnScreen('InitJoinWindowsLight.PNG')
    pyautogui.click(initJoin)
    time.sleep(3)
    pyautogui.write(link)   # puts link into text area
    joinMeeting = pyautogui.locateOnScreen('JoinMeetingWindows.PNG')
    pyautogui.click(joinMeeting)    # joins the meeting
    time.sleep(5)
    joinMeeting2 = pyautogui.locateOnScreen('JoinWithComputerAudioWindows.PNG')
    pyautogui.click(joinMeeting2)

if platform.system() == 'Linux':    # for linux (currently doesn't work due to Pillow dependency)
    time.sleep(3)
    initJoin = pyautogui.locateOnScreen('InitJoinLinux.png')
    pyautogui.click(initJoin)
    time.sleep(3)
    pyautogui.write(link)
    joinMeeting = pyautogui.locateOnScreen('JoinMeetingLinuxLight.png')
    pyautogui.click(joinMeeting)
    time.sleep(5)
    joinMeeting2 = pyautogui.locateOnScreen('JoinWithComputerAudioLinux.png')
    pyautogui.click(joinMeeting2)

# check for end time, then unlock
while run_prog == True:
    if datetime.today() >= EndTime_obj:
        run_prog = False
        time.sleep(2)

# leave the meeting
if platform.system() == 'Darwin':   # for macOs
    leaveMeeting = pyautogui.locateOnScreen('LeaveMeetingMac.png')
    pyautogui.click(leaveMeeting)
    time.sleep(2)
    if darkdetect.theme() == 'Dark':
        leaveMeeting2 = pyautogui.locateOnScreen('LeaveMeetingConfirmMacDark.png')
    else:
        leaveMeeting2 = pyautogui.locateOnScreen('LeaveMeetingConfirmMacLight.png')
    pyautogui.click(leaveMeeting2)
    time.sleep(1)
    pyautogui.keyDown('command')    # will cmd+Q out of zoom
    pyautogui.press('q')
    pyautogui.keyUp('command')

if platform.system() == 'Windows':  # for Windows
    leaveMeeting = pyautogui.locateOnScreen('LeaveMeetingWindows.PNG')
    pyautogui.click(leaveMeeting)
    time.sleep(2)
    leaveMeeting2 = pyautogui.locateOnScreen('LeaveMeetingConfirmWindows.PNG')
    pyautogui.click(leaveMeeting2)
    time.sleep(1)
    pyautogui.keyDown('alt')    # will alt+f4 out of zoom
    pyautogui.press('F4')
    pyautogui.keyUp('alt')

if platform.system() == 'Linux':    # for Linux (currently doesn't work due to Pillow dependency)
    pyautogui.keyDown('ctrl')       # the lobby controls at the bottom need to be set to always show by a ctrl+\
    pyautogui.press('\\')
    pyautogui.keyUp('ctrl')
    leaveMeeting = pyautogui.locateOnScreen('LeaveMeetingLinux.png')
    pyautogui.click(leaveMeeting)
    time.sleep(2)
    leaveMeeting2 = pyautogui.locateOnScreen('LeaveMeetingConfirmLinux.png')
    pyautogui.click(leaveMeeting2)
    time.sleep(1)
