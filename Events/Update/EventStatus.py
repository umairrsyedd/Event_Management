def updateStatus(mycursor, mydb):
    ID = input("Enter Event ID To Update  ")
    status = input("Enter Updated Status\n1 - On Schedule\n0 - Cancelled\n")
    mycursor.execute(
        f'Update events set status = {status} where Event_ID={ID}')
    mydb.commit()
