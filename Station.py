import sys

input_data = sys.stdin.read().strip()

rows = input_data.split("\n")

city_map = [list(rows[0]), list(rows[1])]



def check(city_map):
    if city_map[0][0] == '#' and city_map[0][1] == '#' and city_map[1][0] == '#' and city_map[1][1] == '#':
        return "Yes"
    if city_map[0][0] == '#' and city_map[0][1] == '#':  
        return "Yes"
    if city_map[1][0] == '#' and city_map[1][1] == '#':  
        return "Yes"
    if city_map[0][0] == '#' and city_map[1][0] == '#':  
        return "Yes"
    if city_map[0][1] == '#' and city_map[1][1] == '#':  
        return "Yes"

    return "No"

print(check(city_map))