def capitalizeFirst(arr):
    for el in arr:
        first_letter = el[0].capitalize()
        rest = el[1:]
        el = first_letter + rest
    return arr    

print(capitalizeFirst(['car', 'taco', 'banana']))            