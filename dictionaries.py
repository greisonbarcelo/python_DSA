config = {
    "color": "green",
    "width": 42,
    "height": 100,
    "font": "Courier",
}

# Access a value through its key
# config["color"]
# 'green'

# # Update a value
# config["font"] = "Helvetica"


# print(config["font"])
# print(config["width"])

# print(config.get("color"))

# if config.get("color"):
#     print(f"color exists with value: ", config.get("color"))
# else:
#     print("That key doesn't exist")


config.update({"keytest": "valuetest"})
config.update({"color": "red"})
config["color"] = "blue"

# config.pop("keytest")
# config.popitem()
# config.clear()

# keys = config.keys()

# # for key in config.keys():
# #     print(key)  # just return the key
# #     # print(config.get(key))  # get the value
# print(keys)
# # # print(config)
# # # # print(config["keytest"])
# # # print(config.get("keytesta"))


# values = config.values()
# print(values)

# for value in config.values():
#     print(value)

items = config.items()
print(items)

for key, value in config.items():
    print(f"{key}:  {value}")
    # print(key, value)
