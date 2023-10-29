#Extend the program again by adding a method fire_alarm that does not receive any parameters
# and moves all elevators to the bottom floor.
# Continue the main program by causing a fire alarm in your building.

class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.position = bottom_floor

    def floor_up(self):
        self.position += 1
        print(f"Elevator is now at {self.position} floor.")
        return

    def floor_down(self):
        self.position -= 1
        print(f"Elevator is now at {self.position} floor.")
        return

    def go_to_floor(self, floor):
        while self.position != floor:
            if self.position < floor:
                self.floor_up()

            if self.position > floor:
                self.floor_down()
        print(f"You have reached floor {floor}.")

class Building:
    def __init__(self, btm_floor, upp_floor, elevators):
        self.bottom = btm_floor
        self.up = upp_floor
        self.elevators = []
        for i in range(elevators):
            elevator = Elevator(btm_floor, upp_floor)
            self.elevators.append(elevator)

    def run_elevator(self, el_number, dest_floor):
        elevator = self.elevators[el_number-1]
        elevator.go_to_floor(dest_floor)
        print(f"Elevator {el_number} now at destination floor {dest_floor}")
        return

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)
            print(f"Elevator {self.elevators.index(elevator) + 1} is at floor {self.bottom}!")
        print("Fire alarm. All elevators at the bottom floor!")




building = Building(1, 12, 3)
building.run_elevator(3, 10)
building.run_elevator(1, 7)
building.fire_alarm()

