from math import ceil

def infected(days):
    patch_days = range(3, days + 1, 3)

    total = 1
    for num in range(1, days + 1):
        total = total * 2

        if num in patch_days:
           patched = total - ceil(total * 0.2)
           total = patched


    return total


# AI alternate compact code


# def infected(days):
#     total = 1
#     for day in range(1, days + 1):
#         total *= 2
#         if day % 3 == 0:
#             total -= math.ceil(total / 5)
#     return total
        

print(infected(25))