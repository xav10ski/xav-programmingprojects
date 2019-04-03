"""    
#
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Code made for the Hanscom Composite Squadron Cyberpatriot Team!
-Xavier Wrenn
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
"""

import warnings
warnings.filterwarnings("ignore")
warnings.filterwarnings('ignore', category=SyntaxWarning)
global run_admin
run_admin = False
import os
import os.path
import time
import sys
import getpass
from shlex import split
from more import *
from time import gmtime, strftime
start_dir = os.getcwd()
current_user = getpass.getuser()
run_admin = False

pointless_services = ['iphlpsvc','Fax','tlntsvr','HomeGroupProvider','SSDPSRV','ehRecvr','ehSched','spoolsv','WPDBusEnum','wbengine','ProtectedStorage','NetTcpPortSharing','SCardSvr','NMIndexStoreSvr','TeaTimer','IoctlSvc','JUCheck','SynTPEnh','HKCMD','Reader_SL','ATI2evxx','ITunesHelper','NVSvc32']
pointlessNetServices = ['','','','','','']
#Above, list(s) of unneeded services.
admin_user = "administrator" #This is only tempory for setup purposes, it is re-assighned during setup by the user
""
def Compiler(filename):
    start = time.time()
    os.system("echo off")
    newname = str(filename[:(len(filename)-3)] + 'bat')
    if os.path.isfile(filename):

        #Setup Phase

        start_dir = os.getcwd()
        os.system('copy "' + filename + '" "' + current_root_dir() + '\\compiler\\temp" /y')
        os.chdir(current_root_dir() + '\\compiler\\temp')
        #Main Phase
        os.system('(echo from framework_scr import *)>scrob.py')
        os.system('>>scrob.py echo from framework_more import *')
        os.system("for /f \"tokens=*\" %i in ('type " + '"' + filename + '"' + "') do echo mainloop(\'%i\')>>scrob.py")
        os.system('start scrob.py')

        
        #Termination Phase CLEANUP
        while os.path.isfile("COMPILED.bat") == False:
            print('working...')
            time.sleep(0.2)
        os.system("del " + current_root_dir() + '\\compiler\\temp\\scrob.py /q')
        os.system("del " + filename + '/q')
        os.system("move /y COMPILED.BAT " + start_dir)

        os.chdir(start_dir)
        if os.path.isfile('COMPILED.bat'):
            os.system("rename COMPILED.bat " + '"' + newname +'"')
        os.system("echo on")
        end = time.time()
        print('Compilation Complete. Took ' + str(end-start) + ' seconds.')
        
    else:
        print('File doesn\'t exist.')
""

#
def current_root_dir():
    return(os.path.dirname(__file__))


def nuke_pointless():
    for service in pointless_services:
        service_remover(service)
        
def add_pointless(service_name):
    pointless_services.append(service_name)

def get(name):
    if name == 'Belarc' or name == 'BELARC' or name == 'belarc':        
        if os.path.isfile('%programfiles%\\Belarc\\BelarcAdvisor\\BelarcAdvisor.exe') == True:
            sudo("%programfiles%\\Belarc\\BelarcAdvisor\\BelarcAdvisor.exe")
        elif os.path.isfile('%programfiles(x86)%\\Belarc\\BelarcAdvisor\\BelarcAdvisor.exe') == True:
            sudo("%programfiles(x86)%\\Belarc\\BelarcAdvisor\\BelarcAdvisor.exe")
        else:
            sudo(current_root_dir() + "\\internals\\get-belarc.exe")
    elif name == 'malwarebytes' or name == 'mbam' or name == 'Malwarebytes':
        if os.path.isfile('%programfiles(x86)%\\Malwarebytes Anti-Malware\\mbam.exe'):
            sudo('%programfiles(x86)%\\Malwarebytes Anti-Malware\\mbam.exe')
        elif os.path.isfile('%programfiles%\\Malwarebytes Anti-Malware\\mbam.exe'):
            sudo('%programfiles%\\Malwarebytes Anti-Malware\\mbam.exe')
        else:
            sudo(current_root_dir() + '\\internals\\mbam-setup.exe')
        
def admin_remove(fake_admin):
    sudo('net localgroup Administrators ' + fake_admin + ' /delete')
    sudo('net localgroup "Power Users" ' + fake_admin + ' /delete')
    
def guest(boolean):
    if boolean == True or boolean == "true" or boolean == 'on' or boolean == 'On':
        sudo("net user guest /active:yes")
    elif boolean == False or boolean == "false" or boolean == 'off' or boolean == 'Off':
        sudo("net user guest /active:no")


def setup():
    try:
        import warnings
        warnings.filterwarnings("ignore")
        os.system("echo off")
        os.system("cls")
        os.system("title Cyberpatriot Command Prompt")
        os.system("color 1a")
        os.system("net localgroup administrators")
        global admin_user
        admin_user = raw_input("What is the Built-In Administrator's username?:")
        if admin_user == "":
            print("Not the valid admin username.")
            time.sleep(2)
            setup()
        elif admin_user == 'exit':
            __exit__()
        else:
            cv = "setup.exe " + admin_user
            os.system(cv)
        if os.path.isfile(current_root_dir() + "\\internals\\firewall-True.bat") == False:
            os.system('echo Netsh firewall set opmode enable > ' + current_root_dir() + '\\internals\\firewall-True.bat>nul')
            os.system('echo Netsh firewall set opmode disable > ' + current_root_dir() + '\\internals\\firewall-False.bat>nul')
        #os.chdir('C:\\users')
        if os.path.isfile(current_root_dir() + '\\internals\\history\\history.txt') == False:
            os.system('echo #> ' + current_root_dir() + '\\internals\\history\\history.txt')
        os.system('echo NEW SESSION ' + strftime("%m/%d/%y %H:%M:%S") +' >> ' + current_root_dir() + '\\tools\\pcinfo.txt')
        os.system('echo &#*($&*(#&*$*&(#$(*#$(*#@*($&*#$&(@$ >> ' + current_root_dir() + '\\tools\\pcinfo.txt')
        os.system('net user >>' + current_root_dir() + '\\tools\\pcinfo.txt')
        #os.system('net user >>' + current_root_dir() + '\\tools\\pcinfo.txt')
    except NameError:
        __exit__()
        
def __exit__():
    os.chdir(start_dir)
    cv = "exit.exe " + admin_user
    sudo(cv)
    os.system('cls')
    os.system("color 07")
    os.system('cls')
    exit()

def restart():
    os.chdir(start_dir)
    cv = "exit.exe " + admin_user
    os.system("cls")
    os.system('"' + os.path.realpath(__file__) + '"')
    __exit__()


def commands():
    os.system('cls')
    cmd = 'type "' + current_root_dir() + '\\help.txt" | more'
    os.system(cmd)

def ls_services_pointless():
    for x in pointless_services:
        print(x)
        
def failed():
    print("operation failed.")
    print("to ensure this script works:")
    print("You may find that the local Administrator account is in fact disabled.")
    print("Take a look in the Local Users and Groups in Computer Management.")
    print("then, enable the built-in administrator acount and run this script again.")

def sudo(cmd):
    com = 'runas /noprofile /env /savecred /user:%USERDOMAIN%\\' + admin_user + ' "' + cmd + '"'
    aba = os.system('runas /noprofile /env /savecred /user:%USERDOMAIN%\\' + admin_user + ' "' + cmd + '"')

def run(boolean):
    if boolean == True or boolean == "true" or boolean == 'on' or boolean == 'On':
        sudo("REG delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoRun /f")
    elif boolean == False or boolean == "false" or boolean == 'off' or boolean == 'Off':
        sudo("REG add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoRun /t REG_DWORD /d 1 /f")
    
def time_limits(): #sets time limits for all users
    sudo("for /F %i in ('net localgroup users') do net user %i /time:Monday-Friday,09:00-16:00")
    sudo("for /F %i in ('net localgroup administrators') do net user %i /time:Monday-Friday,09:00-16:00")
    sudo("for /F %i in ('net localgroup homeusers') do net user %i /time:Monday-Friday,09:00-16:00")
    sudo("net user " + current_user + " /time:all")
    #sudo("net user " + admin_user + " /time:all")
    
def service_remover(service_name):
    sudo('sc stop ' + service_name)
    sudo('sc config ' + service_name + ' start= disabled')
#    sudo('sc delete ' + service_name)

def service_adder(service_name):
    sudo('sc start ' + service_name)
    sudo('sc config ' + service_name + ' start= enabled')
#    sudo('sc delete ' + service_name)
    
def nuke_pointless():
    for service in pointless_services:
        service_remover(service)
        
def nuke_pointless_undo():
    for service in pointless_services:
        service_adder(service)

def remove_int():
    print("user remover...")
    print("enter each username to remove then press enter:")
    while True:
        try:
            inpt = raw_input("user (CTRL-C to exit)::")
            if inpt == "":
                continue
            else:
                userremove(inpt)
        except KeyboardInterrupt:
            print
            break
        
"""def snapin_int():# hopefully, when and if I make a command compiler, interactive fetures like one this wont be there. -Wrenn
    while 1:
        break"""

def snapin_add(name):
    if os.path.isfile(current_root_dir() + '\\internals\\snapins\\' + name):
        os.system(current_root_dir() + '\\internals\\snapins\\' + name)
    elif os.path.isfile(current_root_dir() + '\\internals\\snapins\\' + name + '.msc'):
        os.system(current_root_dir() + '\\internals\\snapins\\' + name + '.msc')
    else:
        print('Snap-in not found. See the folder "\\internals\\snapins" for available snap-ins, or use mmc.exe to create one.')
        
    #Default names are to be snapin, snapin1, snapin2, etc. use mmc.exe > CTRL + M >  to make custom snapins


def cd(dirt):
    try:
        os.chdir(dirt)
    except WindowsError:
        print('can\'t switch to that directory. Sowy.')
    """if dirt == '.':
        os.chdir('.')
    elif dirt == '..':
        os.chdir('..')
    elif dirt.find(' ') != -1:
        toswitch = '"' + str(dirt) + '"'
        print(toswitch)
        try:
            os.chdir(dirt)
        
    else:
        os.chdir(dirt)"""

def firewall(boole):
    if boole == "true" or boole == True or boole == 'on' or boole == 'On' or boole == 'enabled' or boole == 'Enabled':
        sudo(start_dir + "\\internals\\firewall-True.bat")
    elif boole == "false" or boole == False or boole == 'off' or boole == 'Off' or boole == 'disabled' or boole == 'Disabled':
        sudo(start_dir + "\\internals\\firewall-False.bat")
        

def userremove(usr):
    sudo('net user ' + usr + ' /delete')
    
def input_mainloop():
    global run_admin
    head = 'in ' + os.getcwd() + '> '
    todo = raw_input(head)
    todo = todo.lower()
    mainloop(todo)

def search(words):
    search_command = 'dir %systemdrive%\\ /s /b'
    search_command_h = 'dir %systemdrive%\\ /s /b /a:h'
    if words.find(" ") == -1:#no space
        os.system(search_command + ' | find /i "' + words + '"')
        os.system(search_command_h + ' | find /i "' + words + '"')
        
    elif words.find(" ") != -1:#found space
        word_list = split(words)
        for word in word_list:
            search_command = search_command + ' | find /i "' + word + '"'
            search_command_h = search_command_h + ' | find /i "' + word + '"'
        os.system(search_command)
        os.system(search_command_h)

def search_here(words):
    search_command = 'dir /s /b'
    search_command_h = 'dir /s /a:h /b'

    if words.find(" ") == -1:#no space
        os.system(search_command + ' | find /i "' + words + '"')
        os.system(search_command_h + ' | find /i "' + words + '"')
        
    elif words.find(" ") != -1:#found space
        word_list = split(words)
        for word in word_list:
            search_command = search_command + ' | find /i "' + word + '"'
            search_command_h = search_command_h + ' | find /i "' + word + '"'
        os.system(search_command)
        os.system(search_command_h)

#"""
#
#NEW FUNCTIONS BELOW HERE
#
#"""

        


#"""
#
#NEW FUNCTIONS ABOVE HERE
#
#"""

def rename_user(old, new):
    if sudo("wmic useraccount where name='" + old + "' rename " + new) == 1:
        os.system("echo there may have been an error")
        
def disable_user(user):
    sudo("net user " + user + " /active:no")
    
def mainloop(_input_):
    global run_admin
    pwd = os.getcwd()
    head = 'in ' + pwd + '> '
    todo = _input_#    todo = raw_input(head)
    todo = todo.lower()
    os.system('>>' + current_root_dir() + '\\internals\\history\\history.txt echo ' + todo)
    #end1 = todo.find('| ')

    if todo == "" and run_admin == True:
        input_mainloop()
    
    elif todo == 'commands':
        commands()
    elif todo == 'history':
        os.system('notepad' + current_root_dir() + '\\internals\\history\\history.txt')

    elif todo == 'belarc' or todo == 'BELARC':
        if os.path.isfile('%programfiles%\\Belarc\\BelarcAdvisor\\BelarcAdvisor.exe') == True:
            sudo("%programfiles%\\Belarc\\BelarcAdvisor\\BelarcAdvisor.exe")
        elif os.path.isfile('%programfiles(x86)%\\Belarc\\BelarcAdvisor\\BelarcAdvisor.exe') == True:
            sudo("%programfiles(x86)%\\Belarc\\BelarcAdvisor\\BelarcAdvisor.exe")
        else:
            sudo(current_root_dir() + "\\internals\\get-belarc.exe")

    elif todo == 'malwarebytes' or todo == 'Malwarebytes':
        if os.path.isfile('%programfiles%\\Malwarebytes Anti-Malware\\mbam.exe') == True:
            sudo("%programfiles%\\Malwarebytes Anti-Malware\\mbam.exe")
        elif os.path.isfile('%programfiles(x86)%\\Malwarebytes Anti-Malware\\mbam.exe') == True:
            sudo("%programfiles(x86)%\\Malwarebytes Anti-Malware\\mbam.exe")
        else:
            get('malwarebytes')

    elif todo[:7] == 'snapin ':
        if todo == 'snapin ':
            print('To view addable snap-ins (addons), see internals\\snapins.')
            print('Default, recommended snap-in to add is named "snapin.msc"')
            print('USAGE:')
            print('snapin [snap-in_name_to_add]')
            print('To create a snap-in, type mmc.exe.')
            
        elif todo.find('/?') == -1:
            snapin_add(todo[7:])
        elif todo[8] == '' or todo == 'snapin ':
            print('To view addable snap-ins (addons), see internals\\snapins.')
            print('Default, recommended snap-in to add is named "snapin.msc". type "snapin snapin.msc" to enable it.')
            print('USAGE:')
            print('snapin [snap-in_name_to_add]')
            print('To create a snap-in, type mmc.exe.')
        else:
            print('To view addable snap-ins (addons), see internals\\snapins.')
            print('Default, recommended snap-in to add is named "snapin.msc"')
            print('USAGE:')
            print('snapin [snap-in_name_to_add]')
            print('To create a snap-in, type mmc.exe.')

    elif todo[:7] == 'search ':
            search(todo[7:])
    elif todo[:9] == 'searchcd ':
            search_here(todo[9:])
    
    #REMOVE THIS FOR COMPILER
    elif todo == "remove." or todo == 'remove...':
        userremove_int()

    elif todo == 'exit':
        __exit__()

    elif todo == 'ls services':
        aba = os.system('sc query type= service state= all | find "SERVICE_NAME"')
        os.system('sc query type= service state= all | find "SERVICE_NAME"')

    elif todo == 'view contents':
        if os.path.isfile(current_root_dir() + '\\CyberpatHelper.py'):
            os.system('type CyberpatHelper.py')
        else:
            print('Source unable to be found. Please consult the developers to obtain source.')

    elif todo == "time-lim":
        time_limits()

    elif todo[:4] == 'get ':
        get(todo[4:])

    elif todo[:9] == "firewall ":
        firewall(todo[9:])

    elif todo == "ls services-pointless":
        ls_services_pointless()        

    elif todo[:4] == 'run ' or todo[:4] == 'Run ':
        run(todo[4:])

    elif todo == "nuke pointless":
        print("Disabling and shutting down pointless tasks...")
        print("to view pointless tasks type 'ls services-pointless'")
        for service in pointless_services:
            service_remover(service)
        print("if you can see this message then you did not get blue-screened. Good work developers! :)")


    elif todo == "nuke pointless -undo":
        print("undoing the damage! :)")
        for service in pointless_services:
            service_adder(service)

    elif todo == "remove...":
        userremove_int()
        


    elif todo == 'cm':
        global admin_user
        if run_admin == False:
            run_admin = True
            print('Will now run commands as admin. Type "cmd" to run administrator command prompt.')
            #mainloop()
        else:
            run_admin = False
            print("will now run as normal user")
            #mainloop()

    elif todo == "restart":
        restart()

    elif todo[:5] == 'nuke ':
        if todo[(len(todo)-2):] == "-r":
            service = todo[5:]
            service = service[:(len(service)-2)]
            service_remover(service)
            sudo('sc delete ' + service)
        else:
            service_remover(todo[5:])
            
    elif todo[:14] == "add-pointless ":
        service_name = todo[14:]
        add_pointless(service_name)
        
    elif todo == "pw-pol":
        sudo("net accounts /minpwage:10 /maxpwage:30 /forcelogoff:5 /minpwlen:8 /uniquepw:5 /domain")
        sudo("net accounts /minpwage:10")
        sudo("net accounts /maxpwage:30")
        sudo("net accounts /forcelogoff:5")
        sudo("net accounts /minpwlen:8")
        sudo("net accounts /uniquepw:5")
    elif todo == 'nuke':
        print("usage: nuke [<service name> OR pointless] .")

    elif todo[:12] == 'user-rename ':
        try:            
            cmd = todo[12:]
            if cmd.find(' ') != -1:
                old = cmd[:cmd.find(' ')]
                new = cmd[cmd.find(' ')+1:]
                rename_user(old, new)
            elif cmd.find(' ') == -1 or len(old) == 0 or len(new) == 0:
                os.system("echo Error: command must be rename-user [old] [new]")
        except IndexError:
            os.system("echo Error: command must be rename-user [old] [new]")

    elif todo[:12] == "user-remove ":
        pointless_user = todo[12:]
        userremove(pointless_user)

    elif todo[:13] == "user-disable ":
        disable_user(todo[13:])

    
    
    elif todo[:10] == 'not-admin ':
        fake_admin = todo[10:]
        sudo('net localgroup Administrators ' + fake_admin + ' /delete')
        sudo('net localgroup [Power Users] ' + fake_admin + ' /delete')

    elif todo[:6] == "guest ":
        boolean = (todo[6:])
        guest(boolean)
    elif todo[:3] == "cd ":
        cd(todo[3:])
    elif todo == 'start cmd' and run_admin == True:
        sudo('cmd')

    elif todo[:(len('compiler '))] == 'compiler ':
        Compiler(todo[(len('compiler ')):])
        #compiler <filename>
    
    #"""
    #
    #NEW FUNCTIONS BELOW HERE
    #
    #"""
    

 
        
    #"""
    #
    #NEW FUNCTIONS ABOVE HERE
    #
    #"""
    
    else:
        if run_admin == True:
            cmd = 'runas /noprofile /env /savecred /user:%USERDOMAIN%\\' + admin_user + ' "' + todo + '"'
            os.system(cmd)
        elif run_admin == False:
            os.system(todo)
        

try:
    setup()
    print('type "commands" for help')
    while True:
        input_mainloop()
except KeyboardInterrupt:
    __exit__()
