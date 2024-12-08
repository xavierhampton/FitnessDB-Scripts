import mysql.connector # type: ignore
from initDatabase import initDatabase
from ClientAppointments import ClientAppointments
from ClientExercises import ClientExercises
from TrainerUpcomingAppointment import TrainerUpcomingAppointment

def main():
    #Connects to database and creates cursor
    cnx = mysql.connector.connect(user='root', password='password',
                                host='127.0.0.1')
    cursor = cnx.cursor()

    #Calls database initalization script
    #Inputs test data and sets up database
    initDatabase(cnx, cursor).run()

    #Prompts the user for their function
    userInput = -1
    while userInput not in {1,2,3,4}:
        print('#######################################')
        print('Select an option for the fitness database.\n')
        print("1. Display all client's future appointments")
        print("2. Display all of client's exercises on a date")
        print("3. Display the time and location of a trainer's upcoming appointment")
        print("4. Quit")

        #Tries to turn user input into int. If unable, Discard the input
        try:
            userInput = int(input("\nYour Option: "))
        except:
            userInput = -1

        #Matches user input to respected cases
        match userInput:
            case 1:
                ClientAppointments(cursor).run()
            case 2: 
                ClientExercises(cursor).run()
            case 3:
                TrainerUpcomingAppointment(cursor).run()
            case 4:
                print('\nExiting...')

            case default:
                print("Invalid Option. Please Choose Again")
    
    
    #------------------------------------------------------
    #Closes the connection when done
    cnx.commit()

    cursor.close()
    cnx.close()

main()