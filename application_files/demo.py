def action(value1, value2, action):
    if action == "into":
        result = value1*value2
    if action == "add":
        result = value1+value2
    return result


a = 67
b = 50
c = "into"

result = action(a, b, c)
print(result)

# for i in range(0, 5):
#     print(i)
#     if i == 3:
#         print(i,"break")
#         break