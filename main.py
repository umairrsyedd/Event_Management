import mysql.connector
from Events.Create.CreateClient import createClient
from Events.Create.CreateVenue import createVenue
from Events.Create.CreateEvent import createEvent
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Uzair2005",
    database="event_management"
)
mycursor = mydb.cursor()


createClient(mycursor, mydb)
createVenue(mycursor, mydb)
createEvent(mycursor, mydb)
