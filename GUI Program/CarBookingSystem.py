import tkinter as tk
from tkinter import simpledialog

class CarBookingSystem:
    def __init__(self):
        self.destination = None
        self.pickupLocation = None

    def setDestination(self, destination):
        self.destination = destination

    def getDestination(self):
        return self.destination

    def setPickupLocation(self, pickupLocation):
        self.pickupLocation = pickupLocation

    def getPickupLocation(self):
        return self.pickupLocation

    def getTripDetail(self):
        tripDetail = {}
        tripDetail["Pickup Location"] = self.pickupLocation
        tripDetail["Drop Location"] = self.destination
        return tripDetail


class CarBookingGUI:
    def __init__(self, master):
        self.master = master
        master.title("Car Booking System")

        self.listTrip = []
        self.trip = CarBookingSystem()

        self.label = tk.Label(master, text="Car Booking System")
        self.label.pack()

        self.start_button = tk.Button(master, text="Start Trip", command=self.start_trip)
        self.start_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=master.destroy)
        self.exit_button.pack()

        self.output_label = tk.Label(master, text="")
        self.output_label.pack()

    def start_trip(self):
        self.trip.setPickupLocation(simpledialog.askstring("Input", "Enter pickup Location:"))
        self.trip.setDestination(simpledialog.askstring("Input", "Enter Drop Location:"))
        trip_detail = self.trip.getTripDetail()
        print(trip_detail)
        self.listTrip.append(trip_detail)
        self.update_output_label()

    def update_output_label(self):
        output_text = "\n".join(["PICKUP LOCATION: {}\t\tDROP LOCATION: {}".format(trip['Pickup Location'], trip['Drop Location']) for trip in self.listTrip])
        self.output_label.config(text=output_text)


root = tk.Tk()
app = CarBookingGUI(root)
root.mainloop()

print("Congrats! Today you had 100 trips")
print("PICKUP LOCATION\t\tDROP LOCATION")

for trip in app.listTrip:
    print("{}\t\t\t{}".format(trip['Pickup Location'], trip['Drop Location']))
