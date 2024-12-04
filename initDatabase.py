import mysql.connector # type: ignore

#Connects to database and creates cursor
cnx = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1')
cursor = cnx.cursor()
#Resets by dropping the database "fitness"
try:
    cursor.execute("DROP DATABASE FITNESS")
except:
    print('No Database to Drop. Continuing\n')

cursor.execute("CREATE DATABASE FITNESS")
cursor.execute("USE FITNESS")

#Creates Trainer Table
cursor.execute("""CREATE TABLE TRAINER (
                Trainer_ID          INT             NOT NULL,
                F_name              VARCHAR(15),
                L_name              VARCHAR(15),
                Gender              CHAR(1),
                Years_Experience    INT,
                DOB                 DATE,
                PRIMARY KEY(Trainer_ID)
               )""")

#Creates Client Table
cursor.execute("""CREATE TABLE CLIENT (
               Client_ID            INT             NOT NULL,
               F_Name               VARCHAR(15),
               L_name               VARCHAR(15),
               Gender               CHAR(1),
               Height               INT,
               Weight               INT,
               DOB                  DATE,
               Trainer              INT,
               PRIMARY KEY(Client_ID),
               FOREIGN KEY(Trainer) REFERENCES TRAINER(Trainer_ID)
               )""")

#Creates Gym Table
cursor.execute("""CREATE TABLE GYM (
                Gym_ID              INT             NOT NULL,
                Name                VARCHAR(15),
                City                VARCHAR(15),
                State               VARCHAR(2),
                Zip                 INT,
                St_Address          VARCHAR(30),
                PRIMARY KEY(Gym_ID)
               )""")

#Creates Appointment Table
cursor.execute("""CREATE TABLE APPOINTMENT (
               Appt_ID              INT             NOT NULL,
               Appt_Date            DATE            NOT NULL,
               Appt_Time            TIME            NOT NULL,
               Trainer              INT,
               Client               INT,
               Gym                  INT,
               FOREIGN KEY(Trainer) REFERENCES TRAINER(Trainer_ID),
               FOREIGN KEY(Client) REFERENCES CLIENT(Client_ID),
               FOREIGN KEY(Gym) REFERENCES GYM(Gym_ID)
               )""")

#Creates Exercise Table
cursor.execute("""CREATE TABLE EXERCISE (
                Exercise_ID         INT             NOT NULL,
                Client              INT,
                Date                DATE,
                Name                VARCHAR(15),
                Weight              INT,
                Rep_Count           INT,
                PRIMARY KEY(Exercise_ID),
                FOREIGN KEY(Client) REFERENCES CLIENT(Client_ID)
               )""")

#Creates Language Table
cursor.execute("""CREATE TABLE TRAINER_LANGUAGES (
                Trainer_ID          INT             NOT NULL,
                Language            VARCHAR(20),
                FOREIGN KEY(Trainer_ID) REFERENCES TRAINER(Trainer_ID)
               )""")


#Closes the connection when done
cnx.close()