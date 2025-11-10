nums = [5, 2, 9, 1, 5, 6]
n = len(nums)
# ascending insertion sort
# for i in range(1, n):
#     insert_index = i
#     current_value = nums.pop(i)
#     for j in range(i-1, -1, -1):
#         if nums[j] > current_value:
#             insert_index = j
#     nums.insert(insert_index, current_value)

# descending insertion sort
# for i in range(1, n):
#     insert_index = i
#     current_value = nums.pop(i)
#     for j in range(i-1, -1, -1):
#         if nums[j] < current_value:
#             insert_index = j
#     nums.insert(insert_index, current_value)

# improved ascending insertion sort
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1, n):
    insert_index = i
    current_value = mylist[i]
    for j in range(i-1, -1, -1):
        if mylist[j] > current_value:
            mylist[j+1] = mylist[j]
            insert_index = j
        else:
            break
    mylist[insert_index] = current_value

# improved descending insertion sort
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1, n):
    insert_index = i
    current_value = mylist[i]
    for j in range(i-1, -1, -1):
        if mylist[j] < current_value:
            mylist[j+1] = mylist[j]
            insert_index = j
        else:
            break
    mylist[insert_index] = current_value

print(mylist)
