#Create an empty dictionary called dog
dog=dict()

#Add name, color, breed, legs, age to the dog dictionary
dog['name']='Captain'
dog['color']='Ox blood'
dog['legs']='4'
dog['age']='5'
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, 
#marital status, skills, country, city
#and address as keys for the dictionary
student={
    'first_name':'Abubakar',
    'last_name':'Auwal Khalid',
    'gender':'Male',
    'age':'150',
    'is_married':'True',
    'skills':['Java','Python','R','C#'],
    'country':'Nigeria',
    'city':'Kaura Namoda'   
}
print(student)

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

#Modify the skills values by adding one or two skills
student['skills'].append('Java Script')
student['skills'].append('HTML')
student['skills'].append('PHP')
print(student['skills'])

#Get the dictionary keys as a list
keys=student.keys()
print(keys)

#Get the dictionary values as a lis
values=student.values()
print(values)

#Change the dictionary to a list of tuples using items() method
print(student.items())

#Delete one of the items in the dictionary
student.popitem() #city removed
print(student)

#Delete one of the dictionaries
del dog
#print(dog)

print("Alhamdulillah! Day 8 challenge done!")