import mysql.connector # type: ignore
from initDatabase import initDatabase


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
    while userInput != 4:
        print('#######################################\n')
        print('Select an option for the fitness database.\n')
        print("1. Display all client's future appointments")
        print("2. Display all of client's exercises on a date")
        print("3. Display the time and location of a trainer's upcoming appointment")
        print("4. Quit")

        userInput = input("\n Your Option: ")

        match userInput:
            case 1:
                break

            case 2: 
                break

            case 3:
                break

            case 4:
                break
               
            case default:
                print("Invalid Option. Please Choose Again")
    

    #------------------------------------------------------
    #Closes the connection when done
    cnx.commit()

    cursor.close()
    cnx.close()

main()