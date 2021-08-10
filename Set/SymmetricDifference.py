first_number = int(input())
first_set = set([int(item) for item in input().split()])
second_number = int(input())
second_set = set([int(item) for item in input().split()])
res = first_set - second_set
res |= second_set - first_set
sored_res = sorted(res)
for item in sored_res:
    print(item)
