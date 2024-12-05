class FutureClientDates:
    def __init__(self, cursor):
        self.cursor = cursor
    
    def run(self):
        #Retrieves client ID from user. If not a number, discard the value and set it to -1
        print("\nYou are searching for a client's future appoints. Please give the client ID for the specfied client")
        try:
            clientID = int(input("Client's ID: "))
        except:
            clientID = -1

