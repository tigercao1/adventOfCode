def process_input(content_list):
    part_ranges = list(item for item in content_list[0].split('\n'))
    part_ranges = list(item.split(' ') for item in part_ranges)
    part_ranges = list(item[-3:] for item in part_ranges)
    part_ranges = list([[int(i) for i in part[0].split('-')], [int(i) for i in part[2].split('-')]] for part in part_ranges)
    part_nearby_tickets = content_list[2]
    part_my_ticket = content_list[1].split('\n')
    part_my_ticket = part_my_ticket[1]
    my_ticket = list(int(x) for x in part_my_ticket.split(','))
    nearby_tickets = part_nearby_tickets.split('\n')
    nearby_tickets = nearby_tickets[1:]
    nearby_tickets = list([int(i) for i in ticket.split(',')] for ticket in nearby_tickets)
    return part_ranges, nearby_tickets, my_ticket

def find_overlapping_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    overlapping_ranges = [ranges[0]]
    for i in range(1, len(ranges)):
        if ranges[i][0] <= overlapping_ranges[-1][1]:
            overlapping_ranges[-1][1] = max(ranges[i][1], overlapping_ranges[-1][1])
        else:
            overlapping_ranges.append(ranges[i])

    return overlapping_ranges

def remove_error_tickets(ranges, tickets):
    valid_tickets = []
    for ticket in tickets:
        in_range = True
        for num in ticket:
            for r in ranges:
                if not r[0] <= num <= r[1]:
                    in_range = False
                else:
                    in_range = True
                    break
            if not in_range:
                break
        if in_range:
            valid_tickets.append(ticket)
    return valid_tickets

class Field:
    def __init__(self, range1, range2, idx):
        self.range1 = range1
        self.range2 = range2
        self.idx = idx

    def check_bound(self, num):
        r1_lower, r1_upper = self.range1[0], self.range1[1]
        r2_lower, r2_upper = self.range2[0], self.range2[1]
        return r1_lower <= num <= r1_upper or r2_lower <= num <= r2_upper

    def __str__(self):
        return [self.range1, self.range2]

def main():
    myfile = open("input.txt", "r")
    content = myfile.read()
    content_list = content.split("\n\n")
    myfile.close()

    ranges, tickets, my_ticket = process_input(content_list)

    combined_ranges = []
    for item in ranges:
        combined_ranges.extend(item)

    # Finds combinded overlapping ranges from all given ranges
    overlapping_ranges = find_overlapping_ranges(combined_ranges)

    valid_tickets = remove_error_tickets(overlapping_ranges, tickets)

    # Append my ticket since it is given valid
    valid_tickets.append(my_ticket)

    # Each ticket field has a range and an index from the given input (ordered by input order)
    for i, r in enumerate(ranges):
        ranges[i] = Field(r[0], r[1], i)
    
    # Each number in the ticket is mapped to a set of field indicies that the number is valid for
    # e.g. ticket 1 field 1 is valid for "departure location", "departure station" -> 1:{0,1}
    ticket_pos_map = {}

    # For every element in every ticket, make a set of field indicies that the number is valid for
    # Union the set with the existing set in the map
    # What we get is a staircase structured sets AFTER SORTING with 1 element difference each step
    for i in range(len(valid_tickets[0])):
        for j in range(len(valid_tickets)):
            matched = set()
            for f in ranges:
                if f.check_bound(valid_tickets[j][i]):
                    matched.add(f.idx)
            if i not in ticket_pos_map:
                ticket_pos_map[i] = matched
            else:
                ticket_pos_map[i] &= matched

    # make a tuple of key:field_set for sorting
    ticket_sets = []
    for key in ticket_pos_map.keys():
        ticket_sets.append((key, ticket_pos_map[key]))
    
    # sort by length of the sets to achieve the staircase structured sets
    ticket_sets.sort(key=lambda x: len(x[1]))

    # Our answer requires the valid fields in our ticket for fields 0-5
    required_field_idx = set([0,1,2,3,4,5])
    matching_fields = []

    p = 0
    counter = 0

    # The first ticket index that contains the required field index is the
    # correct ticket index for the field index
    while len(matching_fields) < len(required_field_idx):
        if required_field_idx & ticket_sets[counter][1]:
            matching_fields.append(ticket_sets[counter][0])
            p += 1
        counter += 1

    # multiply the ticket number of the correct ticket index
    output = 1
    for i in matching_fields:
        output *= my_ticket[i]
    print(output)

main()


'''

map idx to each range

ticket_pos:set(range_idx)

for each element in ticket, make a set with range_idx

union the set with ticket_pos set assign it to ticket_pos

'''