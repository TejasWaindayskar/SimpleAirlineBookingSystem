import random
import mysql.connector as a
mycon=a.connect(host="localhost",user="root",passwd="0000",database="airways")
cursor=mycon.cursor()
def Booking():
    no_of_passengers=int(input("Enter no of passengers: "))
    for i in range(no_of_passengers):
        print("\nEnter details of passenger no.",i+1)
        #to Auto-generate random seat no
        x='A'
        y='Z'
        section=chr(random.randint(ord(x), ord(y)))
        no_=str(random.randint(00,100))
        seatno=section+"-"+no_
        # to Auto-generate random passenger id
        passid=random.randint(63200,65000)
        #user inserted Passenger details
        passname=input("Enter name: ")
        age=input("Enter age: ")
        print("Enter 'B'/'E'/'F'")
        passclass=input("Enter class: ")
        place=int(input("Enter your travel route:\n1.DELHI-MUMBAI\n2.DELHI-MUMBAI-CHENNAI(connecting)\n==> "))
        if place==1:
            from_to="DELHI-MUMBAI"
            duration='11:00-12:35'
        elif place==2:
             from_to="DELHI-MUMBAI-CHENNAI"
             duration='11:00-14:25'
        food=input("Enter Food: ")
        cursor.execute("insert into passengers(passid,passname,age,passclass,seatno,food,From_To,Duration) values ({},'{}',{},'{}','{}','{}','{}','{}')".format(passid,passname,age,passclass,seatno,food,from_to,duration))
        mycon.commit()
        print ("Passenger registered")
    print("\nWe wish you a safe and happy journey")
Booking()
import MainPage
webpage()
