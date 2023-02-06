concatenated_string1= 'Thirty '+'Days '+'Of '+'Python'
print(concatenated_string1)

concatenated_string2='Coding '+'For '+'All'
print(concatenated_string2)

company="Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

first_word=company[0:6]
print(first_word)

print(company.index('Coding'))
print(company.replace('Coding','python'))

challenge='Python For Everyone'
print(challenge.replace('Everyone','all'))

print(company.split(' '))

giant_tech_companies="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(giant_tech_companies.split(','))

print(company[0])
print(company[-1])
print(company[10])

acronym1=challenge[0:14:7]
print(acronym1)

acronym2=company[0:12:7]
print(acronym2)

print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rfind('because'))
slice_because=sentence[31:54]
print(slice_because)

print(company.startswith('Coding'))
print(company.endswith('Coding'))

sentence2='   Coding For All      ' 
print(sentence2.strip(' '))

variable1='30DaysOfPython'
variable2='thirtyDaysOfPython'
print(variable1.isidentifier())
print(variable2.isidentifier())

python_libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))

print('I am enjoying this challenge. \nI just wonder what is next.')

print('name\tage\tcountry\tcity')
print('Abubakar\t220\tNigeria\tKano')

#formatting strings
radius = 10
area = 3.14 * radius ** 2
print('the area of the circle with the radius {} is {:2f} meters square'.format(radius,area))

print(f'{8}+{6}={8+6}')
print(f'{8}-{6}={8-6}')
print(f'{8}*{6}={8*6}')
print(f'{8}+{6}={8+6}')
print(f'{8}/{6}={8/6:2f}')
print(f'{8}%{6}={8%6}')
print(f'{8}//{6}={8//6}')
print(f'{8}**{6}={8**6}')
