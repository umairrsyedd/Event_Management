def deleteVenue(mycursor, mydb):
    print("Venue List : \n")
    mycursor.execute(f'select * from venues')
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Id : ", x[0], "   ", x[1], "   ", x[4], "   ", x[5])
    Venue_ID = input("Enter Venue ID From Above List To Delete\n")
    mycursor.execute(
        f'delete from Venues where Venue_ID={Venue_ID}')
    mydb.commit()
    print("Venue Deleted Successfully")
