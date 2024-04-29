def webpage():
    print("Welome to ______ Airlines")
    print("How shall we serve you?")
    print("Press \n1:- Book Tickets \n2:- Edit Ticket \n3:- Pre-order On-board Edibles \n4:- Ticket Cancellations \n5:- Customer Care \n6:- Merchandises  ")
    c=int(input("Enter your choice here:-"))
    if c==1:
        print("Hello")
        import Booking
        print("bye")
    elif c==2:
        import Update
    elif c==3:
        import Hotel
    elif c==4:
        import cancellation
    elif c==5:
        import complains
    elif c==6:
        import Wanna_work_with_us
webpage()

    
