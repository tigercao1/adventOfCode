myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n\n")
myfile.close()

REQUIRED_FIELDS = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

def parse_input(arr):
    parsed = []
    for passport in arr:
        segment = passport.split("\n")
        item = []
        for part in segment:
            item += part.split(" ")
        passport_dict = dict(i.split(":") for i in item)
        parsed.append(passport_dict)
    return parsed

def is_passport_valid(passports):
    num_valid = 0
    for passport in passports:
        is_valid = True
        for field in REQUIRED_FIELDS:
            if field not in passport:
                is_valid = False
                break
        if is_valid:
            num_valid += 1
    return num_valid


print(is_passport_valid(parse_input(content_list)))

