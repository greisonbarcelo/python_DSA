nums = [5, 2, 9, 1, 5, 6]
n = len(nums)
# ascending insertion sort
for i in range(1, n):
    insert_index = i
    current_value = nums.pop(i)
    for j in range(i-1, -1, -1):
        if nums[j] > current_value:
            insert_index = j
    nums.insert(insert_index, current_value)

# descending insertion sort
for i in range(1, n):
    insert_index = i
    current_value = nums.pop(i)
    for j in range(i-1, -1, -1):
        if nums[j] < current_value:
            insert_index = j
    nums.insert(insert_index, current_value)


print(nums)
