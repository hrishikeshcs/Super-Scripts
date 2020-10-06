'''
This script is meant to keep a user's system awake (prevent it from going to sleep, useful for keeping workplace's skype status availaibility lol)
by constantly providing automatic key input from the "DOWN" key of the user's keyboard.
'''
import time
import keyboard                             # We will need to install this lib via pip first. Use command "pip3 install keyboard"

print(' ')
print('--------------------------------------------------')
print('This script will keep your UNIX/Linux system awake')
print('--------------------------------------------------')
print(' ')

duration = input(
    'How long do you need the screen to remain awake? (in minutes) : ')

print(' ')
print('Note : Please press ctrl+c to stop execution manually.')
print(' ')
print('Now Running...')

time_end = time.time() + 60 * int(duration) # This line of code allows the input of time duration in minutes.

try:
    while time.time() < time_end:
        keyboard.KEY_DOWN
except KeyboardInterrupt:                   # This will keep the unwanted error hidden. 
    print(' ')
    print('Stopped by user! Exiting...')
    print(' ')

print('Execution finished!')
print(' ')
