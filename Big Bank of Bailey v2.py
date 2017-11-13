userlist = open('userlist.txt','r+')
# Allows the program access to the list of users
username = str(input("Please enter your username (all lower case):"))
# Takes the users identification
x = 0
# Used in the actioncheck function
def accountcheck(username, x):
    # Checks to see if the user is registered on the system
    a = 0
    check = False
    for line in userlist:
        possible_users = userlist.readlines(line).replace('/n','')
    print(possible_users)
    for possible_user in possible_users:
        if possible_users[a] == username:
            user = open(username + '.txt','r+')
            pin = user.read(4)
            enterpin = input("Please enter your pin:")
            y = 0
            pincheck(pin, enterpin, username, y, user)
            check = True
        print(possible_user)
        print(username)
    if check == False:
        issue_action = int(input("Sorry, it does not appear that this account exists. Press 1 to retry, press 2 to make an account, press 3 to quit."))
        actioncheck(issue_action, x)
        a += 1
def actioncheck(action, x):
    if x < 2:
        if action == 1:
            x = x + 1
            accountcheck(username, x)
        elif action == 2:
            accountmake()
        elif action == 3:
            quit()
        else:
            action = int(input("Only between 1 and 3 please!"))
            actioncheck(action)

def pincheck(pin, enterpin, username, y, user):
    if y != 3:
        if str(pin) == str(enterpin):
            print("Welcome back " + username )
            maintask(user)
        else:
            enterpin = str(input("Sorry, the pin you have entered is incorrect, please re-enter your pin."))
            y +=1
            pincheck(pin, enterpin, username, y, user)
    else:
        print("Apologies, but we are now locking this program. Good day.")
        #Add time check subroutine here
        #exit()

def maintask(user):
    user.seek(0)#
    user.readline()
    cash = user.readline()
    task = int(input("You are cleared for access. Press 1 to make a deposit. Press 2 to make a withdrawl. Press 3 to check your balance. Press 4 to set up a new account."))
    taskcheckruns = 0
    while taskcheckruns == 0:
        if task > 0 and task < 5:
            taskcheckruns = 1
        else:
            task = int(input("Please enter a number between 1 and 4."))
    if task == 1:
        deposit = int(input("Please enter the amount you wish to deposit."))
        cash += deposit
        print("Transaction complete.")
        save(cash, user)
    elif task == 2:
        withdrawl = int(input("Please enter the amount you wish to withdrawl"))
        cash -= withdrawl
        if account < 0:
            print("Sorry, but you do not have the balance neccesary to withdraw this amount of money.")
            cash += withdrawl
            save(cash, user)
        else:
            print("Transaction complete.")
            save(cash, user)
    elif task == 3:
            print("Ã‚Â£" + cash)
    else:
        accountmake()

def save(cash, user):
    code = user.read(4)
    line_list = [code, cash]
    for line in user:
        user.writeline(line_list[line])
    user.close()

def accountmake():
    users = []
    newusername = input("Please input the name you wish to be known by.")
    newuser = open(newusername + ".txt", "w")
    newuserpin = str(input("Now input the pin you wish to use."))
    line_list = [newuserpin, "0"]
    newuser.writelines(line_list)
    for line in userlist:
        users.append(line)
    users.append(newusername)
    for user in users:
        userlist.writeline(users[user])
    print("Your account has been created. Goood day.")
    userlist.close()
    newuser.close()
accountcheck(username, x)
userlist.close
exit()
