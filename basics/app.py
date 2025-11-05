count = 0

for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)

print(f"We have {count} even numbers!")


def greet_user(first_name, last_name):
    print(f"Hi there, {first_name} {last_name}")
    print("welcome aboard")


greet_user("Greison", "Kei")
greet_user("John", "Doe")
greet_user("johnny")
