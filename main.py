import mysql.connector
from Events.Create.CreateClient import createClient
from Events.Create.CreateVenue import createVenue
from Events.Create.CreateEvent import createEvent
from Events.Select.Select_AllRecords import selectAll
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Uzair2005",
    database="event_management"
)
mycursor = mydb.cursor()

while True:
    print("Enter What Do You Want To Do\n")
    choice = int(
        input("1 : Create Client\n2 : Create Venue\n3 : Create Event\n"))
    if choice == 1:
        createClient(mycursor, mydb)
    elif choice == 2:
        createVenue(mycursor, mydb)
    elif choice == 3:
        createEvent(mycursor, mydb)
    elif choice == 8:
        break
