

def infected(days):
    patch_days = range(3, days + 1, 3)
    print(list(patch_days))

    total = 1
    for num in range(1, days + 1):
        total = total * 2
        print(f'Total at day {num}:', total)

        if num in patch_days:
           patched = total - round(total * 0.2)
           total = patched
           print(f'Patched at day {num}:', patched)


    return total

        

print(infected(25))