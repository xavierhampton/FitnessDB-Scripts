import datetime
class TrainerUpcomingAppointment:
    def __init__(self, cursor):
        self.cursor = cursor
    
    def run(self):
        #Retrieves trainer ID from user. If not a number, discard the value and set it to -1
        print("\nYou are searching for a Trainer's next appointment")
        try:
            trainerID = int(input("Trainer's ID: "))
        except:
            trainerID = -1
        curDate = datetime.date.today()


        query = """SELECT TRAINER.F_Name, TRAINER.L_Name, CLIENT.F_Name,
                     CLIENT.L_Name, APPT_Date, APPT_Time, GYM.Name
                     FROM CLIENT, TRAINER, APPOINTMENT, GYM
                     WHERE Client=Client_ID AND 
                     APPOINTMENT.Trainer=Trainer_ID AND
                     APPOINTMENT.GYM = GYM.GYM_ID AND
                     Trainer_ID = %s AND
                     APPT_Date > %s

                     ORDER BY APPT_Date, APPT_Time ASC
                     LIMIT 1
                     """

        self.cursor.execute(query, (trainerID, curDate))

        itr = 0

        for (T_F, T_L, C_F, C_L, A_DATE, A_TIME, G_NAME) in self.cursor:
            if itr == 0:
                print("------------------------------")
                print(f'The next appointment for {T_F} {T_L} is:\n')

            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
            print(f"Date: {A_DATE.isoformat()}")
            print(f"Time: {A_TIME}")
            print(f"Gym Location: {G_NAME}")
            print(f"Client: {C_F} {C_L} \n")
            itr += 1
        
        if itr == 0:
            print("------------------------------\n")
            print(f'There is no Scheduled Future Appointments \n')
            