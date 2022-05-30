def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
l=eval(input("enter the list"))
print(unique_list(l))
