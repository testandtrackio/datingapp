import csv

global strengthslist
strengthslist=["patience","efficiency","sensitivity","frankness","submissiveness","leadership","timekeeping","laidback"]

def mainmenu():
      while True:
        print("""
    ============MAIN MENU================
                       *Find the love of your life*
                       1. Register
                       2. Login
                       3. Quit
    """)
        
        x=input("Enter choice:")
        if int(x)==1:
            register()
            break
        elif int(x)==2:
            login()
            break
        elif int(x)==3:
            print("Goodbye then!")
            break
            

def register():
    print("===Register====")
    print("First things first, sign up and tell us a little about yourself")
    with open("dating.txt","a") as fo: 
        writer=csv.writer(fo)        
        firstname=input("Enter first name:")
        lastname=input("Enter last name:")
        username=firstname+lastname[0]+"bird"
        print("Your automatically generated username is:",username)
        password=input("Enter password:")
        gender=input("Enter gender")
        email=input("Enter email:")
        dob=input("Enter date of birth in format dd/mm/yy:")
        beliefs=input("Enter beliefs")
        strengthslist=["patience","efficiency","sensitivity","frankness","submissiveness","leadership","timekeeping","laidback"]
        print(strengthslist)
        strengths=input("Enter your top strength: (select from the above list)")
        contactcount=0
        writer.writerow([username,password,firstname,lastname,gender,email,dob,beliefs,strengths,contactcount])
        print("written to file")
    mainmenu()


def login():
    print("===Welcome to the Dating System prototype====")
    global notloggedin
    notloggedin=True 

    while notloggedin==True: 
        with open("dating.txt","r") as f:
            username=input("Enter username:")
            password=input("Enter password:")
            reader=csv.reader(f)
            for row in reader:
                for field in row:
                    if field==username and row[1]==password:
                        notloggedin=False
                    else:
                        break
            if notloggedin==True: 
                    print("Try again")
            else:
                    print("=====Access Granted! Ready to date?!======")
                    profile(username)

def profile(username):
  print()
  print()
  print("------Welcome to your profile---------")
  print()
  print()
  with open("dating.txt",newline="") as f:
    reader=list(csv.reader(f))
    temporarylist=enumerate(reader)
    for idx, row in temporarylist:
      for field in row:
        if field==username:
           username_index = idx
           print(username_index)
           print("Welcome,",field)
           wavedcount=int(reader[username_index][9])
  print("Waved at:",wavedcount)
  waved=int(input("How many potential dates have you waved at this week?"))
  wavedcount=wavedcount+waved
  print("Waved-at count:",waved)
  ##ADDING ABILITY TO UPDATE contactcount variable in the file
  temporarylist=[]
  updatedlist=[]
  with open("dating.txt",newline="") as f:
    reader=list(csv.reader(f))
    temporarylist=reader #store copy of the file contents here
    for row in reader: #for every row in the file
      for field in row:
        if field==username:
          updatedlist.append(row)
          updatedlist[0][9]=int(updatedlist[0][9])+waved
    updatecontactcount(updatedlist,temporarylist)

def updatecontactcount(updatedlist,temporarylist):
    for index, row in enumerate(temporarylist):
        for field in row:
            if field==updatedlist[0]:
                temporarylist[index]=updatedlist #replace old record with updated records
    with open("dating.txt","w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(temporarylist)
        print("File has been updated")
        print("People you have waved at:",updatedlist[0][9])
    print("-------What next?-----------")              
    choice=input("Enter S to start searching or M if you want us to find you a match!")
    if choice=="s" or choice=="S":
      search()
    elif choice=="M" or choice=="m":
      matchmagic()
                   
def search():        
        print("====Search Menu======")
        print("""
        1. Search by Gender
        2. Search by Date
        3. Search by key word
        4. Return to Main Menu
    """)
        choice=input("What would you like to do?:")
        if int(choice)==1:
            gender()
        elif int(choice)==2:
            date()
        elif int(choice)==3:
            keyword()
        elif int(choice)==4:
            mainmenu()

def gender():
    print("==Search by Gender==")
    with open("dating.txt","r") as f: 
        gender=input("Enter the gender you are looking for:")
        reader=csv.reader(f)
        for row in reader:
            for field in row:
                if field==gender:
                    print(row)
    
    search()

def keyword():
    wordfound=False
    print("===Search by Key word===")
    while wordfound==False: 
        with open("dating.txt","r") as f:
            keyword=input("Enter keyword:")
            reader=csv.reader(f)
            for row in reader:
                for field in row:
                    if field==keyword:
                        print(row)
                        wordfound=True           
    search()

def date():
  pass   

def matchmagic():
    wordfound=False
    print("===Creating Match===")
    while wordfound==False: 
        with open("dating.txt","r") as f:
            keystrength=input("Enter one of your key strengths:")
            print()
            print()
            print("Printing potential --true love-- matches!")
            reader=csv.reader(f)
            for row in reader:
              if row[8] != keystrength: 
                print(row)
                wordfound=True
                                   
    search()
                
mainmenu()
    
