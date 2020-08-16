
int_list = [x for x in range(100)]
import random
from collections import Counter
def div_3(x):
    if x % 3 == 0:
        return  'fizz'
    else: return ''
def div_5(x):
    if x % 5 == 0:
        return 'buzz'
    else: return ''
def div_3_5(x):
    return (x % 3 == 0) or (x % 5 == 0)

def fizz_buzz(x):
    word = ''
    if ((x % 3 != 0) and (x % 5 != 0)):
        return str(x)
    elif (x % 3 == 0) and (x % 5 == 0):
        return 'fizzbuzz'
    elif(x % 5 == 0):
        return 'buzz'
    else:
        return 'fizz'

int_list3 = list(map(fizz_buzz  , int_list))

int_list2 = [div_3_5(x) for x in int_list]

int_list1 = [str(div_3(x))+str(div_5(x)) if div_3_5(x) else x for x in int_list]

counts = Counter(int_list1)
print(counts)


all_words = "all the words in the world".split()

def get_random_word():
    return random.choice(all_words)

my_as = 'this is a str'
my_as1 = my_as[::-1]
print(my_as1)
