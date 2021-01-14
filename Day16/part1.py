def process_input(content_list):
    part_ranges = list(item for item in content_list[0].split('\n'))
    part_ranges = list(item.split(' ') for item in part_ranges)
    part_ranges = list(item[-3:] for item in part_ranges)
    part_ranges = list([[int(i) for i in part[0].split('-')], [int(i) for i in part[2].split('-')]] for part in part_ranges)
    part_nearby_tickets = content_list[2]
    nearby_tickets = part_nearby_tickets.split('\n')
    nearby_tickets = nearby_tickets[1:]
    nearby_tickets = list([int(i) for i in ticket.split(',')] for ticket in nearby_tickets)
    ranges = []
    for item in part_ranges:
        ranges.extend(item)
    return ranges, nearby_tickets

def find_overlapping_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    overlapping_ranges = [ranges[0]]
    for i in range(1, len(ranges)):
        if ranges[i][0] <= overlapping_ranges[-1][1]:
            overlapping_ranges[-1][1] = max(ranges[i][1], overlapping_ranges[-1][1])
        else:
            overlapping_ranges.append(ranges[i])

    return overlapping_ranges

def find_scanning_error_rate(ranges, tickets):
    error_rate = 0
    for ticket in tickets:
        for num in ticket:
            in_range = False
            for r in ranges:
                if r[0] <= num <= r[1]:
                    in_range = True
                    break
            if not in_range:
                error_rate += num
    return error_rate

def main():
    myfile = open("input.txt", "r")
    content = myfile.read()
    content_list = content.split("\n\n")
    myfile.close()

    ranges, tickets = process_input(content_list)
    print(find_scanning_error_rate(find_overlapping_ranges(ranges), tickets))

main()

