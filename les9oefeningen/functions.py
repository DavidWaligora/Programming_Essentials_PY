vegetables1 = {'tomato', 'celery', 'endive', 'fennel' }
vegetables2 = {'cucumber', 'tomato', 'celery'}
vegetable_union = vegetables1.union(vegetables2)
vegetable_difference = vegetables1.difference(vegetables2)
vegetable_intersection = vegetables1.intersection(vegetables2)
print('union:', vegetable_union)
print('difference:', vegetable_difference)
print('intersection:', vegetable_intersection)
vegetables1.add("bla")
vegetables1.remove("bla")
vegetables1.clear()

vegetables1 = {'tomato', 'celery', 'endive', 'fennel' }
vegetables2 = {'cucumber', 'tomato', 'celery'}
vegetables3 = {'endive', 'fennel'}
print(vegetables2.issubset(vegetables1)) #False
print(vegetables3.issubset(vegetables1)) #True
print(vegetables1.issubset(vegetables1)) #True
print(vegetables2.issuperset(vegetables3)) #False
print(vegetables1.issuperset(vegetables3)) #True
print(vegetables1.isdisjoint(vegetables2)) #False
print(vegetables2.isdisjoint(vegetables3)) #True


letters = {'e': 1, 'h': 1, 'n': 1, 'o': 2, 't': 4}
# letters["t"] # 4

print(letters.get("a", 'This character does not occur'))
print(letters.get("e", 'This character does not occur')) #1


# go through letters in word
word = "abcde"
characters = {}
for letter in word:
# check if letter is present in dictionary
    if letter in characters:
        characters[letter] += 1
        # increase value via key
    else:
        characters[letter] = 1
        # create new key/value pair

for character in characters:
    print(character, characters[character])
    #key -> value t 4

del characters["a"] # removes key value pair
characters.clear()

# total number of letters
print('Total:',sum(characters.values()), 'chars')
print('Total:',sum(characters.keys()), 'keys')

sorted(characters) #sorts temporary
# sorted(characters, reversed=True) #sorts temporary reversed