# concatenate
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
print("----------------------------------------")

# operator *
d = 4 *[0]
print(d)
print("----------------------------------------")

e = [1, 2]
f = 5 * e
print(f)
print("----------------------------------------")

# len()
print(len(c))
print("----------------------------------------")

# max()
print(max(c))
print("----------------------------------------")

# min()
print(min(c))
print("----------------------------------------")

# sum()
print(sum(c))
print("----------------------------------------")

print(sum(c)/len(c))
print("----------------------------------------")

myList = list()
while(True):
  inp = input("Enter a number: ")
  if inp == "done":break
  value = float(inp)
  myList.append(value)
average = sum(myList)/len(myList)

print("Average: ", average)