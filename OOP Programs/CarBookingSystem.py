class CarBookingSystem:
    def __init__(self):
        destination = None
        pickupLocation = None
    
    def setDestination(self,destination):
        self.destination = destination

    def getDestination(self):
        return self.destination

    def setPickupLocation(self,pickupLocation):
        self.pickupLocation = pickupLocation

    def getPickupLocation(self):
        return self.pickupLocation
    
    def getTripDetail(self):
        tripDetail = {}
        tripDetail["Pickup Location"] = self.pickupLocation 
        tripDetail["Drop Location"] = self.destination
        return tripDetail


listTrip = []

process = True

while process:
    userInput = int(input("1. Press 1 to start Trip\n2. Press  0  to Exit\nEnter your choice: "))
    if userInput == 1:
        trip = CarBookingSystem()
        trip.setPickupLocation(input("Enter pickup Location:"))
        trip.setDestination(input("Enter Drop Location:"))
        print(trip.getTripDetail())
        listTrip.append(trip)
    else:
        process = False
    
print(f"Congrats! Today you had 100 trips")
print("PICKUP LOCATION\t\tDROP LOCATION" )

for trip in listTrip:
    tripDetail = trip.getTripDetail() 
    print("{}\t\t\t{}".format(tripDetail['Pickup Location'],tripDetail['Drop Location']))