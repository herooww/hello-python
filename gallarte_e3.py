
data = input ("Enter a comma separated list of numbers:")
real_numbers= data.split(",")


total = 0.0
for x in range(len(real_numbers)):
    G = float(real_numbers[x])
    total+= G * G 
   
print ("sum of squares=", total)