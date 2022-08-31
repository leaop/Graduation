"""LISTAS"""
mylist = ["apple", "samsung", "motorola"]

"""
List items are: 
- ordered(the order not change without a command), 
- changeable(we can change, remove and add), and 
- allow duplicate values (Since lists are indexed, lists can have items with the same value)
we can use any data type: "apple", 2, True, 2k, 2.4

print(mylist)
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage
print(len(mylist))
#how many itens a list has
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))
#to show the type of variable
#list are created with []
print(list1[1])
#the index of list starts in 0
#to access the specific item we use [] + number of index (positive or negative)
#print(sum(mylist)) this function just work in 'int'. This is for add the values in list
print(min(mylist))
print(max(mylist))#this is for show the greater value in the list and 'min' is for the minimum
mylist.pop() #remove the last item
print(mylist)
#mylist.remove("apple") - in this case we use for remove a especific item from the list
list3 = ["a", "b", "c"]
del list3 #here I exclude the list totally
list4 = ["Ana", "Aluizio", "Alberto", "inicio"]
#list4.reverse() - this function reverse the order
list4.sort(key = str.lower) #the function sort put a chronological order. The key=str.lower is a step: all elements will be transform in tiny
print(list4)
list.extend(list3) # is equal 'list = list + list 2' and for x in list2: list.append(x)/print(list)
print(list)
list4.append("d") #To add an item to the end of the list
print(list4)
list4.insert(2,"Bia") #To insert a list item at a specified index
print(list4)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
"""

"""DICT"""
"""The dictionary is ordered, changeable but not allow duplicate value"""
"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
w = thisdict.get("brand")
print(w) #this is the same as X... is the function get
y = thisdict.keys()
print(y)
z = thisdict.keys()
thisdict["color"] = "white"
print(z)
q = thisdict.values()
thisdict["year"] = 2020
print(q)
print(thisdict.values())
thisdict["id"] = 'pbz2030' #So, I can create a new item with this command. In other cases, I was saying the new value of the new atribute: the w is a variable who call the valor brand
print(thisdict.keys())
c = thisdict.items()
print(c)
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  thisdict.update({"model": "Maverick"})
  thisdict.popitem() #allways remove the last
print(thisdict)
del thisdict["brand"] # I can del an specific item or the dict 
print(thisdict)
#thisdict.clear() = this not remove the dict, just clear the dict
for x in thisdict:
  print(x) #Print all key names
  print(thisdict[x]) # Print all values in the dictionary
"""

"""TUPLE"""
"""The tuples are ordered, unchangeable and allow duplicate values"""
"""
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#we can 'create' a tuple with one item, but we have to put a comma after the item
tuple2 = ("blossom",)
tuple3 = ("grape", 1, 4, True, False)
print(type(tuple3))
thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
#to update the tuple, we can transforme the tuple in list, update the item and transform into tuple again
print(x)
print(type(x))
#any update (add, remove, change) we have to do this: transform in a list, after in a tuple
#to unpacking tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
"""