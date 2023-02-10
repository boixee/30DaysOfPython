#QLEVEL1
#Q1
def add_two_numbers ():
    num_one = 5
    num_two = 6
    total = num_one + num_two
    print(total)
add_two_numbers()

#Q2
def area_of_a_circle (r):
    pi = 3.14
    Area = pi * r ** 2
    return Area 
print(area_of_a_circle(5))


#Q3
def add_all_nums(*arg):
    sum_all = sum(arg)
    return sum_all
print(add_all_nums(1,2,3,4,5,6,6,7,5))

#Q4
def convert_celsius_to_fahrenheit(c):
    F = str(( c * (9/5)) + 32) + "°F"
    return F 
print(convert_celsius_to_fahrenheit(10))

#Q5
def check_season(month):
    month = month.lower()
    month_list = [
        "january","febuary",
        "march","april","may",
        "june","july","august",
        "september","octomber",
        "november","december"
    ]
    season_dict = {
        "january":"Autumn",
        "febuary":"Autumn",
        "march":"Winter",
        "april":"Winter",
        "may":"Winter",
        "june":"Spring",
        "july":"Spring",
        "august":"Spring",
        "september":"Autumn",
        "octomber":"Winter",
        "november":"Summer",
        "december":"Autumn",
    }

    if month in month_list:
        return "The season of {}".format(season_dict[month])
    else:
        return "the month is not entered in full"

print(check_season("enter month here"))

#Q6
def calculate_slope(m,c):
    y= str(m)+"x" + " + " + str(c) 
    return "y = " + y
print(calculate_slope(7,1))

#Q7
def solve_quadratic_equation(a,b,c,x):
    quadratic_equation = a*x*x + b*x + c
    return "quadratic_soln = ", quadratic_equation
print(solve_quadratic_equation(4,6,3,1))


#Q8
def print_list(g):
    for j in list(g):
        print(j)
print(print_list([4,5,2,6,7]))

#Q9
["C", "B", "A"]
def reverse_list(lst):
    reverse_lst = []
    for j in lst:
        reverse_lst.insert(0,j)
    return reverse_lst
print(reverse_list(["A", "B", "C"]))
print(reverse_list([1, 5, 2, 7, 6]))

#Q10
def capitalize_list_items(lst):
    cap_lst = []
    for j in lst:
        cap_lst.append(j.upper())
    return cap_lst
print(capitalize_list_items(["finland", "canada", "australia"]))

#Q11
def add_item(items,item):
    items.append(item)
    return items
print(add_item([2, 3, 7, 9], 5))
print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Meat'))

#Q12
def remove_item(items,item):
    items.remove(item)
    return items
print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Mango'))
print(remove_item([2, 3, 7, 9], 3))

#Q13
def sum_of_numbers(num):
    sum_num = 0
    for i in range(num+1):
        sum_num = sum_num + i
    return sum_num
print(sum_of_numbers(5)) 
print(sum_of_numbers(10)) 
print(sum_of_numbers(100))

#Q14
def sum_of_odds(num):
    sum_odds = 0
    for j in range(num+1):
        if j % 2 != 0:
            sum_odds = sum_odds + j
    return sum_odds

#Q15
def sum_of_even(nums):
    sum_of_even = 0
    for j in range(nums+1):
        if j % 2 != 0:
            sum_of_even = sum_of_even + j
    return sum_of_even


#QLEVEL2
#Q1
def evens_and_odds(n):
    list_of_even = []
    list_of_odds = []
    for i in range(n+1):
        if i % 2 != 0:
            list_of_even.append(i)
            nums_of_even = len(list_of_even)
        else:
            list_of_odds.append(i)
            nums_of_odds = len(list_of_odds)
    return 'nums_of_even = ',list_of_even,'\n num_of_odds = ',list_of_odds

#Q2
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
print(factorial(5))
print(factorial(2))

#Q3
def is_empty(empty=None):
    if empty == None:
        print("is empty")
    else:
        print("is not empty")
print(is_empty())
print(is_empty(5))

#Q4
def calculate_mean(num):
    sum_num = sum(num)/len(num)
    return sum_num
print(calculate_mean([1,1,1,2,3,3,4,4]))

    
def calculate_meadian(lst):
    lst.sort()
    if len(lst) % 2 == 1:
        return lst[len(lst)//2]
    else:
        return (lst[(len(lst)//2)-1] + lst[len(lst)//2])/2
print(calculate_meadian([1,1,1,2,3,3,4,4]))

    
from collections import Counter
def calculate_mode(myList):
    n = len(myList)  
    data = Counter(myList) 
    get_mode = dict(data) 
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
    if len(mode) == n: 
        get_mode = "No mode found"
    else: 
        get_mode = ' , '.join(map(str, mode)) 
    return(get_mode)

print (calculate_mode(['a','b','b','c','c']))


def calculate_range(*numb):
    numbe = []
    for i in numb:
        numbe.append(i)
    range_ = max(numbe) - min(numbe)
    return range_
print(calculate_range(4,4,4,5))

    
def calculate_variance(lst,calculate_mean):
    b=[]
    for i in lst:
        b.append(i - calculate_mean(lst))
    return sum(b)
print(calculate_variance([1,1,1,2,3,4,4],calculate_mean))

def calculate_std(lst,calculate_mean,calculate_variance):
    return calculate_variance(lst,calculate_mean) * 0.5
 
#QLEVEL3
#Q1
def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
        
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
            else:
                print(num, "is a prime number")
                break
    else:
        print(num, "is not a prime number")

#Q2
def unique(test_list):

    print("The original list is : " + str(test_list))

    flag = True

    for i in test_list:
        if test_list.count(i) > 1:
            flag = False
            break

    if(flag):
       return "List contains all unique elements"
    else:
       return "List contains does not contains all unique elements"
print(unique([1, 3,3, 4, 6, 7]))

#Q3
def items_types(lst):
    items =[]
    for i in lst:
        items.append(type(i))
    return items
print(items_types(["!", "ba",3, 4, 6, 7]))

#Q4
def is_variable(name=None):
    if f'{name}'.isidentifier() == True:
        return 'it is a variable'
    else:
        return 'it is not a variable'
print(is_variable("WA"))
print(is_variable("12"))