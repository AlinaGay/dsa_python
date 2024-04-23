str_1 = 'spam'
list_1 = list(str_1)
print(list_1)

str_1 = 'spam1-spam2-spam3'
delimeter = '-'
list_2 = str_1.split(delimeter)
print(list_2)
print(delimeter.join(list_2))