
def singIngPage():

  while (True):
    name = input("Enter your Name: ")

    if (len(name) <= 8):
        print("Ok!")
    else:
        print("Get out")
        break;
    

    email = input("Enter your Email: ")
    
    if (len(email) <= 18):
        print("Thanks for your email?")
    else:
        print("GET OUT")
        break;
    

    password = input("Enter your Password: ")
    
    if (len(password) <= 8):
        print("Thanks for your password?")
    else:
        print("See you later?")
        break;

    confirm = input("do you like to confirm (Y/N): ")

    if (confirm == "Y"):
        print("You are been hacked!.He he heee!")
        print("Buy buy Tata he hee?")
    elif (confirm == "y"):
        print("You are been hacked!.He hehe heee!")
        print("Buy buy Tata he hee")
    elif (confirm == "N"):
        print("You are safe!")
    elif (confirm == "n"):
        print("You are Safe")
    break;



singIngPage()
