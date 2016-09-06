import types

def flatten(x):
  res = []
  for item in x:
    if type(item) is list:
      res += flatten(item)
    else:
      res.append(item)
  return res

def flatten2(x):#7
  y=[]
  for z in x:
    print x
    print y
    if type(z) is types.ListType:
      y += flatten(z)
    else:
      y.append(z)
  return y


#m=["Hi","my",["name","is"],"Winston."]
m = [1, 2, [3, 4], [], 5, [6, 7, [8, 9]]]
n=flatten2(m)
print n