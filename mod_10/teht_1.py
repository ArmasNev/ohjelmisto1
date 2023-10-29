#Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
# The elevator has methods go_to_floor, floor_up and floor_down.
# A new elevator is always at the bottom floor.
# If you make elevator h for example the method call h.go_to_floor(5),
# the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
# The methods run the elevator one floor up or down and tell what floor the elevator is after each move.
# Test the class by creating an elevator in the main program,
# tell it to move to a floor of your choice and then back to the bottom floor.

class Elevator:


    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.position = bottom_floor

    def floor_up(self):
        self.position += 1
        print(f"Elevator is now at {self.position} floor. Elevator going up.")
        return
    def floor_down(self):
        self.position -= 1
        print(f"Elevator is now at {self.position} floor. Elevator going down.")
        return

    def go_to_floor(self, floor):
        while self.position != floor:
            if self.position < floor:
                self.floor_up()

            if self.position > floor:
                self.floor_down()
        print(f"You have reached floor {floor}.")


elevator_A = Elevator(0, 10)
elevator_A.go_to_floor(9)
elevator_A.go_to_floor(3)




