shoppingList = ['Milk','Cheese','Butter']

print(shoppingList[0])
print('Bread' in shoppingList)

print("------------------------------------------")

for i in range(len(shoppingList)):
  shoppingList[i] = shoppingList[i] + "+"
  print(shoppingList[i])

print("------------------------------------------")

empty = []
for i in empty:
  print("I am empty")  