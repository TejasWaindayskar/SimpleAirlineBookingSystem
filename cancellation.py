import mysql.connector as a
mycon=a.connect(host="localhost",user="root",passwd="0000",database="airways")
cursor=mycon.cursor()
def cancell():
    print("Welcome to the cancellation page.\nHere you can cancel your ticket")
    Passid=int(input("Enter your PassID:"))
    sure=input("Are you sure you want to cancel your ticket(y/n)? If your ticket is cancelled all input data will be lost!\n==> ")
    if sure=="y":
        sql="delete from passengers where PassID=%s"%(Passid,)
        cursor.execute(sql)
        for i in cursor:
            print(i)
        mycon.commit()
        print("CANCELLATION SUCCESSFUL")
        print("\nWe request you to fill our feedback form")
        i=input("Do you want to fill our feedback form?(y/n)")
        if i=="y":
            import complains
        elif i=="n":
            print("Thank you :)")
    elif sure=="n":
        print("So you want to reconsider, good choice!")
cancell()
import MainPage
webpage()
