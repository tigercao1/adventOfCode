myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

class Ship():
    def __init__(self, dir="E", deg=90):
        self.dir = dir
        self.deg = deg
        self.vpos = 0
        self.hpos = 0
        self.turn_set = set(["L", "R"])
        self.dir_set = set(["N", "E", "S", "W", "F"])

    def process_input(self, dir, deg):
        if dir in self.turn_set:
            self.turn(dir, deg)
        elif dir in self.dir_set:
            self.move(dir, deg)

    def turn(self, dir, deg):
        if dir == "L":
            self.calculate_dir(self.deg - deg)
        elif dir == "R":
            self.calculate_dir(self.deg + deg)
    
    def calculate_dir(self, deg):
        dir_map = {0: "N", 90: "E", 180: "S", 270: "W"}
        if 360 > deg >= 0:
            self.deg = deg
            self.dir = dir_map[deg]
        elif deg >= 360:
            self.deg = deg - 360
            self.dir = dir_map[self.deg]
        elif deg < 0:
            self.deg = 360 + deg
            self.dir = dir_map[self.deg]

    def move(self, dir, num):
        if dir == "N":
            self.vpos += num
        elif dir == "S":
            self.vpos -= num
        elif dir == "E":
            self.hpos += num
        elif dir == "W":
            self.hpos -= num
        else:
            self.move(self.dir, num)
    
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
            self.ship.process_input(command, unit)
        return self.ship.calculate_distance()

s = Solution(content_list)
print(s.move_ship())
        