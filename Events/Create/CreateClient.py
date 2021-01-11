def createClient(mycursor, mydb):
    Client_Name = input("Enter Client Name  ")
    Client_Number = input("Enter Client Phone Number  ")
    Client_Email = input("Enter Client Email ID  ")
    mycursor.execute(
        f'insert into Clients(Name, Phone, email) values("{Client_Name}",{Client_Number}, "{Client_Email}")')
    mydb.commit()
    print("New Client Created Successfully\n")
