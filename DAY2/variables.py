    #Day 2: 30 Days of python programming
first_name = ('abubakar')              #str
last_name = ('labaran')                #str
full_name = ('abubakar labaran')        #str
country = ('nigeria')                  #str
city = ('kano')                         #str
age = (23)                             #int
year = (2023)                          #int
is_married = False                    #bool
is_true = ('no')                       #str
is_light = ('yes')                    #str
name, surname, middle_name = ('abubakar','labaran','salisu')         #set

      #checking the data type of all the variables

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type({name, surname, middle_name}))

       #find len of the first name
print(len(first_name))
       #compare length of first name and last name
print(len(first_name) + len(last_name))

num_one = 5
num_two = 4
total = 9
diff = -1
product = 20
division = 1.25
remainder = 1
exp = 625
floor_division = 1

     #using the built in input
first_name = input('whats your first name:')
last_name = input('whats your last name:')
country = input('which country are you from?')
age = input('how old are you?')

print(first_name)
print(last_name)
print(country)
print(age)
