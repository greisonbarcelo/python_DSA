# mylist = [64, 34, 25, 12, 22, 11, 90, 5]
mylist = [7, 3, 9, 12, 11]

n = len(mylist)

print(f"0 Run {mylist}")
for i in range(n-1):
    switched = False
    for j in range(n-i-1):
        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            switched = True
    print(f" {i+1} Run {mylist}")
    if switched:
        break

print(f"Final {mylist}")
