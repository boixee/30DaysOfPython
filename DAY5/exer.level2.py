#Q1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Q1A
ages.sort()
min_age=ages[0]
max_age=ages[-1]
print('The sorted list is: ',ages)
print('The min number is: ',min_age)
print('the max number is: ',max_age)

#Q1B
ages.append(min_age)
ages.append(max_age)
print(ages)

#Q1C
median_age=ages[5]+ages[6]/2
print('The median age is {:.2f}: '.format(median_age))

#Q1D
average_sum=ages[0]+ages[1]+ages[2]+ages[3]+ages[4]+ages[5]+ages[6]+ages[7]+ages[8]+ages[9]+ages[10]+ages[11]/12
print('The average is: {:.2f}'.format(average_sum))

#Q1E
range_of_ages=max_age-min_age
print("the range is: ",range_of_ages)

#Q1F
diff_btw_min_and_average=min_age-average_sum
print(abs(diff_btw_min_and_average))
diff_btw_max_and_average=max_age-average_sum
print(abs(diff_btw_max_and_average))