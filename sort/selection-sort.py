# mylist = [64, 34, 25, 5, 22, 11, 90, 12]
# n = len(mylist)

# for i in range(n-1):
#     min_index = i
#     for j in range(i+1, n):
#         if mylist[j] < mylist[min_index]:
#             min_index = j
#     min_value = mylist.pop(min_index)
#     mylist.insert(i, min_value)

# print(mylist)


# mylist = [64, 34, 25, 5, 22, 11, 90, 12]
# n = len(mylist)

# min_value = mylist.pop(1)
# mylist.insert(0, min_value)


# print(mylist)

# improved selectionsort by swapping instead of pop and insert causing shift down on pop and shift up on insert across array
mylist = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(mylist)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if mylist[j] < mylist[min_index]:
            min_index = j

    mylist[min_index], mylist[i] = mylist[i], mylist[min_index]


print(mylist)
