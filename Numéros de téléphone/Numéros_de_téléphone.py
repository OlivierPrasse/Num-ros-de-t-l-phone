import sys

n = int(input())

root = {}

total_elements = 0

for i in range(n):
    telephone = input()

    current_node = root
    
    for digit in telephone:
        if digit not in current_node:
            current_node[digit] = {}
            total_elements += 1 

        current_node = current_node[digit]

print(total_elements)
