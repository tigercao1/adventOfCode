myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

buses_str = content_list[1].split(",")

buses = []
offsets = []

offset = 0

for bus in buses_str:

    if bus.isdigit():
        buses.append(int(bus))
        offsets.append(offset)
    offset += 1
    
print(offsets)

def find_min_departure():
    depart_time = [0 for i in range(len(buses))]
    common_multiple = buses[0]
    for i in range(1, len(buses)):
        while True:
            depart_time = [x + common_multiple for x in depart_time]
            if (depart_time[i] + offsets[i]) % buses[i] == 0:
                common_multiple *= buses[i]
                break
    return depart_time[0]
    


print(find_min_departure())

'''

everything move by common multiple
if time % bus1 == 0
common multiple *= bus1



find the scenario where bus1 departs 1 min after bus0

if bus0 < bus1-1 increase bus0 by id0
if bus0 > bus1-1 increase bus1 by id1
else target = bus1

if bus2-1 < bus1 increase bus2 by id2
if bus2-1 == bus1 target = bus2
else back to incrementing bus1 and bus 0

common multiple  = bus[0]

find first bus1 depart x min after bus0

common multiple = bus[1] * bus[0]

increment the prev elements by common multiple until bus[]

'''