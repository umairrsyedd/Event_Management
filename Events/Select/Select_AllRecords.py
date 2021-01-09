def selectAll(mycursor, mydb):
    mycursor.execute(f'select * from events')
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
