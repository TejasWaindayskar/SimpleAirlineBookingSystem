import mysql.connector as a
mycon=a.connect(host="localhost",user="root",passwd="0000",database="airways")
cursor=mycon.cursor()
def Update():
    print("Enter your Passenger ID to proceed to updating procedure:-")
    PassID=input("Enter Passenger ID: ")
    print("This is your current ticket")
    cursor.execute("select* from passengers where passid={}".format(PassID))
    for x in cursor:
        print(x)
        mycon.commit()
    i = int(input("1.Age,\n2.Class,\n3.Food,\n4.Destination(DEHLI-MUMBAI-CHENNAI / DEHLI-MUMBAI)\n==> "))
    if i==1:
        new_age=int(input("Enter age to be updated : "))
        cursor.execute("update passengers set Age={} where PassID={}".format(new_age,PassID))
        print("This is your updated ticket")
        cursor.execute("select* from passengers where PassID={}".format(PassID))
        for y in cursor:
            print(y)
        mycon.commit()
    elif i==2:
        print("Please insert in Double Inverted Comma("")")
        new_class=input("Enter Class to be updated : ")
        cursor.execute("update passengers set PassClass={} where PassID={}".format(new_class,PassID))
        print("This is your updated ticket")
        cursor.execute("select* from passengers where PassID={}".format(PassID))
        for y in cursor:
            print(y)
        mycon.commit()
    elif i==3:
        print("Please insert in Double Inverted Comma("")")
        new_food=input("Enter food to be updated : ")
        cursor.execute("update passengers set Food={} where PassID={}".format(new_food,PassID))
        print("This is your updated ticket")
        cursor.execute("select* from passengers where PassID={}".format(PassID))
        for y in cursor:
            print(y)
        mycon.commit()
    elif i==4:
        print("Please insert in Double Inverted Comma("")")
        new_dest=input("Enter destination to be updated : ")
        cursor.execute("update passengers set From_To={} where PassID={}".format(new_dest,PassID))
        print("This is your updated ticket")
        cursor.execute("select* from passengers where PassID={}".format(PassID))
        for y in cursor:
            print(y)
        mycon.commit()
Update()
import webpage
webpage()
