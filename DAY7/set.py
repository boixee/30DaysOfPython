# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
multiple_it_companies=['Linkedin', 'Instagram','Telegarm']
it_companies.update(multiple_it_companies)
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Apple')
it_companies.discard('Microsoft')
it_companies.pop()
print(it_companies)

#What is the difference between remove and discard:
#remove returns an error if the specified item does not exist in the set
#while, discard does not return error if the item does not exist in the set

#QLEVEL2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#Join A and B
A_and_B= A.union(B)
print('A joined with B is: ',A_and_B)

#Find A intersection B
print('The common elements in both A and B: ',A.intersection(B))

#Is A subset of B
print('Is A subset of B? : ', A.issubset(B))

#Are A and B disjoint sets
print('Are A and B disjoint sets? : ',A.isdisjoint(B))

#Join A with B and B with A
print(A.union(B))
print(B.union(A))

#What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#Delete the sets completely
del A
del B

#QLEVEL3

age = [22, 19, 24, 25, 26, 24, 25, 24]

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set=set(age)
print('Is the list age greater than the set age_set? : ',len(age)>len(age_set))

#Explain the difference between the following data types: string, list, tuple and set:
# A string is a data type that consists of one or more characters.
# A list is an ordered collection of different data types which is modifiable and allows duplicates.
# A tuple is an ordered collection of different data types which is not modifiable and allows duplicates.
# A set is an unordered and un-indexed collection items that does not allows duplicates.

#I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence?
#  Use the split methods and set to get the unique words.
sentence=['I','am','a','teacher','and','I','love','to','inspire','and', 'teach','people']
sentence_set=set(sentence)
print('The unique words used in the sentence {}. are:  {}\nAnd their number is: {}'.format(sentence,sentence_set,len(sentence_set)))

print("ALHAMDULILLAH. done with day 7 !!")