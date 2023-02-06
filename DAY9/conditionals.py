#30DaysOfPythonChellenge
#Day9
#Excercise 1
#Q1
age=int(input('Enter your age: '))
if age<=0:
    print('Invalid age!')
elif age>=18:
    print('Your are old enough to drive')
else:
    print('You need {} more years to learn to drive'.format(18-age))

#Q2
my_age=22
your_age=int(input('Enter your age: '))

if your_age>0:
   if your_age>my_age:
    diff=your_age-my_age
    if diff==1:
        print('You are 1 year older than me')
    else:
        print('You are {} years older than me'.format(diff))

   elif your_age==my_age:
    print('We are age mates')
   else:
    diff2=my_age-your_age
    if diff2==1:
        print('I am 1 year older than you')
    else:
        print('I am {} years older than you'.format(diff2))

else:
    print('Invalid age')


#Q3
a=int(input('Enter number one:'))
b=int(input('Enter number two:'))

if a>b:
    print('{} is greater than {}'.format(a,b))
elif a<b:
      print('{} is smaller than {}'.format(a,b))
else:
       print('{} is eqauals to {}'.format(a,b))



  #Excercise 2
  #Q1
score=int(input('Enter the student\'s score: '))

if score<=100:
    if score>=80:
        print('A')
    elif score>=70:
        print('B')
    elif score>=60:
        print('C')
    elif score>=50:
        print('D')
    else:
        print('F')
else:
    print('No score morethan 100')

#Q2
Autumn=['September', 'October', 'November']
Winter=['December', 'January', 'February']
Spring=['March', 'April', 'May']
Summer=['June', 'July', 'August']

month=(input('Enter the month: ')).capitalize()
if month in Autumn:
    print(' Hi! It is Autumn')
elif month in Winter:
    print(' Hi! It is Winter')
elif month in Spring:
    print(' Hi! It is Spring')
elif month in Summer:
      print(' Hi! It is Summer')
else:
    print('Invalid month')


#Q3
fruits = ['banana', 'orange', 'mango', 'lemon']
add_fruit=input('Add a fruit you like into the list of fruits: ').lower()
if add_fruit in fruits:
    print('The fruit already exists in the list')
else:
    fruits.append(add_fruit) 
    print(fruits)

    #Exercise 3


person={
    'first_name': 'Abubakar',
    'last_name': 'Labaran',
    'age': 22,
    'country': 'Nigeria',
    'is_married': False,
    'skills': ['HTML','CSS', 'Photoshop', 'CorelDraw', 'Python'],
    'address': {
        'street': 'Rijiyarzaki',
        'zipcode': '073563'
    }
    }

    #Check if the person dictionary has skills key, 
    #if so print out the middle skill in the skills list.
if 'skills' in person:
    skills_length=len(person['skills'])
    if skills_length%2==0:
        middle_element=person['skills'][int(((skills_length/2)-1)) : int(((skills_length/2))+1)] 
        print('The middle element(s) :',middle_element)
    else:
        middle_element2=person['skills'][skills_length//2] 
        print('The middle element(s) :',middle_element2)

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill
# and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print(person['skills'])
    else:
        print('Not proficient in python')

#If a person skills has only JavaScript and React, print('He is a front end developer'),
#if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
#if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
# else print('unknown title') - for more accurate results more conditions can be nested!
if 'JavaScript' in person['skills'] and 'React' in person['skills']:
       print('He is a front end developer')
elif 'Node' in person['skills'] and 'python' in person['skills'] and 'MangoDB' in person['skills']:
    print('He is a backend developer')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MangoDB' in person['skills']:
    print('He is a fullstack developer')
else:
    print('Unknown title!')

 #If the person is married and if he lives in Finland, 
 # print the information in the following format:
if person['is_married']==True and person['country']=='Finland':
    print('{} {} is married. He lives in {}'.format(person['first_name'],person['last_name'],person['country']))

print("Alhamdulillah! Done with day 9 challenge")
print("This challenge is cool")