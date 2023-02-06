#Declare an empty list
empty_list1=list()
empty_list2=[]

#Declare a list with more than 5 items
lis=[8,9,10,11,12,13,14,15,16]

#Find the length of your list
print(len(lis))

#Get the first item, the middle item and the last item of the list
first_item=lis[0]
middle_item=lis[4]
last_item=lis[-1]
print('The first item in the list is {} :'.format(first_item))
print('The middle item in the list is {} :'.format(middle_item))
print('The last item in the list is {} :'.format(last_item))

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Auwal',250,12.5,"single",'06. Masallacin Jumu\'a Kaura']
print(mixed_data_types)

#Declare a list variable named it_companies and assign initial values
#Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Print the list using print()
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company
first_company=it_companies[0]
middle_company=it_companies[3]
last_company=it_companies[-1]
print('The first company in the list is {} :'.format(first_company))
print('The middle company in the list is {} :'.format(middle_company))
print('The last company in the list is {} :'.format(last_company))

#Print the list after modifying one of the it_companies
it_companies[0]='Tweeter'
print(it_companies)

#Add an IT company to it_companies
it_companies.append('Telegram')
print(it_companies)

#Insert an IT company in the middle of the companies list
it_companies.insert(4,'LinkedIn')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0].upper()
print(it_companies)

#Join the it_companies with a string '#;  
print('#'.join(it_companies))

#Check if a certain company exists in the it_companies list.
print('Telegram' in it_companies)

#Sort the list using sort() method
it_companies.sort()
print(it_companies)


#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#Slice out the first 3 companies from the list
first_three=it_companies[0:3]
print(first_three)

#Slice out the last 3 companies from the list
last_three=it_companies[-3:]
print(last_three)

#Slice out the middle IT company or companies from the list
middle=it_companies[4]
print(middle)

#Remove the first IT company from the list
it_companies.remove('Tweeter')
print(it_companies)

#Remove the middle IT company or companies from the list
it_companies.remove('LinkedIn')
print(it_companies)

#Remove the last IT company from the list
it_companies.remove('Amazon')
print(it_companies)

#Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#Destroy the IT companies list#
del it_companies

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list= front_end + back_end
print(joined_list)

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack.
#Then insert Python and SQL after Redux.
full_stack= joined_list.copy()
full_stack.insert(5,'python')
full_stack.insert(6,'SQL')
print(full_stack)