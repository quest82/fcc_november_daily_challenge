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

        

print(infected(25))