
#To print the hollow square of n lines
lines = int(input('Enter lines of the hollow Square: '))

for i in range(lines):
   for j in range(lines):
      if i == 0 or i == lines-1 or j == 0 or j == lines-1:
         print("*", end=" ")
      else:
         print(" ", end=" ")
   print("\r")