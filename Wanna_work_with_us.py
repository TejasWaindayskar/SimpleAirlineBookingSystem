def jobs():
    print("WELCOME!!!,\nx.JOBS AVAILABLE \ny.APPLY \nz.EXIT")
    cho=str(input("ENTER YOUR CHOICE:"))
    if cho in['x']:
        sql="desc job"
        cursor.execute(sql)
        for j in cursor:
            print(j)
    elif cho in ['y']:
        NAME=input("ENTER YOUR NAME:")
        AGE=int(input("ENTER YOUR AGE:"))
        QUALIFICATION=input("ENTER YOUR QUALIFICTIONS:")
        EXPERIENCE=input("ENTER YOUR EXPERIENCE IN THE FIELD IF ANY:")
        APPLYING_FOR=input("ENTER THE JOB YOU WANT TO APPLY FOR:")
        sql="insert into applyy(EMPNAME,APPLYING_FOR,AGE,QUALIFICATION,EXPERIENCE) values(%s,%s,%s,%s,%s)"%(NAME,APPLYING_FOR,AGE,QUALIFICATION,EXPERIENCE)
        cursor.execute(sql)
        mycon.commit()
        print("THANK YOU :)")
    elif cho in ['z']:
        feedbackfile=open('feedback.txt','a')
        feed='y'
        if feed=='y':
            NAME=str(input("PLEASE ENTER YOUR NAME FOR FEEDBACK:"))
            FEEDBACK=str(input("PLEASE GIVE A FEEDBACK:"))
            feedbackfile.write(NAME)
        feedbackfile.write(FEEDBACK)
        print("THANK YOU COMING :)")
jobs()
