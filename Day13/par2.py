myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

buses_str = content_list[1].split(",")

buses = []
offsets = []

offset = 1

for bus in buses_str:

    if bus.isdigit():
        buses.append(int(bus))
        offsets.append(offset)
        offset = 1
    else:
        offset += 1
    
print(offsets)

def find_min_departure():
    bus_departure = [0 for i in range(len(buses))]
    target = -1
    latest = -1
    while latest < len(buses)-1:
        if target == -1:
            time0, time1 = find_one_up(buses[0], buses[1], bus_departure[0], bus_departure[1], offsets[1])
            bus_departure[0], bus_departure[1] = time0, time1
            target = time1
        else:
            for i in range(2, len(buses)):
                next_time = buses[i] + bus_departure[i]

                while True:
                    if next_time-offsets[i] < target:
                        next_time += buses[i]
                    elif next_time-offsets[i] == target:
                        target = next_time
                        bus_departure[i] = next_time
                        latest = i
                        break
                    else:
                        target = -1
                        break
                if target == -1:
                    break
        print(bus_departure[0])

    return bus_departure[0]



def find_one_up(bus0, bus1, time0, time1, offset):
    time0 += bus0
    time1 += bus1
    
    while True:
        if time0 < time1-offset:
            time0 += bus0
        elif time0 > time1-offset:
            time1 += bus1
        else:
            return time0, time1


print(find_min_departure())

'''
find the scenario where bus1 departs 1 min after bus0

if bus0 < bus1-1 increase bus0 by id0
if bus0 > bus1-1 increase bus1 by id1
else target = bus1

if bus2-1 < bus1 increase bus2 by id2
if bus2-1 == bus1 target = bus2
else back to incrementing bus1 and bus 0



'''