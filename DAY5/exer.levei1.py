#Q1
empty_list1=list()
empty_list2=[]

#Q2
lis=[8,9,10,11,12,13,14,15,16]

#Q3
print(len(lis))

#Q4
first_item=lis[0]
middle_item=lis[4]
last_item=lis[-1]
print('The first item in the list is {} :'.format(first_item))
print('The middle item in the list is {} :'.format(middle_item))
print('The last item in the list is {} :'.format(last_item))

#Q5
mixed_data_types=['Abubakar',220,11.5,"single",'Rijiyarzaki kano']
print(mixed_data_types)

#Q6
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Q7
print(it_companies)

#Q8
print(len(it_companies))

#Q9
first_company=it_companies[0]
middle_company=it_companies[3]
last_company=it_companies[-1]
print('The first company in the list is {} :'.format(first_company))
print('The middle company in the list is {} :'.format(middle_company))
print('The last company in the list is {} :'.format(last_company))

#Q10
it_companies[0]='Tweeter'
print(it_companies)

#Q11
it_companies.append('Telegram')
print(it_companies)

#Q12
it_companies.insert(4,'LinkedIn')
print(it_companies)

#Q13
it_companies[0].upper()
print(it_companies)

#Q14
print('#'.join(it_companies))

#Q15
print('Telegram' in it_companies)

#Q16
it_companies.sort()
print(it_companies)


#Q17
it_companies.reverse()
print(it_companies)

#Q18
first_three=it_companies[0:3]
print(first_three)

#Q19
last_three=it_companies[-3:]
print(last_three)

#Q20
middle=it_companies[4]
print(middle)

#Q21
it_companies.remove('Tweeter')
print(it_companies)

#Q22
it_companies.remove('LinkedIn')
print(it_companies)

#Q23
it_companies.remove('Amazon')
print(it_companies)

#Q24
it_companies.clear()
print(it_companies)

#Q25
del it_companies

#Q26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list= front_end + back_end
print(joined_list)

#Q27
full_stack= joined_list.copy()
full_stack.insert(5,'python')
full_stack.insert(6,'SQL')
print(full_stack)