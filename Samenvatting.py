#ask for input
text = input('give me a text: ')

#print output
print('This is the text:')
print(text)

#convert variables and get type of variable
#type of variables: int, float, str, bool, list, tuple, dict, set, NoneType
type_number = int(5)
type_string = str(type_number)
type_float = float(type_number)
boolean = True
type_list = [1, 2, 3, 'a', 'b', 'c']
type_tuple = tuple(type_list)
type_set = set(type_list)
list2 = list(type_tuple)
type_dict = {1:"One" , 2 : "Two" , 3 : "Three"}

#operators
#Equals             ==
#Is not Equal       !=
#less than          <
#greater than       >
#less or equal      <=
#greater or equal   >=
#logical operators  and/or

#a big if-else structure can be replaced by match-case
variable = 1
match variable:
    case 1:
        print('The value is 1')
    case 2:
        print('The value is 2')
    case 3:
        print('The value is 3')

#seperator and end parameter for print
#No space, all together
print('seperator examples')
print('G','F','C', sep='')
#space in between
print('G','F','C', sep=' ')
#@ in between
print('G','F','C', sep='@')

#Space in between, don't go to a new line
print('end='' examples' )
print('G','F','C', end=' ')
print('followed by text without new line')

#String functions
print('string functions')
#length of a string, can also be used for lists etc
length = len(text)
#character to ASCII
ord('e')
#ASCII to character
chr(101)

#get 1 or multiple characters out of string
#name_string[start:end:jump_size], end itself is not included
#second and third character
print(text[1:3])
#print complete string in steps of 2
print(text[::2])

#string functions
print('string functions: ')
#capitalize, first letter to uppercase
print(text.capitalize())
#lowercase, full string to lowercase
print(text.lower())
#uppercase, full string to uppercase
print(text.upper())
#remove leading and trailing whitespaces
print(text.strip())
#remove leading whitespaces
print(text.lstrip())
#remove trailing whitespaces
print(text.rstrip())
#count how often a string occurs within the string
print(text.count('a'))
#look up first position where a string occurs
print(text.find('a'))
#replace string by another string
print(text.replace('a','c'))

#tuple and list functions
print('tuple and list functions')
#receive number of elements in a list/tuple
string='1 2 3 4 5 6 7 8 9 10 11 12'
#stop alle waarden als int in een lijst gebruik makende van string.split en list() + map()
lijst_getallen = list(map(int, string.split()))
print(lijst_getallen)

len(type_list)
#search index of value 'a'
type_list.index('a')
#slicing a list, print index 1 to 3, last one is not included
print(type_list[1:4])
#check if 'a'is in the list
if 'a' in type_list:
    print('a is in the list')
#add value to the list
type_list.append('d')
#add an element at indicated position: add 4 on position 3
type_list.insert(3, 4)
#delete the first element of the specified value: remove the 4
type_list.remove(4)
#delete element at indicated position: delete 'd' at end of list (position -1)
type_list.pop(-1)
#sort the elements from low to high
list_sorting=[5,4,5,6,2,1,3,10,15,54,58]
list_sorting.sort()
print('niet gesorteerde lijst: ', list_sorting)
#add a second list/tuple to the list
type_list.extend(type_tuple)
#count number of occurrences of 'a' in the list
type_list.count('a')
#reverse order of the list
type_list.reverse()
#remove elements from list based on index: remove first element
del type_list[0]
#delete last 3 elements, last index is included
del type_list[-3:-1]
#determine min, max or sum of numbers in a list
max(list_sorting)
min(list_sorting)
sum(list_sorting)
print('gesorteerde lijst: ', list_sorting)
#you can add 2 lists together
new_list = type_list + list(type_tuple)
#you can multiply a list as well, just like a string
print(type_list * 4)

#compare lists using <, >, output will be True or False, you can only compare str or int to same type.
strings1 = ['a', 'b', 'c']
numbers1 = [1, 2, 3]
strings2 = ['d', 'e', 'f']
numbers2 = [4, 5, 6]
#result = True
result = strings1 < strings2
#result2 = False
result2 = numbers2 < numbers1

#use is to compare if memory location of both lists is equal
a = [1, 2, 3]
b = [1, 2, 3]
#result will be True or False
not_same = a is b
#use == to check if content of lists is the same, result is True or False
same = a==b
#find memory location using id
memory_location_a = id(a)
memory_location_b = id(b)

#you can use nested lists to link data together
list_hours_day = [['Mon', 6], ['Tue', 4.5], ['Wed', 3], ['Thu', 0], ['Fri', 4.5]]
#get the hours of Tuesday out of the list by using double index
hours_tuesday = list_hours_day[1][1]

#Functions
print('Information regarding Functions')
#import random to randomly generate numbers
import random

#example define a function to generate a list or random numbers
def generate_list(numbers,lower_limit,upper_limit):
    """
    Function to generate a list of random numbers between upper and lower limit
    :param numbers: amount of numbers to be generated
    :param lower_limit: lower limit for randon number
    :param upper_limit: upper limit for random number
    :return: list of randomly generated values
    """
    list = []
    while numbers > 0:
        list.append(random.randint(lower_limit,upper_limit))
        numbers -= 1
    return list

#example 2: Define function to filter a list and only keep unique values
def filter_list(list):
    """
    Function to return a list of unique values
    :param list: input list
    :return: filtered list with unique values
    """
    list.sort()
    filtered_list = []
    for item in list:
        if item not in filtered_list:
            filtered_list.append(item)
    return filtered_list

#ask for user input
size = int(input("How long do you want the list to be: "))
lower_limit = int(input("Give the lower limit to generate random numbers: "))
upper_limit = int(input("Give the upper limit to generate random numbers: "))

#generate random list and print
randomlist = generate_list(size,lower_limit,upper_limit)
print("Random generated list:\n" , randomlist)

#return filtered list
filteredlist = filter_list(randomlist)
print("Filtered and sorted list:\n" , filteredlist)

#Text files
print('Text files information')
#open a text file, optionally add encoding (UTF-8 pr ASCII)
file = open('schedule.txt', encoding='UTF-8')
#read and display the full content
print(file.read())
#close file
file.close()

#use block to perform these actions in 1 block, no need to close file
with open('schedule.txt') as file:
    # read and display the full content
    print(file.read())

    #read line and strip trailing whitespaces
    line = file.readline().rstrip()

    #read all lines and place them in a list of strings
    all_lines = file.readlines()

    #keep looping to read remaining lines
    while line:
        #skip blank lines, only continue if not blank
        if line != '\n':
            #split data in one line, separated by a ',' (comma)
            record = line.split(';')
            print(record[1])
            #example
            #record[0] = '08/01'
            #record[1] = 'Application development in Python'
            #record[2] = '08:30\n'
        line = file.readline().rstrip()

    #print all lines in all_lines list, seperated by a space
    for line in all_lines:
        if line != '\n':
            print(line, end='')

    #write new lines to the file, important to use newline character \n
    file.write('25/11;Bob Potters; 08:30\n')
    file.write('30/11;René François; 12:30\n')
    file.write('02/12;Chris Benz; 10:15\n')

#write to file within one block, make a list to write
appointments = []
appointments.append('25/11;Bob Potters; 08:30\n')
appointments.append('30/11;René François; 12:30\n')
appointments.append('02/12;Chris Benz; 10:15\n')

#you can open a file in add or write mode to add lines, write mode cleans an existing file:
#check if file exists, if existing, open in add mode, import exists to check
from os.path import exists

#open in add mode if file exists ('a')
if exists('schedule.txt'):
    with open('schedule.txt', 'a', encoding='UTF-8') as file:
        # use writelines() to write all elements in a list.
        file.writelines(appointments)
else:
#open in write mode ('w')
    with open('schedule.txt', 'w', encoding='UTF-8') as file:
        # Write data to file
        file.write('25/11;Bob Potters; 08:30\n')
        file.write('30/11;René François; 12:30\n')
        file.write('02/12;Chris Benz; 10:15\n')

#group data information
print('Group data information')

#use indicative to use as indication
text = 'aaaaadddppppppsssssssssww'
print('The compressed text: ', end='')
i = 0

#loop through complete text
while i < len(text):
    #set indicative
    characterind = text[i]
    number_characters = 0
    #loop as long as character is the same as indicative
    while i < len(text) and text[i] == characterind:
        number_characters += 1
        i += 1
    #print the output
    print('('+str(number_characters)+characterind+')', end='')

print()

#Set and Dictionary
# Set = collection in which each individual element can only be stored once.
# You cannot sort a set, but you can convert to a list to sort.
print('Set and Dictionary')
numbers = {10, 90, 70, 56}
french_letters = set()
for sign in "éçàèéàèçé":
    french_letters.add(sign)
vowels = set('aeiou')
squares = set(x**2 for x in range(10))

print(numbers)
print(french_letters)
print(vowels)
print(squares)

#Remove element
french_letters.remove('é')
#Add element
french_letters.add('é')
#clear full set
french_letters.clear()

vegetables1 = {'tomato', 'celery', 'endive', 'fennel' }
vegetables2 = {'cucumber', 'tomato', 'celery'}

# Union delivers a set that contains all the elements of both sets.
vegetable_union = vegetables1.union(vegetables2)
# Difference delivers a set that only occurs in the first set and not in the second set.
vegetable_difference = vegetables1.difference(vegetables2)
# intersection delivers a set that contains the elements that both sets have in common.
vegetable_intersection = vegetables1.intersection(vegetables2)

print('union:', vegetable_union)
print('difference:', vegetable_difference)
print('intersection:', vegetable_intersection)

# issubset True if all elements of the first set are also present in the set, which you specify as parameter
# issuperset True if all elements of the set, which you specify as parameters, are also present in the first set
# isdisjoint True if both sets have no elements in common
vegetables1 = {'tomato', 'celery', 'endive', 'fennel' }
vegetables2 = {'cucumber', 'tomato', 'celery'}
vegetables3 = {'endive', 'fennel'}
print(vegetables2.issubset(vegetables1))         #False
print(vegetables3.issubset(vegetables1))         #True
print(vegetables1.issubset(vegetables1))         #True

print(vegetables2.issuperset(vegetables3))       #False
print(vegetables1.issuperset(vegetables3))       #True

print(vegetables1.isdisjoint(vegetables2))       #False
print(vegetables2.isdisjoint(vegetables3))       #True

# A dictionary is an unordered, changeable collection consisting of key-value pairs
# The key is unique so you can use it to retrieve any value
# You can imagine a dictionary as a table with two columns
letters = {'e': 1, 'h': 1, 'n': 1, 'o': 2, 't': 4}
print('Occurrences of letter t:', letters['t'])

#Get returns the number of times the value is found
my_choice = input('Letter? ')
#returns the number if found, text if not found
print(letters.get(my_choice, 'This character does not occur'))

# print key/value pairs
for character in letters:
    print(character, letters[character])

# Delete key/value pair ('e': 1) of letter 'e' from letters
del letters['e']

#Clear dictionary can be done using clear()
letters.clear()
letters = {'e': 1, 'h': 1, 'n': 1, 'o': 2, 't': 4}

# If you don't want to work with pairs but with the keys and the values separately, you can retrieve these iterators using the methods keys() and values().
# For example, suppose you want to know the total number of characters based on the dictionary:
# total number of letters
print('Total:',sum(letters.values()), 'chars')

# By definition, a dictionary is a set of unordered key/value pairs.
# There is no method to sort the pairs internally.
# With the help of the sorted() function you can show the pairs sorted (low => high)
for character in sorted(letters):
    print(character, letters[character])

#by using reverse you can reverse sort order high => low
for character in sorted(letters, reverse=True):
    print(character, letters[character])

#Example Count:letters in a word
word = input('Enter a word: ')
characters = {}

# go through letters in word
for letter in word:
    # check if letter is present in dictionary
    if letter in characters:
        characters[letter] += 1
        # increase value via key
    else:
        characters[letter] = 1
        # create new key/value pair

# print key/value pairs
for character in characters:
    print(character, characters[character])
