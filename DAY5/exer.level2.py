#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
min_age=ages[0]
max_age=ages[-1]
print('The sorted list is: ',ages)
print('The min number is: ',min_age)
print('the max number is: ',max_age)

#Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

#Find the median age (one middle item or two middle items divided by two)
median_age=ages[5]+ages[6]/2
print('The median age is {:.2f}: '.format(median_age))

#Find the average age (sum of all items divided by their number )
average_sum=ages[0]+ages[1]+ages[2]+ages[3]+ages[4]+ages[5]+ages[6]+ages[7]+ages[8]+ages[9]+ages[10]+ages[11]/12
print('The average is: {:.2f}'.format(average_sum))

#Find the range of the ages (max minus min)
range_of_ages=max_age-min_age
print("the range is: ",range_of_ages)

#Compare the value of (min - average) and (max - average), use abs() method
diff_btw_min_and_average=min_age-average_sum
print(abs(diff_btw_min_and_average))
diff_btw_max_and_average=max_age-average_sum
print(abs(diff_btw_max_and_average))

#Find the middle country(ies) in the countries list