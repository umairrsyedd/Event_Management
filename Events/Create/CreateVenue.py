def createVenue(mycursor, mydb):
    Venue_Name = input("Enter Venue Name  ")
    Venue_Name = Venue_Name.upper()
    Owner_Name = input("Enter Name Of Owner  ")
    Owner_Number = input("Enter Owner Number  ")
    Price = input("Enter Price Of Venue  ")
    Address = input("Enter Address Of The Venue")
    mycursor.execute(
        f'insert into Venues (Name,Owner_Name,Owner_Number,price,address) values ("{Venue_Name}" , "{Owner_Name}" , {Owner_Number} , {Price} , "{Address}")')
    mydb.commit()
