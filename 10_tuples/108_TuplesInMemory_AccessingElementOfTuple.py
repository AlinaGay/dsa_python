new_tuple = ('a','b','c','d','e')

print(new_tuple[1])
print(new_tuple[-2])
print(new_tuple[:])
print(new_tuple[1:3])

new_tuple[0] = 'f' # doesn't work, because tuple is immutable