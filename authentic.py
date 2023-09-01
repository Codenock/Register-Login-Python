def register():
    db = open("database.txt", "r")
    Username = input("Create username:")
    Password = input("Create password:")
    Password1 = input("Confirm password:")
    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    if Password != Password1:
        print("Passwords don't match, restart")
        register()
    else:
        if len(Password)<=6:
            print("Password too short, restart:")
            register()
        elif Username in d:
            print("Username already exists")
            register()
        else:
            db = open("database.txt", "a")
            db.write(Username+", "+Password+"\n")
            print("Success!")



def access():
    db = open("database.txt", "r")
    Username = input("Enter username:")
    Password = input("Enter password:")

    if not len(Username or Password)<1:
        d = []
        f = []
        for i in db:
            a,b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print("Login success")
                        print("Hi,", Username)
                    else:
                        print("Username or Password incorrect")
                except:
                    print("Incorrect Password or Username")
            else:
                print("Username or Password doesn't exist")
        except:
            print("Username or Password doesn't exist")
    else:
        print("Please enter a value")

def home(option=None):
    option = input("Login | Signup:")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Please enter an option")
home()