# List is mutable, we can reassing the list
my_list_1 = [1,4,5,6,7]
my_list_1 = [2,3,0,1,5]
print(my_list_1)

# tuple is immutable, we can't reassing the tuple or change the element
my_tuple_1 = (1,4,5,6,7)
my_tuple_1 = (2,3,0,1,5)
my_tuple_1[0] = 0

#both tuples and lists can be nested
my_list_2 = [(1,2),(3,4)]
my_tuple_2 = ([1,2],[3,4])
print(my_list_2)
print(my_tuple_2)