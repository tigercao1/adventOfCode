myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()
print(content_list[0])
depart_time = int(content_list[0])
buses_str = content_list[1].split(",")

buses = []

for bus in buses_str:
    if bus.isdigit():
        buses.append(int(bus))

def find_min_departure():
    bus_departure = [0 for i in range(len(buses))]
    while True:
        found = 0
        for i, bus in enumerate(buses):
            if bus_departure[i] < depart_time:
                bus_departure[i] += bus
            else:
                found += 1
        if found >= len(buses):
            break
    min_departure = min(bus_departure)
    return (min_departure - depart_time) * buses[bus_departure.index(min_departure)]
        

print(find_min_departure())
