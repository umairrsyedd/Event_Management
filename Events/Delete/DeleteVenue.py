def deleteVenue(mycursor, mydb):
    VenueName = input("Enter Venue name  ")
    VenueName = VenueName.upper()
    try:
        mycursor.execute(
            f'delete from Venues where Name="{VenueName}"')
    except:
        print("Except Block entered")
        OwnerNumber = input("Enter Owner Number")
    mydb.commit()
