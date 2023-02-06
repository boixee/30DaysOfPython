#QLEVEL1
#Q1
empty_tuple1=tuple()
empty_tuple2=()

#Q2
sisters=('Zainab','Hafsa','Salma')
brothers=('Muhammad','Aliyu','Umar')

#q3
siblings=sisters+brothers
print(siblings)

#q4
print(len(siblings))

#Q5
family_members=list(siblings)
family_members.append("Maryam")
family_members.append("Amina")
family_members=tuple(family_members)
print(family_members)

#QLEVEL2
#Q1
family_members=('Zainab','Hafsa','Salma','Aliyu','Muhammad','Umar','Maryam','Amina')
siblings=family_members[0:6]
parents=family_members[6:]
print(siblings)
print(parents)

#Q2
fruits=('banana','orange','mango')
vegetables=('cabbage','lettuce','cucumba')
animal_products_tuples=('milk','meat')
food_stuff_tp=fruits+vegetables+animal_products_tuples
print(food_stuff_tp)

#Q3
food_stuff_lt=list(food_stuff_tp)

#Q4
middle_items=food_stuff_lt[3:5]
print(middle_items)

#Q5
first_three_items=food_stuff_lt[0:3]
last_three_items=food_stuff_lt[-3:]
print(first_three_items)
print(last_three_items)

#Q6
del food_stuff_tp

#Q7
masters_class_buk=('AI','SE')
print('SE' in masters_class_buk )