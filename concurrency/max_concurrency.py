from collections import defaultdict

schedule = [
            (0, 3),
            (3, 5),
            (2, 3),
            (6, 8),
            (10, 12),
            (73, 92),
            (1, 200),
            ]


# Time complexity to get the time where max concurrency happens is O(n^2) for this solution

schedule_dict = defaultdict(lambda: 0)

for start, end in schedule:
    for time in range(start, end):
            schedule_dict[time] += 1

max_concurrency = max(schedule_dict, key=schedule_dict.get)
print(f"Time where max concurrency happens is : {max_concurrency}")


# Time complexity to get the time where max concurrency happens is O(n) for this solution
for start, end in schedule:
    if start <= max_concurrency < end:
        print(f"{(start, end)}")