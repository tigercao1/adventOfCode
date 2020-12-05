myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n\n")
myfile.close()

import re

REQUIRED_FIELDS = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
VALID_ECL = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
HCL_PATTERN = re.compile("^#([0-9a-f])+$")

print(1 if HCL_PATTERN.match("#abcd") else -1)

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
        has_all_fields = True
        for field in REQUIRED_FIELDS:
            if field not in passport:
                has_all_fields = False
                break
        if has_all_fields:
            if passport["byr"].isdigit() and passport["iyr"].isdigit() and passport["eyr"].isdigit() and 1920 <= int(passport["byr"]) <= 2002 and \
                2010 <= int(passport["iyr"]) <= 2020 and 2020 <= int(passport["eyr"]) <= 2030 and ((passport["hgt"][-2:] == "cm" and passport["hgt"][:-2].isdigit() and 150 <= int(passport["hgt"][:-2]) <= 193) \
                    or (passport["hgt"][-2:] == "in" and passport["hgt"][:-2].isdigit() and 59 <= int(passport["hgt"][:-2]) <= 76)) and len(passport["hcl"]) == 7 \
                        and HCL_PATTERN.match(passport["hcl"]) and len(passport["pid"]) == 9 and passport["pid"].isdigit() and passport["ecl"] in VALID_ECL:
                        num_valid += 1
    return num_valid


print(is_passport_valid(parse_input(content_list)))

