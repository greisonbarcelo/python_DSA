# def greetings(name, age=26):
#     print(f"Happy birthday to {name}, you are {age} years old!")


# greetings("Grei")


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
    # return first_name.capitalize() + " " + last_name.capitalize


full_name = create_name("john", "does")

print(full_name)
