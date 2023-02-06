#Q1
dog=dict()

#Q2
dog['name']='Jack'
dog['color']='Red'
dog['legs']='4'
dog['age']='5'
print(dog)

#Q3
student={
    'first_name':'Abubakar',
    'last_name':'Usman Muhammad',
    'gender':'Male',
    'age':'230',
    'is_married':'True',
    'skills':['corel','Python','C#'],
    'country':'Nigeria',
    'city':'Kano'   
}
print(student)

#q4
print(len(student))

#Q5
print(student['skills'])
print(type(student['skills']))

#Q6
student['skills'].append('HTML')
student['skills'].append('PHP')
print(student['skills'])

#Q7
keys=student.keys()
print(keys)

#Q8
values=student.values()
print(values)

#Q9
print(student.items())

#Q10
student.popitem() #Skills
print(student)

#Q11
del dog