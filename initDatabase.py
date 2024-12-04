import mysql.connector

#Connects to database and creates cursor
cnx = mysql.connector.connect(user='root', password='65821',
                              host='127.0.0.1')
cursor = cnx.cursor()
#Resets by dropping the database "fitness"
try:
    cursor.execute("DROP DATABASE FITNESS")
except:
    print('No Database to Drop. Continuing\n')

cursor.execute("CREATE DATABASE FITNESS")
cursor.execute("USE FITNESS")

cursor.execute("""CREATE TABLE TRAINER (
                )""")


#Closes the connection when done
cnx.close()