def reverse(strng):
  if len(strng) == 0:
    return ""
  else:
    return strng[len(strng)-1] + reverse(strng[:len(strng)-1])
    
print(reverse('python'))
# str = 'python'    
# print(str[:len(str)-1])
