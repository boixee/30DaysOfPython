#QLEVEL1
#Q1
import random
import string
def random_user_id():
    return "".join(str(random.choice(string.ascii_letters + string.digits)) for i in range(6))

print(random_user_id())     #'1ee33d'


#Q2
["".join(str(random.choice(string.ascii_letters + string.digits)) for i in range(6)) for j in range(6)]
def random_user_id_gen_by_user():
    a = int(input("Enter the number of characters: "))
    b = int(input("Enter the number of IDs: "))
    return ["".join(str(random.choice(string.ascii_letters + string.digits)) for i in range(a)) for j in range(b)]


#Q3
def rgb_color_gen():
    a = ','.join(str(random.randint(0,255)) for i in range(3))
    return 'rgb('+ a + ')'
print(rgb_color_gen())



#QLEVEL2
#Q1
def list_of_hexa_colors(x):
     a= ["".join(str(random.choice('abcdef' + string.digits)) for i in range(6)) for j in range(x)]
     b =['#' + item for item in a]
     return b
list_of_hexa_colors(6)

#Q2
def list_of_rgb_colors(x):
    return [rgb_color_gen() for i in range(x)]

list_of_rgb_colors(7)

string.digits

#Q3

def generate_colors(fun,x):
    if fun == 'hexa':
        result = list_of_hexa_colors(x)
    elif fun == 'rgb':
        result = list_of_rgb_colors(x)

    return result

generate_colors('hexa',3)
generate_colors('rgb',1)

#QLEVEL3
#Q1
def shuffle_list(list):
    random.shuffle(list)
    return list
print(shuffle_list([1,2,3,4,5]))
    
#Q2
def unique_random_nums():
    return random.sample([0,1,2,3,4,5,6,7,8,9],k=7)
print(unique_random_nums())