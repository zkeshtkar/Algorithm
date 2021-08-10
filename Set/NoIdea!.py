_ = input().split(' ')
my_list = ([int(i) for i in input().split(' ')])
first_set = set([int(i) for i in input().split(' ')])
second_set = set([int(i) for i in input().split(' ')])
p = 0
for i in my_list:
    if i in first_set:
        p += 1
    if i in second_set:
        p -= 1
print(p)
