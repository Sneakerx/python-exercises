"""Print Every Second Element from Index 1"""

my_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
start_index = 1
step = 2
for i in range(start_index, len(my_list), step):
    print(my_list[i])

# Output: 11, 13, 15, 17, 19
