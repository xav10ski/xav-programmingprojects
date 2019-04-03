#title: functions.py
import getpass
import os
import sys
import time
from temp import *
try:
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
except ImportError:
    print('could not import RPi.GPIO')

user = getpass.getuser()
a_user_inputq = False
path = os.path.realpath('rover.py')

for x in range (0, 31):
    try:
        GPIO.setup(x, GPIO.OUT)
    except ValueError:
        print('pin ' + pin + ' isnt valid.')

def import_rpi():
    try:
        import RPi.GPIO as GPIO
    except ImportError:
        install = raw_input('module RPi.GPIO not found, attempt install? (y/n) >> ')
        if install == 'y' or install == 'yes':
            os.system('sudo apt-get install python-rpi.gpio')
            os.system('sudo python rover.py')
            exit()
            try:
                import RPi.GPIO as GPIO
            except ImportError:
                print('module unable to be found/added. sorry.')
def RPi_NameError():
    install = raw_input('module RPi.GPIO not found, attempt install? (y/n) >> ')
    if install == 'y' or install == 'yes':
        os.system('sudo apt-get update')
        os.system('sudo apt-get install python-dev')
        os.system('sudo apt-get install python-rpi.gpio')
    try:
        import RPi.GPIO as GPIO
    except ImportError:
        print('module unable to be found/added. sorry.')

def helps():
    print
    print('COMMANDS...')
    print
    print('commands     : displays this screen')
    print('credits      : displays credits')
    print('commands -r  : displays rover commands')
    print('a mode       : advanced mode')
    print('os [command] : run system command')
    print('restart      : restart script')
    print
def rovhelp():
    print
    print('ROVER COMMANDS:')
    print
    print('w    : move forwards')
    print('s    : move backwards')
    print('a    : face left')
    print('d    : face right')
    print('ss   : face backwards')
    print
def a_commands_help():
    print
    arc = 'Advanced Rover Commands:'
    arc = arc.upper()
    print(arc)
    print
    print('a commands   | Display this Screen')
    print('commands     | Display this Screen')
    print('cm           | Change mode (to regular commands)')
    print('restart      | restart rover.py')
    print('temp         | view system temperature')# NEW A COMMAND
    print('pintest      | test individual GPIO pins with "on (PIN NUM)')    # NEW A COMMAND
    # NEW A COMMAND
    # NEW A COMMAND
    print('all other commands go through regular command mode.')
    print('for regular commands, type "commands" ')
    print('')
                    
def go_backward(tm): #was go_backward, changed
    try:
        #GPIO python code, setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(tm) #goes forawrd for amt of time
        GPIO.output(18, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        print('...done.')
        #possibly take photo and show on screen? if photomode is on...
    except NameError:
        RPi_NameError()

def go_forward(tm):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(1.5) #goes back for amt of time
    GPIO.output(17, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    print('...done.')
    #possibly take photo and show on screen? if photomode is on...
def face_left():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(1) #left for 1 sec
    GPIO.output(17, GPIO.LOW)
    print('...done.')
    #possibly take photo and show on screen? if photomode is on...
def face_right():
    #GPIO python code, 
    #set the pin
    #activate pin to FACE RIGHT
    #deactivate the pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(1) #goes right for amt of time
    GPIO.output(4, GPIO.LOW)
    print('...done.')
    #possibly take photo and show on screen? if photomode is on...
def face_about():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(4, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(2) #goes right for amt of time
    GPIO.output(4, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    print('...done.')
    
    print('...done.')
    #possibly take photo and show on screen? if photomode is on...

def restart():
    os.system("sudo python rover.py")











    
def rover_do(com):
    if com == 'forward' or com[:1] == 'w' or com == 'forward march':
        go_forward(3)
    elif com == 'backward' or com[:1] == 's' or com == 'to the rear march' or com == 'backwards':
        go_backward(1)
    elif com == 'left' or com[:1] == 'a' or com == 'left face':
        face_left()
    elif com == 'right' or com[:1] == 'd' or com == 'right face':
        face_right()
    elif com == 'about' or com[:1] == 'ss' or com == 'about face':
        face_about()
    elif com[:8] == 'commands':
        helps()
    elif com[:8] == 'commands' and com[9:] == '-r':
        rovhelp()
    elif com == 'a mode' or com == 'cm':
        global a_user_inputq
        a_user_inputq = True
        #break
    elif com[:2] == 'os':
        le = len(com)
        com = com[3:]
        os.system(com)
    elif com[:7] == 'restart':
        os.system(path)
    #if a_user_inputq == True:
        #break
    elif com == 'a commands':
        a_commands_help()
    elif com == 'exit':
        sys.exit('exiting...')
        exit()
    elif com == 'help':
        helps()













        
def user_input():
    while True:
        global a_user_inputq
        com = raw_input(' << Rover Command >> ') #com will be the command to be given to the car
        if com[:8] == 'commands' and com[9:] == '-r':
            helps()
            rovhelp()
        elif com[:8] == 'commands':
            helps()
        elif com == 'a mode' or com == 'cm':
            global a_user_inputq
            a_user_inputq = True
            break
        elif com[:2] == 'os':
            le = len(com)
            com = com[3:]
            os.system(com)
        elif com[:7] == 'restart':
            os.system(path)
        elif a_user_inputq == True:
            break
        elif com == 'a commands':
            a_commands_help()
        else:
            rover_do(com)

def a_do(com):
    #commands to do, in advneced scripting mode
    #print('mode not yet developed...')
    if com == 'restart':
        restart()
    elif com == 'cm':
        global a_user_inputq
        a_user_inputq = False
    elif com == 'acommands':
        a_commands_help()
    elif com == "temp":
        print(temp())
    elif com == 'pintest':
        os.system('sudo python pintest.py')
    #if com == connection-speed:
        #ping.......
        
    #if com == 'script':
    #
    else:
        rover_do(com)

    
def a_user_input():
    print('type acommands for help')
    while a_user_inputq == True:
        com = raw_input(' << Advanced Rover Commands >> ')
        
        a_do(com)
        if a_user_inputq == False:
            break
    
def mainloop():
    while True:
        user_input()
        a_user_input()
