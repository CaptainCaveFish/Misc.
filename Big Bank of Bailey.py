import pickle
import os
def accountcheck():
    username = str(input("Please enter your username."))
    if os.path.exists(username + '.p'):
        username = str(username + '.p')
        userfile = open(username, 'rb')
        user = pickle.load(userfile)
        pincheck(user)
        pickle.dump(user, user)
        user.close
    else:
        action = int(input("Sorry, that username does not appear to exist. Press 1 to retry, press 2 to make a new account, press 3 to quit."))
        actioncheck(action)
def actioncheck(action):
    if action == 1:
        accountcheck()
    elif action == 2:
        accountmake()
        user.close
    elif action == 3:
        user.close
        quit()
    else:
        action = int(input("Only between 1 and 3 please!"))
        actioncheck(action)
def pincheck(user):
    runs = 0
    clear = 0
    pin = str(input("Please enter your pin."))
    while runs < 2:
        if pin == user[1]:
            print("Welcome back," + str(user[0]))
            runs = 2
            clear = 1
            maintask(usernum)
        else:
            pin = str(input("Sorry, the pin you have entered is incorrect, please re-enter your pin."))
            runs = runs + 1
            clear = 1
    if clear == 0:
        print("Apologies, but we are now locking this program. Good day.")
        #Add time check subroutine here
        #exit()
def maintask(usernum):
    task = int(input("Press 1 to make a deposit. Press 2 to make a withdrawl. Press 3 to validate your account. press 4 to set up a new account."))
    taskcheckruns = 0
    while taskcheckruns == 0:
        if task == 1:
            deposit = int(input("Please enter the amount you wish to deposit."))
            user[2] = user[2] + deposit
            print("Transaction complete.")
        elif task == 2:
            withdrawl = int(input("Please enter the amount you wish to withdrawl"))
            user[2] = user[2] - withdrawl
            if int(user[2]) < 0:
                print("Sorry, but you do not have the balance neccesary to withdraw this amount of money.")
                user[2] = user[2] + withdrawl
        elif task == 3:
            print(user[2])
        elif task == 4:
            accountmake()
        else:
            task = int(input("Please enter a number between 1 and 4."))

def accountmake():
    newuser = []
    newusername = input("Please input the name you wish to be known by.")
    newuserpin = input("Now input the pin you wish to use.")
    newuser = [newusername, newuserpin, 0]
    a = (open(newusername + '.p', 'wb'))
    pickle.dump(newuser, a)
    a.close
    accountcheck()
accountcheck()
