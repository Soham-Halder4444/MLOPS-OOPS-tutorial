class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()
    def menu(self):
        user_input=input("""Welcome chatbook !! How would you like to proceed ?
                            1.Press 1 to Signup
                            2.Press 2 to signin
                            3.Press 3 to write a post
                            4.Press 4 to messege a friend
                            5.press any other key exit""")
        if(user_input=="1"):
            self.signup()
        elif(user_input=="2"):
            self.signin()
        elif(user_input=="3"):
            self.my_post()
        elif(user_input=="4"):
            self.sendmsg()
        else:
            exit()
    def signup(self):
        email=input("Enter the your email here ->")
        pwd=input("Enter your password here ->")
        self.username=email
        self.password=pwd
        print("You have signed up successfully")
        print("/n")
        self.menu()
    def signin(self):
        if self.username=="" and self.password=="":
            print("Please signup first:->")
        else:
            uname=input("Enter your email/username here ->")
            pwd=input("Enter you password here ->")
            if self.username==uname and self.password==pwd :
                print("You have signed in successfully")
                self.loggedin=True
            else:
                print("Please enter correct credentials")
        print("/n")
        self.menu()
    def my_post(self):
        if self.loggedin==True:
            txt=input("Enter your messege here ->")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to write a post.")
        print("/n")
        self.menu()
    def sendmsg(self):
        if self.loggedin==True:
            txt=input("Enter your messege here ->")
            frnd=input("Whom to send the messege ->")
            print(f"Your messege has been send to {frnd}")
        else:
            print("You need to signin first to write a post.")
        print("/n")
        self.menu()
