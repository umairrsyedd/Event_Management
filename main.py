import mysql.connector
from Events.Select.Select_AllRecords import selectAll
from Events.Create.CreateClient import createClient
from Events.Create.CreateVenue import createVenue
from Events.Create.CreateEvent import createEvent
from Events.Delete.DeleteVenue import deleteVenue
from Events.Update.EventStatus import updateStatus
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Uzair2005",
    database="Mini_Project_Event_Management"
)
mycursor = mydb.cursor()

while True:
    print("\nEnter What Do You Want To Do\n")
    choice = int(
        input("1 : Show ALL Events\n2 : Create Client\n3 : Create Venue\n4 : Create Event\n5 : Delete Venue\n6 : Update Event Status\n"))
    print("\n")
    if choice == 1:
        selectAll(mycursor, mydb)
    if choice == 2:
        createClient(mycursor, mydb)
    elif choice == 3:
        createVenue(mycursor, mydb)
    elif choice == 4:
        createEvent(mycursor, mydb)
    elif choice == 5:
        deleteVenue(mycursor, mydb)
    elif choice == 6:
        selectAll(mycursor, mydb)
        updateStatus(mycursor, mydb)
    elif choice == 7:
        break
