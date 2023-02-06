# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#Q1
print(len(it_companies))

#Q2
it_companies.add('Twitter')
print(it_companies)

#Q3
multiple_it_companies=['Linkedin', 'Instagram','Telegarm']
it_companies.update(multiple_it_companies)
print(it_companies)

#Q4
it_companies.remove('Apple')
it_companies.discard('Microsoft')
it_companies.pop()
print(it_companies)

#Q5
#remove returns an error if the specified item does not exist in the set
#discard does not return error if the item does not exist in the set

#QLEVEL2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#Q1
A_and_B= A.union(B)
print('A joined with B is: ',A_and_B)

#Q2
print('The common elements in both A and B: ',A.intersection(B))

#Q3
print('Is A subset of B? : ', A.issubset(B))

#Q4
print('Are A and B disjoint sets? : ',A.isdisjoint(B))

#Q5
print(A.union(B))
print(B.union(A))

#Q6
print(A.symmetric_difference(B))

#Q7
del A
del B

#QLEVEL3

age = [22, 19, 24, 25, 26, 24, 25, 24]

#Q1
age_set=set(age)
print('Is the list age greater than the set age_set? : ',len(age)>len(age_set))

#Q2
# A string is a data type that consists of one or more characters.
# A list is an ordered collection of different data types which is modifiable and allows duplicates.
# A tuple is an ordered collection of different data types which is not modifiable and allows duplicates.
# A set is an unordered and un-indexed collection items that does not allows duplicates.

#Q3
sentence=['I','am','a','teacher','and','I','love','to','inspire','and', 'teach','people']
sentence_set=set(sentence)
print('The unique words used in the sentence {}. are:  {}\nAnd their number is: {}'.format(sentence,sentence_set,len(sentence_set)))