import mysql.connector
from Events.Select.Select_AllRecords import selectAll
from Events.Create.CreateClient import createClient
from Events.Create.CreateVenue import createVenue
from Events.Create.CreateEvent import createEvent
from Events.Delete.DeleteVenue import deleteVenue
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
        input("1 : Show ALl Events\n2 : Create Client\n3 : Create Venue\n4 : Create Event\n4 : Delete Venue\n"))
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
        break
