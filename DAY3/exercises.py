  #Q1
age = (22)    #integer
   #Q2
height = (54.6)  #float
   #Q3
comp = (2-3j)   #complex
   #Q4
base = float(input(20))
height = float(input(10))
area = 0.5 * 20 * 10
print('area')
  #Q5
a=float(input('Enter side a: '))
b=float(input('Enter side b: '))
c=float(input('Enter side c: '))
perimeter=a+b+c
print('the perimeter of the triangle is: ', perimeter)

  #Q6
width=float(input('Enter the width: '))
length=float(input('Enter the lenght: '))
area_of_rectangle=length*width
perimeter_of_rectangle=2*(length+width)
print('the area of rectangle is: ',area_of_rectangle)
print('the perimeter of rectangle is: ',perimeter_of_rectangle)

#Q7
radius=float(input('Enter the radius of the circle: '))
area_of_circle=3.14*radius*radius
circumference_of_circle=2*3.14*radius
print('the area of the circle is: ',area_of_circle)
print('the circumference is: ',circumference_of_circle)

#Q8
x=float(input('Enter the intercept x: '))
slope1=2*x-2
print("the slope 1 is: ",slope1)

# slope 2 
x1=2
x2=6
y1=2
y2=10
slope2=(y2-y1)/(x2-x1)
print("the slope 2 is: ",slope2)

#Q9
import math
euclidean_dist=math.sqrt((x1-y1)**2+(x2-y2)**2)
print('the euclidean distance is : ',euclidean_dist)

#Q10
print(slope1 is slope2)

#Q11
x=float(input('Enter the value of x: '))
y=(x**2)+(6*x)+9
print('the value of y is : ', y)

#Q12
python_len=len('python')
dragon_len=len('dragon')
print(not python_len is dragon_len)

#Q13
print('on' in 'python' and 'on' in 'dragon')

#Q14
print('jargon' in 'I hope this course is not full of jargon')

#Q15
print('on'not in 'dragon' and 'on' not in 'python')

#Q16
print(str(int(len('python'))))

#Q17
even_num=int(input("enter a number: "))
if even_num%2==0:
    print("the number ",even_num,' is even')
else:
     print("the number ",even_num,' is odd')  

#Q18
print(7//3 is int(2.7))

#Q19
print(type('10') is type(10))

#Q20
print(type(int('9.8')) == type(10))

#Q21
hours=int(input("enter the number of hours: "))
rate_per_hour=int(input("enter the rate per hour: "))
weekly_pay=hours*rate_per_hour
print("Your pay is: ", weekly_pay)

#Q22
age=int(input('how old are you? '))
life_span=age*31536000
print('You hve lived for ',life_span, ' seconds')

#Q23
print(1, 1, 1, 1, 1)
print(2 ,1 ,2 ,4 ,8)
print(3, 1 ,3 ,9 ,27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)
