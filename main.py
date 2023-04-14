prompt1 = input("Do you want to add, subtract, multiply, divide, or exponents? THIS IS CASE SENSITIVE").lower()

if prompt1 == 'add':
    q = input("First number:")
    w = input("Second number:")
    result = float(q) + float(w)
    print (result)
elif prompt1 == 'subtract':
    e = input("First number:")
    r = input("second number:")
    result1 = float(e) - float(r)
    print (result1)
elif prompt1 == 'multiply':
    t = input("First number:")
    y = input("Second number:")
    result2 = float(t) * float(y)
    print (result2)
elif prompt1 == 'divide':
  u = input("first number:")
  i = input("second number:")
  result3 = float(u) / float(i)
  print (result3)
  print ("Reminder", float(u) % float(i) )
elif prompt1 == 'exponents':
  x = input("What number will be raised to the power?:")
  y = input("What power is your number being raised to?")
  result4 = float(x)**float(y)
  print ("this is your answer:", result4)
else:
  print("not valid")


