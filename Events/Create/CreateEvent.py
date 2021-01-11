def createEvent(mycursor, mydb):
    Event_Date = input("Enter Event Date (YYYY-MM-DD) :  ")
    Event_Name = input("Enter Event Name :  ")
    Start_Time = input("Enter Start Time (HH-MM-SS) :  ")
    End_Time = input("Enter End Time (HH-MM-SS) :  ")
    print("\nVenue List : \n")
    mycursor.execute(f'select * from venues')
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Id : ", x[0], "   ", x[1], "   ", x[4], "   ", x[5])
    Venue_ID = input("Enter Venue ID From Above List\n")
    print("\nClient List : \n")
    mycursor.execute(f'select * from clients')
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[0], "   :    ", x[1])
    Client_ID = input("Enter Client ID From Above List\n")
    status = input(
        "Enter Event Status (0 or 1) (1 - OnSchedule , 0 - Cancelled) :  ")
    mycursor.execute(
        f'insert into events (Event_Date, Event_Name, Start_Time, End_Time , Client_ID , Venue_ID , status) values ("{Event_Date}", "{Event_Name}" , {Start_Time} , {End_Time} , {Client_ID} , {Venue_ID} , {status})')
    print(
        f"New Event Created And Stored In The Database At  :  {Event_Date}\n")
    mydb.commit()
