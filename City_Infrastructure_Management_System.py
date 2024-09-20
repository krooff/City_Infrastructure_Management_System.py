#Task 1: Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    # Method to update the owner of the vehicle
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"The owner of vehicle {self.registration_number} has been updated to {self.owner}.")

# Creating vehicle instances
vehicle1 = Vehicle("ABC123", "Car", "John Doe")
vehicle2 = Vehicle("XYZ789", "Motorcycle", "Jane Smith")

# Printing initial details
print(f"Vehicle 1: Reg: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: Reg: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

# Updating the owners
vehicle1.update_owner("Alice Johnson")
vehicle2.update_owner("Bob Williams")

# Printing updated details
print(f"Updated Vehicle 1: Reg: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Updated Vehicle 2: Reg: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

#Task 2: Event Management System

# Defining the Event class with participant tracking
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count to 0

    
    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added. Total participants: {self.participant_count}")

   
    def get_participant_count(self):
        return self.participant_count

# Demonstration script

event = Event("Python Workshop", "2024-09-25")


event.add_participant()
event.add_participant()


print(f"Current participant count for {event.name}: {event.get_participant_count()}")
