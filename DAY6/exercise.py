#Create an empty tuple
empty_tuple1=tuple()
empty_tuple2=()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters=('Firdausi','Jamila','Khadija')
brothers=('Muhammad','Jafar','Khalid')

#Join brothers and sisters tuples and assign it to siblings
siblings=sisters+brothers
print(siblings)

#How many siblings do you have?
print(len(siblings))

#Modify the siblings tuple
#and add the name of your father and mother and assign it to family_members
family_members=list(siblings)
family_members.append("Abubakar")
family_members.append("Aisha")
family_members=tuple(family_members)
print(family_members)


#Unpack siblings and parents from family_members
family_members=('Firdausi','Khadija','Jamila','Muhammad','Jafar','Khalid','Aubakar','Aisha')
siblings=family_members[0:6]
parents=family_members[6:]
print(siblings)
print(parents)

#Create fruits, vegetables and animal products tuples. 
#Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('banana','orange','mango')
vegetables=('cabbage','lettuce','cucumba')
animal_products_tuples=('milk','meat')
food_stuff_tp=fruits+vegetables+animal_products_tuples
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items=food_stuff_lt[3:5]
print(middle_items)

#Slice out the first three items and the last three items from food_staff_lt list
first_three_items=food_stuff_lt[0:3]
last_three_items=food_stuff_lt[-3:]
print(first_three_items)
print(last_three_items)

#Delete the food_staff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
masters_class_buk=('AI','SE')
print('SE' in masters_class_buk )

print('ALHAMDULILLAH! Day 6 challenge done')