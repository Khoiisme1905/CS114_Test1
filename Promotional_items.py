import sys
import re

input_data = sys.stdin.read().strip().split("\n")

item_prices = list(map(int, input_data[0].split()))

savings_info = input_data[1:-1]

budget = int(input_data[-1])

total_online_cost = sum(item_prices)

total_instore_cost = 0

for i, info in enumerate(savings_info):
    price = item_prices[i]
    match_lower = re.search(r"(\d+(\.\d+)?)% lower than in-store", info)
    match_higher = re.search(r"(\d+(\.\d+)?)% higher than in-store", info)
    
    if match_lower:
        savings_percentage = float(match_lower.group(1))
        total_instore_cost += price / (1 - savings_percentage / 100)
    elif match_higher:
        savings_percentage = float(match_higher.group(1))
        total_instore_cost += price * (1 + savings_percentage / 100)
    else:
        total_instore_cost += price

can_afford_online = total_online_cost <= budget
can_afford_instore = total_instore_cost <= budget

# Output result
print("true" if can_afford_online or can_afford_instore else "false")