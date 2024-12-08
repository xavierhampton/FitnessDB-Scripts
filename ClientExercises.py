from datetime import datetime
class ClientExercises:
    def __init__(self, cursor):
        self.cursor = cursor
    
    def run(self):
        #Retrieves client ID from user. If not a number, discard the value and set it to -1
        print("\nYou are searching for a client's exercises on a given date.\n Please give the client ID for the specfied client")
        try:
            clientID = int(input("Client's ID: "))
        except:
            clientID = -1

        print("Please give the date to search in YYYY-MM-DD Format")
        
        try: 
            tmp = input('Workout Date: ')
            userDate = datetime.strptime(tmp, "%Y-%m-%d").date()
        except:
            userDate = datetime.strptime('1500-01-01', "%Y-%m-%d").date()
        
        query = """SELECT EXERCISE.Name, EXERCISE.Weight, EXERCISE.Rep_Count, F_Name, L_Name
                    FROM EXERCISE, CLIENT
                    WHERE Client=Client_ID AND 
                    EXERCISE.Date=%s AND
                    Client_ID=%s"""
        

        self.cursor.execute(query, (userDate, clientID))

        itr = 0

        for (E_name, E_Weight, E_Rep, C_First, C_Last) in self.cursor:
            if itr == 0:
                print("------------------------------")
                print(f'ALl Exercises For {C_First} {C_Last} on {userDate.isoformat()}\n')

            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
            print(f"Exercise: {E_name} lbs")
            print(f"Weight: {E_Weight}")
            print(f"Reps: {E_Rep}\n")
            itr += 1
        
        if itr == 0:
            print("------------------------------\n")
            print(f'There is no exercise for the specified client on the specified date. \n')

       

