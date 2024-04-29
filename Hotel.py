import random
import mysql.connector as a
mycon=a.connect(host="localhost",user="root",passwd="0000",database="airways")
cursor=mycon.cursor()
print("Welcome to Hotel________,\nHere you can rest after your tiring and weary journeys and replenish yourself for a new journey!!")
PassID=int(input("Pleases enter your PassID to start registration :"))
def hotel():
    PassName=input("Enter your name: ")
    NOP=int(input("Enter no. of people:"))
    print=("Enter the option no. preceeding the following services: ")
    choice=int(input("1. Discount Packages,\n2. Tailor-Made Packages\n==> "))
    if choice==1:
        #to Auto-generate random seat no
        x='A'
        y='Z'
        block=chr(random.randint(ord(x), ord(y)))
        floor=str(random.randint(00,50))
        no_=str(random.randint(00,50))
        room_no=block+"/"+floor+'-'+no_
        bed=int(input("How many beds would you like to order: "))
        suite=input("Size of the suite you wish to live in\nEmperor class \nNoble class\n Discount class\n==> ")
        pool=input("Would you like to avail pool services: ")
        cursor.execute("insert into hotel(PassID,PassName,Room_no,No_of_Beds,Suite_Type_,Pool_Service) values ('{}','{}','{}', {} ,'{}','{}')".format(PassID,PassName,room_no,bed,suite,pool))
        mycon.commit()
print("Thank you for choosing us , we hope your stay is pleasant ,ralaxing and memorable")
hotel()
import MainPage
MainPage()
        
