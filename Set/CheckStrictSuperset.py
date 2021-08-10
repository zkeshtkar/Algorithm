super_set = set([int(item) for item in input().split()])
number = int(input())
for i in range(number):
    my_set = set([int(item) for item in input().split()])
    if not (len(my_set - super_set) == 0 and len(super_set) > len(my_set)):
        print(False)
        break
else:
    print(True)

