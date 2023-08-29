class Spacecraft:
    def __init__(self, x=0, y=0, z=0, direction='N'):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1

    def move_backward(self):
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def turn_up(self):
        if self.direction == 'N' or self.direction == 'S':
            self.direction = 'Up'

    def turn_down(self):
        if self.direction == 'N' or self.direction == 'S':
            self.direction = 'Down'

spacecraft=Spacecraft()
commands={
    "f":spacecraft.move_forward,
    "b":spacecraft.move_backward,
    "l":spacecraft.turn_left,
    "r":spacecraft.turn_right,
    "u":spacecraft.turn_up,
    "d":spacecraft.turn_down
}
while True:
    user_input=input("enter your command(f/b/l/r/u/d)or c :").lower()
    if user_input == "c":
        print("closed...")
        break
    elif user_input in commands :
        commands[user_input]()
        print("Final Position:(x,y,z)=(", spacecraft.x, spacecraft.y, spacecraft.z, ")")
        print("Final Direction:", spacecraft.direction)
        break

    else:
        print("invalid input try again...")
