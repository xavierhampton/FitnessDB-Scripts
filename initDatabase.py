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

#---------------------------------------------------

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
                Exercise_ID         INT             NOT NULL        AUTO_INCREMENT,
                Client              INT             NOT NULL,
                Date                DATE            NOT NULL,
                Name                VARCHAR(30),
                Weight              INT,
                Rep_Count           INT,
                PRIMARY KEY(Exercise_ID, Client),
                FOREIGN KEY(Client) REFERENCES CLIENT(Client_ID)
               )""")

#Creates Language Table
cursor.execute("""CREATE TABLE TRAINER_LANGUAGES (
                Trainer_ID          INT             NOT NULL,
                Language            VARCHAR(20)     NOT NULL,
                PRIMARY KEY(Trainer_ID, Language),
                FOREIGN KEY(Trainer_ID) REFERENCES TRAINER(Trainer_ID)
               )""")


#------------------------------------------------------

#Creates Synthetic Data

#Creates Trainer Data
cursor.execute("""INSERT INTO TRAINER 
               VALUES (111, 'John', 'Gates', 'M', 10, '2000-10-14'),
                      (222, 'Bob', 'Apple', 'M', 2, '1994-01-20'),
                      (333, 'Sydney', 'Cheese', 'F', 6, '1995-08-31')
               """)

#Creates Client Data
cursor.execute("""INSERT INTO CLIENT 
               VALUES (100, 'Xavier', 'Hampton', 'M', 68, 170, '2005-02-03', 111),
                      (200, 'George', 'Washington', 'M', 64, 190, '1842-04-14', 111),
                      (300, 'Janice', 'Quart', 'F', 59, 120, '1997-04-23', 333),
                      (400, 'Jimmy', 'Brown', 'M', 73, 205, '2001-02-27', 222),
                      (500, 'Lebron', 'James', 'M', 78, 185, '1987-07-05', 222)
               """)

#Creates Gym Data
cursor.execute("""INSERT INTO GYM 
               VALUES (10, 'Golds Gym', 'Imperial', 'MO', 63052, '200 Oxford Lane'),
                      (20, 'Planet Fitness', 'Arnold', 'MO', 63051, '320 Smiley Lane'),
                      (30, 'Life Fitness', 'Springfield', 'MO', 67201, '100 Street Lane')
               """)

#Creates Appointment Data
cursor.execute("""INSERT INTO APPOINTMENT 
               VALUES (11, '2024-12-01', '11:30:00', 111, 100, 30),
                      (22, '2024-12-25', '16:00:00', 111, 200, 20),
                      (33, '2025-01-10', '14:45:00', 111, 200, 10),
                      (44, '2025-02-03', '14:30:00', 222, 300, 10),
                      (55, '2024-11-20', '12:45:00', 222, 400, 30),
                      (66, '2025-01-02', '18:00:00', 222, 300, 20),
                      (77, '2024-12-26', '16:00:00', 333, 300, 10),
                      (88, '2024-10-31', '15:30:00', 333, 300, 30),
                      (99, '2025-01-01', '16:45:00', 333, 300, 20)
               """)

#Creates Exercise Data
cursor.execute("""INSERT INTO EXERCISE (Client, Date, Name, Weight, Rep_Count) 
               VALUES (100, '2024-12-10', 'Dumbbell Curls', 30, 12),
                      (100, '2024-12-10', 'Cable Tricep Pushdowns', 70, 8),
                      (100, '2024-12-10', 'Dumbbell Shoulder Press', 60, 10),
                      (200, '2024-12-10', 'Leg Press', 30, 5),
                      (200, '2024-12-10', 'Seated Hamstring Curls', 35, 12),
                      (200, '2024-12-10', 'Calf Raises', 75, 8),
                      (300, '2024-12-10', 'Chest Press', 15, 10),
                      (300, '2024-12-10', 'T-Bar Rows', 25, 9),
                      (300, '2024-12-10', 'Lateral Pulldowns', 100, 6),
                      (400, '2024-12-10', 'Barbell Squat', 90, 12),
                      (400, '2024-12-10', 'Spider Curls', 35, 12),
                      (400, '2024-12-10', 'Reverse Curls', 25, 8),
                      (400, '2024-12-10', 'Deadlift', 20, 9),
                      (500, '2024-12-10', 'Skull Crushers', 70, 7),
                      (500, '2024-12-10', 'Power clean', 80, 15),
                      (500, '2024-12-10', 'Low Rows', 65, 8),
                      (500, '2024-12-10', 'Pull-Ups', 60, 12),
                      (500, '2024-12-10', 'Dips', 5, 6)
               """)

#Creates Trainer Languages Data
cursor.execute("""INSERT INTO TRAINER_LANGUAGES
               VALUES (111, 'English'),
                      (111, 'Spanish'),
                      (222, 'English'),
                      (333, 'English')
               """)



#------------------------------------------------------
#Closes the connection when done
cnx.commit()

cursor.close()
cnx.close()