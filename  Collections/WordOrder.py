number = int(input())
my_dic = {}
for i in range(number):
    string = input()
    if string in my_dic:
        my_dic[string] += 1
    else:
        my_dic[string] = 1
print(len(my_dic))
for i in my_dic:
    print(my_dic[i], end=" ")
