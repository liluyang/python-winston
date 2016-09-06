def listReverse(ListPar1):
  x = []
  for y in ListPar1:
    print y
    x.insert(0,y)
    print x
  return x

a = [1, 2]
list2 = listReverse(a)
print list2