      #Exercise; level 3 question 1
    #example for different python data types
        #Number
a = -20     # integer
b = 5.56    # float
c = 67j     # complex

print(a)
print(b)
print(c)

      # string
name = 'abubakar labaran'

print(name)

      #boolean

a = 5
b = 2

5 > 3    # is True 5 is greater then 3

print(a == b)
print(5 > 3)
  
    #list
list = [1,2,3]

print(list)

    #tuple

tuple = (1,'abubakar',3.4)     #tuple with mixed datatypes

print(tuple)

    #set

number_id = {412, 673, 827, 687, 376}   #a set of integer type

print(number_id)

    #Dictonary

capital_city = {'zamfara': 'gusau', 'oyo': 'ibadan', 'taraba': 'jalingo'}

print(capital_city)


   #Exercise; level 3 question 2
   #find an Euclidian distance

import math
p1 = [2,3]
p2 = [10,8]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

print(distance)