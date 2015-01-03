import datetime

day = [0] * 7
for year in range(400):
  d = datetime.date(year+1, 1, 1)
  day[d.weekday()] += 1
  
for i in range(7):
  print day[i]
