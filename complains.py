def complains():
    print("WELCOME!!!\n Here you can find FAQs and give manual complaints as well,\na. Frequently Asked Questions(FAQs) \nb. Give A Manual Complain or Feedback \nc. Exit Booking Page")
    qa=str(input("ENTER YOUR CHOICE:  "))
    if qa in ['a']:
        print("\nHere You Can See Problems You Might Have That Have Been Answered ,\nIf You Are Not Able To Find Answers Related Your To Your Respective Problems \nThen Please Type 2 And Enter Your Complain There \nWe Will Try To Resolve It As Soon As We Can.\n")
        with open('COMPLAINSS.txt') as f:
            for line in f:
                print(line,end=" ")
    elif qa in ['b']:
        print("HELLO! YOU CAN TYPE YOUR COMPLAINS OR FEEDBACK AS WELL")
        complainfile=open('MANUAL COMPLAINTS.txt','a')
        ans='y'
        name=str(input("ENTER YOUR NAME: "))
        while ans=='y':
            complain=str(input("ENTER YOUR COMPLAIN HERE: "))
            complainfile.write("\n"+name+" \n")
            complainfile.write(complain+"\n"+"\n")
            ans=input("DO YOU WANT TO ADD ANYTHING MORE TO YOUR COMPLAIN ?(y/n)...")
    elif qa in ['c']:
        print("THANK YOU FOR VISITING :)")
complains()
import MainPage
webpage()
