# Extend the previous program by creating a Building class.
# The initializer parameters for the class are the numbers of the bottom and top floors
# and the number of elevators in the building. When a building is created,
# the building creates the required number of elevators. The list of elevators is stored as
# a property of the building. Write a method called run_elevator that accepts the number
# of the elevator and the destination floor as its parameters. In the main program,
# write the statements for creating a new building and running the elevators of the building.


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

building = Building(1, 12, 3)
building.run_elevator(3, 10)
building.run_elevator(1, 7)
