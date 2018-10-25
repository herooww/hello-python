
message = input ("Enter a comma separated list of numbers:")

x=1 
total = 0
while x < 10:
   if x & 1 :
        
        print(x**2, end= " ")
        total += x
   x += 1

   print ("total=", total)