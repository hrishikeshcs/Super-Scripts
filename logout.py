# A script to erase all cookies and therefore log out of all accounts 
# Change cookie paths to enable support for other browsers & operating systems
# Tested on Ubuntu 20.4  | Chromium Version 85.0.4183.121
# By getcake (https://github.com/getcake)

import platform 
import os 

def logout():
    if platform.system().lower() == 'linux':
        browser_type = input("""Which of the following browsers do you use?
                                1) Firefox
                                2) Chrome
                                3) Chromium
                                > """)
        if browser_type == "1":
            profile_string = input('Please enter your random profile string from ~/.mozilla/firefox/\n > ')
            cookie_path = os.path.expanduser('~/.mozilla/firefox/')
            cookie_path = os.path.join(cookie_path, profile_string + "/cookies.sqlite")
            if os.path.isfile(cookie_path) == True:
                print('true', cookie_path)
                os.system('rm {}'.format(cookie_path))
                if os.path.isfile(cookie_path) == False:
                    print("Successfully deleted cookies")           
                else:
                    print("Failed to delete cookies")
            else:
                print(cookie_path)
                print("Not a valid directory 1")

        elif browser_type == "2":
            cookie_path = '~/.config/google-chrome/Default/Cookies'
            if os.path.isfile(cookie_path) == True:
                os.system('rm {}'.format(cookie_path))
                if os.path.isfile(cookie_path) == False:
                    print("Successfully deleted cookies ")
                else:
                    print("Failed to delete cookies")
            else:
                print("Not a valid directory")
        
        elif browser_type == "3":
            cookie_path = '~/.config/chromium/Default/Cookies'
            if os.path.isfile(cookie_path) == True:
                os.system('rm {}'.format(cookie_path))
                if os.path.isfile(cookie_path) == False:
                    print("Successfully deleted cookies")
                else:
                    print("Failed to delete cookies")
            else:
                print("Not a valid directory")
logout()


