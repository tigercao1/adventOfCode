myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

class Waypoint():
    def __init__(self):
        self.vpos = 1
        self.hpos = 10
        self.turn_set = set(["L", "R"])
        self.dir_set = set(["N", "E", "S", "W"])

    def process_input(self, dir, deg):
        if dir in self.turn_set:
            self.turn(dir, deg)
        elif dir in self.dir_set:
            self.move(dir, deg)

    def turn(self, dir, deg):
        if dir == "L":
            self.rotate_waypoint(-deg)
        elif dir == "R":
            self.rotate_waypoint(deg)
    
    def rotate_waypoint(self, deg):
        if deg >= 0:
            num_rotation = deg // 90
            for i in range(num_rotation):
                temp = self.hpos
                self.hpos = self.vpos
                self.vpos = -temp
        if deg < 0:
            num_rotation = -deg // 90
            for i in range(num_rotation):
                temp = self.hpos
                self.hpos = -self.vpos
                self.vpos = temp

    def move(self, dir, num):
        if dir == "N":
            self.vpos += num
        elif dir == "S":
            self.vpos -= num
        elif dir == "E":
            self.hpos += num
        elif dir == "W":
            self.hpos -= num

class Ship():
    def __init__(self, dir="E", deg=90):
        self.vpos = 0
        self.hpos = 0
        self.waypoint = Waypoint()

    def move(self, num):
        for i in range(num):
            self.vpos += self.waypoint.vpos
            self.hpos += self.waypoint.hpos

    def update_waypoint(self, dir, deg):
        self.waypoint.process_input(dir, deg)

    def calculate_distance(self):
        return abs(self.hpos) + abs(self.vpos)

class Solution():
    def __init__(self, arr):
        self.arr = arr
        self.ship = Ship()

    def move_ship(self):
        for i in self.arr:
            command = i[0]
            unit = int(i[1:])
            if command == "F":
                self.ship.move(unit)
            else:
                self.ship.update_waypoint(command, unit)
        return self.ship.calculate_distance()

s = Solution(content_list)
print(s.move_ship())
        