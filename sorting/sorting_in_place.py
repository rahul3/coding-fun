input_list = ['G', 'B', 'R', 'R', 'B', 'R', 'G']

# Convert to ASCII
input_list.sort(key=lambda x: ord(x), reverse=True)

print(input_list)