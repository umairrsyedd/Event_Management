def createEvent(mycursor, mydb):
    Event_Date = input("Enter Event Date (YYYY-MM-DD) :  ")
    Event_Name = input("Enter Event Name :  ")
    Start_Time = input("Enter Start Time (HH-MM-SS) :  ")
    End_Time = input("Enter End Time (HH-MM-SS) :  ")
    Client_ID = 123
    Venue_ID = 456
    status = input(
        "Enter Event Status (0 or 1) (1 - OnSchedule , 0 - Cancelled) :  ")
    mycursor.execute(
        f'insert into events (Event_Date, Event_Name, Start_Time, End_Time , Client_ID , Venue_ID , status) values ("{Event_Date}", "{Event_Name}" , "{Start_Time}" , "{End_Time}" , {Client_ID} , {Venue_ID} , {status})')
    mydb.commit()
