year=int(input("Введите год: "))
if year %4 ==0 and year%100 !=0:
  print ("Это високосный год!")
elif year%400 ==0: 
  print ("Это високосный год")
else:
  print ("Это обычный год!")