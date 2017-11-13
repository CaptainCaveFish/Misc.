import pickle
import os
def accountcheck():
    username = input("Please enter your username (all lower case):")
    if os.path.exists(username + ".p"):
        user = pickle.load(open(username + ".p" , "rb"))
        pin = user[0]
        print("Welcome back " + username )
        enterpin = input("Please enter your pin:")
        pinchecks = 0
        pincheck(pin, enterpin, user, pinchecks, username)
    else:
        action = int(input("Sorry, it does not appear that this account exists. Press 1 to retry, press 2 to make an account, press 3 to quit."))
        checks = 0
        actioncheck(action, checks)
def actioncheck(action, checks):
        if action == 1:
            checks += 1
            accountcheck(username)
        elif action == 2:
            accountmake()
        elif action == 3:
            quit()
        else:
            action = int(input("Only between 1 and 3 please!"))
            actioncheck(action, checks)

def pincheck(pin, enterpin, user, pinchecks, username):
    if pinchecks < 3:
        if int(pin) == int(enterpin):
            maintask(user, pin, username)
        else:
            enterpin = int(input("Sorry, the pin you have entered is incorrect, please re-enter your pin."))
            pinchecks +=1
            pincheck(pin, enterpin, user, pinchecks)
    else:
        print("Apologies, but we are now locking this program. Good day.")
        #Add time check subroutine here
        #exit()

def maintask(user, pin, username):
    cash = user[1]
    task = int(input("You are cleared for access. Press 1 to make a deposit. Press 2 to make a withdrawl. Press 3 to check your balance. Press 4 to set up a new account."))
    taskchecks = 0
    if task == 1:
        deposit = int(input("Please enter the amount you wish to deposit."))
        cash += deposit
        print("Transaction complete.")
        save(cash, pin, username)
    elif task == 2:
        withdrawl = int(input("Please enter the amount you wish to withdrawl"))
        cash -= withdrawl
        if account < 0:
            print("Sorry, but you do not have the balance neccesary to withdraw this amount of money.")
            cash += withdrawl
            save(cash, pin, username)
        else:
            print("Transaction complete.")
            save(cash, pin, username)
    elif task == 3:
            print("£" + str(cash))
    elif task == 4:
        accountmake()
    else:
        task = int(input("Only between 1 and 4, please."))
        maintask(user, pin, username)

def save(cash, pin, username):
    userstuff = [pin, cash]
    pickle.dump(userstuff, open(username + '.p', 'wb'))


def accountmake():
    newusername = str(input("Please input the name you wish to be known by."))
    newuserpin = str(input("Now input the 4 digit pin you wish to use."))
    newuserstuff = [newuserpin, 0]
    pickle.dump(newuserstuff, open(newusername + '.p', 'wb'))
    print("Your account has been created. Goood day.")
accountcheck()
exit()
