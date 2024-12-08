import datetime

class ClientAppointments:
    def __init__(self, cursor):
        self.cursor = cursor
    
    def run(self):
        #Retrieves client ID from user. If not a number, discard the value and set it to -1
        print("\nYou are searching for a client's future appoints. Please give the client ID for the specfied client")
        try:
            clientID = int(input("Client's ID: "))
        except:
            clientID = -1
        curDate = datetime.date.today()

        query = """SELECT APPT_DATE, APPT_TIME, TRAINER.F_Name, GYM.Name, CLIENT.F_Name, CLIENT.L_Name
                    FROM APPOINTMENT, TRAINER, CLIENT, GYM
                    WHERE TRAINER.Trainer_ID = APPOINTMENT.Trainer AND 
                    GYM.Gym_ID = APPOINTMENT.Gym AND
                    CLIENT.Client_ID = APPOINTMENT.Client AND
                    APPT_DATE > %s AND CLIENT.Client_ID = %s"""

        self.cursor.execute(query, (curDate, clientID))

        itr = 0

        for (Appt_Date, Appt_Time, T_Name, G_Name, C_First, C_Last) in self.cursor:
            if itr == 0:
                print("------------------------------")
                print(f'ALl Future Appointments For {C_First} {C_Last}\n')

            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
            print(f"Date: {Appt_Date.isoformat()}")
            print(f"Time: {Appt_Time}")
            print(f"Gym Location: {G_Name}")
            print(f"Trainer: {T_Name}\n")
            itr += 1
        
        if itr == 0:
            print("------------------------------")
            print(f'There is no Scheduled Future Appointments \n')
            