test_number = int(input())
for i in range(test_number):
    input()
    first_set = set([int(item) for item in input().split()])
    input()
    second_set = set([int(item) for item in input().split()])
    if first_set & second_set == first_set:
        print(True)
    else:
        print(False)

