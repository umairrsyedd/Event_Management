def selectAll(mycursor, mydb):
    mycursor.execute(f'select * from events')
    myresult = mycursor.fetchall()
    for x in myresult:
        if(x[7] == 0):
            temp = "Cancelled"
        else:
            temp = "On Schedule"
        print(f'Event ID: ', x[0], '  Event Name: ',
              x[2], '      Event Status: ',  temp)
